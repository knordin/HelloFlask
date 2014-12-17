from flask.ext.wtf import Form
from wtforms import TextField, validators, PasswordField, SelectMultipleField, widgets
# from werkzeug import secure_filename
# from flask_wtf.file import Filefield

class CommentForm(Form):
    text = TextField('Comment', [validators.Required()])

class LoginForm(Form):
    username = TextField("username")
    password = PasswordField("password")

data = [('expSF', 'exploring SF'), ('nightlife', 'nightlife'), ('outdoors', 'outdoors'), ('sports', 'sports'), ('videogames', 'video games')]

class SearchForm(Form):
    Profname = TextField("Name")
    about = TextField("About Me")
    age = TextField("Age")
    email = TextField("Email")
    phone = TextField("Phone Number")
    interests = SelectMultipleField("Interests", 
	choices = data,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
	)
    loc = TextField("Location")
    group = TextField("Group")
    empid = TextField("Employee ID")
    school = TextField("School")
    gradYear = TextField("Graduation Year")
    involv = TextField("Involvement")
    

# class PhotoForm(Form):
# 	photo = FileField('Your Photo')

