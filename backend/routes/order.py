import uuid
import random
import sqlalchemy as sa
from extensions import db
from apiflask import APIBlueprint
from flask import request, jsonify
from responses import error_response, render_response
from flask_jwt_extended import jwt_required, current_user
from models import Order, OrderItem, Cart, User, Product, ProductColor, ProductSize


order_bp = APIBlueprint('order', __name__, url_prefix='/api/order')


def generate_random_order_id():
    order_id = random.randint(10000000, 99999999)

    if db.session.get(Order, order_id):
        generate_random_order_id()
    return order_id
    

@order_bp.post("/get/<int:order_id>")
@jwt_required()
def get_order(order_id):
    order = db.session.get(Order, order_id)
    username = db.session.get(User, current_user.id).username

    if not order:
        return error_response(404, 'Order not found')

    data = order.to_dict()
    data['username'] = username

    return render_response(data=data)


@order_bp.post("/create")
@jwt_required()
def create_new_order():
    cart_ids = request.json.get('cart_ids')
    user_id = current_user.id
    payment_method = request.json.get('payment_method')
    items = Cart.query.filter(Cart.id.in_(cart_ids)).all()

    order = Order(
        id=generate_random_order_id(),
        user_id=user_id,
        total_price=sum([item.total_price for item in items]),
        payment_method=payment_method,
        transaction_id=str(uuid.uuid4()),
        items=[
            OrderItem(
                product_id=item.product_id,
                color_id=item.color_id,
                size_id=item.size_id,
                quantity=item.quantity,
                total_price=item.total_price
            ) for item in items
        ],
    )

    # delete item in Cart Table after create order
    Cart.query.filter(Cart.id.in_(cart_ids)).delete(synchronize_session=False)

    db.session.add(order)
    db.session.commit()

    return render_response(data=order.to_dict())


@order_bp.post("/list")
@jwt_required()
def list_orders():
    user_id = current_user.id
    orders = Order.query.filter(Order.user_id == user_id).all()
    orders_info = [order.to_dict() for order in orders]

    for order in orders_info:
        for item in order['items']:
            item.update({
                'product_detail': db.session.get(Product, item['product_id']).to_dict(),
                'color_detail': db.session.get(ProductColor, item['color_id']).to_dict(),
                'size_detail': db.session.get(ProductSize, item['size_id']).to_dict()
            })

    return render_response(data=orders_info)


@order_bp.post("/delete")
@jwt_required()
def delete_order():
    order_id = request.json.get('order_id')
    order = db.session.get(Order, order_id)

    if not order: 
        return error_response(404, 'Order not found')

    db.session.delete(order)
    db.session.commit()

    return render_response()