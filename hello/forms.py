from flask.ext.wtf import Form
from wtforms import TextField, validators, PasswordField
# from werkzeug import secure_filename
# from flask_wtf.file import Filefield

class CommentForm(Form):
    text = TextField('Comment', [validators.Required()])

class LoginForm(Form):
    username = TextField("username")
    password = PasswordField("password")

# class PhotoForm(Form):
# 	photo = FileField('Your Photo')

