from flask import Blueprint, request

bp = Blueprint('admin', __name__, subdomain='admin')


@bp.route('/')
def get_cookie():
    username = request.cookies.get('username')
    return username or 'no username obtain'
