from wtforms import Form,FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed


class UploadForm(Form):
    file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'txt'])])
