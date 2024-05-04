import sqlalchemy as sa
import sqlalchemy.orm as so
from extensions import db
from apiflask import APIBlueprint
from flask import request, jsonify
from responses import error_response, render_response
from flask_jwt_extended import jwt_required, current_user
from models import Cart, Product, ProductColor, ProductSize


cart_bp = APIBlueprint('cart', __name__, url_prefix='/api/cart')


@cart_bp.post("/add")
@jwt_required()
def add_cart_item():
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')
    color_id = request.json.get('color_id')
    size_id = request.json.get('size_id')
    quantity = request.json.get('quantity')
    total_price = request.json.get('total_price')

    cart = Cart(user_id=user_id, product_id=product_id, color_id=color_id, size_id=size_id, quantity=quantity, total_price=total_price)

    db.session.add(cart)
    db.session.commit()

    return render_response()


@cart_bp.post("/update")
@jwt_required()
def update_cart_item():
    cart_id = request.json.get('cart_id')
    update_fields = request.json.get('update_fields')
    
    item = db.session.get(Cart, cart_id)

    if not item:
        return error_response(404, "Item not found")

    for key in update_fields.keys():
        if key not in Cart.__table__.columns.keys():
            return error_response(400, f"Invalid field: {key}")

    db.session.execute(sa.update(Cart).where(Cart.id == cart_id).values(**update_fields))
    db.session.commit()

    item = db.session.get(Cart, cart_id)
    item_info = item.to_dict()
    item_info.update({
        'product_detail': db.session.get(Product, item_info['product_id']).to_dict(),
        'color_detail': db.session.get(ProductColor, item_info['color_id']).to_dict(),
        'size_detail': db.session.get(ProductSize, item_info['size_id']).to_dict()
    })

    return render_response(data=item_info)


@cart_bp.post("/get_cart_info")
@jwt_required()
def get_cart_info():
    if not current_user.carts:
        return error_response(404, 'Cart is empty')

    items = [item.to_dict() for item in current_user.carts]

    for item in items:
        item.update({
            'product_detail': db.session.get(Product, item['product_id']).to_dict(),
            'color_detail': db.session.get(ProductColor, item['color_id']).to_dict(),
            'size_detail': db.session.get(ProductSize, item['size_id']).to_dict()
        })

    return render_response(data=items)


@cart_bp.post("/delete")
@jwt_required()
def delete_cart_item():
    cart_id = request.json.get("cart_id")
    item = db.session.get(Cart, cart_id)

    if not item:
        return error_response(404, "Item not found")

    db.session.delete(item)
    db.session.commit()

    return render_response()
    