from flask.ext.wtf import Form
from wtforms import TextField, validators, PasswordField

class CommentForm(Form):
    text = TextField('Comment', [validators.Required()])

class LoginForm(Form):
    username = TextField("username")
    password = PasswordField("password")



