import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import List
from extensions import db
from dataclasses import dataclass
from datetime import datetime, timezone
from whoosh.fields import ID, TEXT
from searcher.mixin import SearchableMixin
from werkzeug.security import check_password_hash, generate_password_hash


@dataclass
class Product(SearchableMixin, db.Model):
    __tablename__ = 'products'
    __searchable__ = {
        'id': ID(stored=True, unique=True),
        'name': TEXT(stored=True),
        'brand_name': TEXT(stored=True)
    }

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(250), nullable=False, index=True)
    price: float = db.Column(db.Float, nullable=False, index=True)
    brand_name: str = db.Column(db.String(50), index=True)
    description: str = db.Column(db.String)
    category: str = db.Column(db.String(20), index=True)
    sub_category: str = db.Column(db.String(20), index=True)
    gender: str = db.Column(db.String(10))
    season: str = db.Column(db.String(10))
    year: int = db.Column(db.Integer)
    images: so.Mapped[List['ProductImage']] = so.relationship('ProductImage', back_populates='product', lazy=True)
    colors: so.Mapped[List['ProductColor']] = so.relationship('ProductColor', back_populates='product', lazy=True)
    sizes: so.Mapped[List['ProductSize']] = so.relationship('ProductSize', back_populates='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.id} {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'brand_name': self.brand_name,
            'description': self.description,
            'category': self.category,
            'sub_category': self.sub_category,
            'gender': self.gender,
            'season': self.season,
            'year': self.year,
            'images': [image.to_dict() for image in self.images] if self.images else [],
            'colors': [color.to_dict() for color in self.colors] if self.colors else [],
            'sizes': [size.to_dict() for size in self.sizes] if self.sizes else [],
        }
    

@dataclass
class ProductColor(db.Model):
    __tablename__ = 'product_colors'

    id: int = db.Column(db.Integer, primary_key=True)
    product_id: int = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    primary_color: str = db.Column(db.String(15), nullable=False)
    secondary_color: str = db.Column(db.String(15))
    url: str = db.Column(db.String)
    product: so.Mapped['Product'] = so.relationship('Product', back_populates='colors', lazy=True)

    def __repr__(self):
        return f'<Color {self.id} {self.value}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'primary_color': self.primary_color,
            'secondary_color': self.secondary_color,
            'url': self.url
        }
    

@dataclass
class ProductSize(db.Model):
    __tablename__ = 'product_sizes'

    id: int = db.Column(db.Integer, primary_key=True)
    product_id: int = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    value: str = db.Column(db.String(10))
    product: so.Mapped['Product'] = so.relationship('Product', back_populates='sizes', lazy=True)

    def __repr__(self):
        return f'<ProductSize {self.id} {self.value}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'value': self.value
        }
    

@dataclass
class ProductImage(db.Model):
    __tablename__ = 'product_images'

    id: int = db.Column(db.Integer, primary_key=True)
    product_id: int = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    url: str = db.Column(db.String)
    product: so.Mapped['Product'] = so.relationship('Product', back_populates='images', lazy=True)

    def __repr__(self):
        return f'<ProductImage {self.id} {self.product_id} {self.url}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url
        }


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(30), nullable=False, index=True)
    email: str = db.Column(db.String(50), nullable=False, index=True)
    password: str = db.Column(db.String(256), nullable=False)
    phone_number: str = db.Column(db.String(20), nullable=False)
    address: str = db.Column(db.String(256))
    created_at: datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    carts: so.Mapped[List['Cart']] = so.relationship('Cart', back_populates='user', lazy=True)
    orders: so.Mapped[List['Order']] = so.relationship('Order', back_populates='user', lazy=True)

    def __repr__(self):
        return f'<User {self.id} {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address,
            'created_at': self.created_at.replace(tzinfo=timezone.utc).isoformat(),
            'carts': [cart.to_dict() for cart in self.carts] if self.carts else [],
            'orders': [order.to_dict() for order in self.orders] if self.orders else [],
        }

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)


@dataclass
class Cart(db.Model):
    __tablename__ = 'carts'
    
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id: int = db.Column(db.Integer, db.ForeignKey('products.id'))
    color_id: int = db.Column(db.Integer, db.ForeignKey('product_colors.id'))
    size_id: int = db.Column(db.Integer, db.ForeignKey('product_sizes.id'))
    quantity: int = db.Column(db.Integer)
    total_price: float = db.Column(db.Float)
    created_at: datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    user: so.Mapped['User'] = so.relationship('User', back_populates='carts', lazy=True)

    def __repr__(self):
        return f'<Cart {self.id} {self.user_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,   
            'product_id': self.product_id,
            'color_id': self.color_id,
            'size_id': self.size_id,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'created_at': self.created_at.replace(tzinfo=timezone.utc).isoformat(),
        }


@dataclass
class Order(db.Model):
    __tablename__ = 'orders'

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'))
    total_price: float = db.Column(db.Float)
    created_at: datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    payment_method: str = db.Column(db.String(20))
    transaction_id: str = db.Column(db.String(256))
    user: so.Mapped['User'] = so.relationship('User', back_populates='orders', lazy=True)
    items: so.Mapped[List['OrderItem']] = so.relationship('OrderItem', back_populates='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.id} {self.user_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'total_price': self.total_price,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'payment_method': self.payment_method,
            'transaction_id': self.transaction_id,
            'items': [item.to_dict() for item in self.items] if self.items else [],
        }


@dataclass
class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id: int = db.Column(db.Integer, primary_key=True)
    order_id: int = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id: int = db.Column(db.Integer, db.ForeignKey('products.id'))
    color_id: int = db.Column(db.Integer, db.ForeignKey('product_colors.id'))
    size_id: int = db.Column(db.Integer, db.ForeignKey('product_sizes.id'))
    quantity: int = db.Column(db.Integer)
    total_price: float = db.Column(db.Float)
    order: so.Mapped['Order'] = so.relationship('Order', back_populates='items', lazy=True)

    def __repr__(self):
        return f'<OrderItem {self.id} {self.order_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'color_id': self.color_id,
            'size_id': self.size_id,
            'quantity': self.quantity,
            'total_price': self.total_price,
        }
