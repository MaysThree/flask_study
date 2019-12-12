from flask import Blueprint

product_list = Blueprint('products', __name__)


@product_list.route('/products')
def products():
    return '产品模块'
