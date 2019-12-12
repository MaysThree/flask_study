from flask import Blueprint

# 1.第一个参数不能与对象名重复。2.第二个参数用来初始化
news_list = Blueprint('news', __name__)


@news_list.route('/news')
def news():
    return '新闻模块'
