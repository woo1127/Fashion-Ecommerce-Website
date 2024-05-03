import sqlalchemy as sa
import sqlalchemy.orm as so
from extensions import db
from utils import deep_get
from models import Product
from collections import Counter
from apiflask import APIBlueprint
from responses import error_response, render_response
from flask import request, jsonify, current_app as app


product_bp = APIBlueprint('product', __name__, url_prefix='/api/product')


def get_filter_values(data, field, top=10):
    values = (deep_get(item, field) for item in data)
    counter = Counter(list(values)).most_common(top)
    keys = [key for key, _ in counter]
    return keys


@product_bp.get("/search")
def search():   
    search_keyword = request.args.get('q', "")
    page = request.args.get('page', 1, type=int)
    gender = request.args.get('gender', None)
    category = request.args.get('category', None)
    sub_category = request.args.get('subCategory', None)

    if page < 1:
        return error_response(400, "Invalid page number")

    filters = []
    if gender:
        filters.append(Product.gender == gender)
    if category:
        filters.append(Product.category == category)
    if sub_category:
        filters.append(Product.sub_category == sub_category)

    query, _ = Product.search("name", search_keyword)
    query = query.filter(*filters)
    products = db.paginate(query, page=page, per_page=app.config["PRODUCTS_PER_PAGE"], error_out=False)
    product_list = [product.to_dict() for product in products.items]
    total = len(product_list)

    if (total == 0):
        return error_response(404, "No products found")
    
    data = {
        'total': total,
        'products': product_list,
        'filters': {
            "category": get_filter_values(product_list, "category"),
            "subCategory": get_filter_values(product_list, "subCategory")
        },
        'previous': products.prev_num if products.has_prev else None,
        'next': products.next_num if products.has_next else None
    }
    return render_response(data=data)


@product_bp.get("/<int:product_id>")
def get_product_info(product_id: int):
    product = db.session.get(Product, product_id)

    if not product:
        return error_response(404, "Product not found")
    return render_response(data=product.to_dict())
