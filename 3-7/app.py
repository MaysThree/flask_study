from flask import Flask, render_template
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    goods = [{'name': 'close1'}, {'name': 'close2'},
             {'name': 'close3'}, {'name': 'close4'},
             {'name': 'close5'}]
    return render_template('index.html', **locals())


def do_index_class(index):
    if index % 3 == 0:
        return 'line'
    else:
        return ''


app.add_template_filter(do_index_class, 'index_class')


if __name__ == '__main__':
    app.run()
