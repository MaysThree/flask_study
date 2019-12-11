from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    book = {
        'name': 'maysthree',
        'age': 26
    }
    return render_template('index.html', book=book)


@app.route('/test1')
def test1():
    render_template('test1.html')


@app.route('/test2')
def test2():
    render_template('test2.html')


if __name__ == '__main__':
    app.run()
