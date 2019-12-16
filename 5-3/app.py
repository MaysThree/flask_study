from flask import Flask, render_template, request
from os import path
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(path.join('static/uploads', filename))
    return 'upload success!'


if __name__ == '__main__':
    app.run()
