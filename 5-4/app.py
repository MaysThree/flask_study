from flask import Flask, render_template, request, send_from_directory
import time
import os
from os import path
from werkzeug.utils import secure_filename
import platform
from werkzeug.datastructures import CombinedMultiDict
from forms import UploadForm

app = Flask(__name__)

if platform.system() == 'Windows':
    slash = '\\'
else:
    # platform.system() == 'Linux'
    slash = '/'

UPLOAD_PATH = path.curdir + path.sep + 'uploads' + path.sep
# UPLOAD_PATH = path.curdir + slash + 'uploads' + slash


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        if not path.exists(UPLOAD_PATH):
            os.mkdir(UPLOAD_PATH)
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            f = request.files['file']
            filename = secure_filename(f.filename)  # 会丢失中文名字
            ext = filename.rsplit('.')[-1]
            print(ext)
            # ext = filename.rsplit('.', 1)[1]
            # unix_time = int(time.time())
            # new_filename = str(unix_time) + '.' + ext
            # file_url = UPLOAD_PATH + new_filename
            file_url = UPLOAD_PATH + filename
            f.save(file_url)
            return 'upload success'
        else:
            return '不支持问格式文件！'


@app.route('/images/<filename>/', methods=['POST', 'GET'])
def get_image(filename):
    dir_path = path.join(app.root_path, 'uploads')
    # 下载模式
    # return send_from_directory(dir_path, filename, as_attachment=True)
    # 在线浏览
    return send_from_directory(dir_path, filename)


if __name__ == '__main__':
    app.run()
