from flask import Blueprint

bp = Blueprint('admin', __name__)


@bp.route('/admin')
def index():
    return '后台首页'
