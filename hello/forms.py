from flask.ext.wtf import Form
from wtforms import TextField, validators, PasswordField, SelectMultipleField, widgets

class CommentForm(Form):
    text = TextField('Comment', [validators.Required()])

class LoginForm(Form):
    username = TextField("username")
    password = PasswordField("password")

data = [('exploring', 'exploring'), ('nightlife', 'nightlife'), ('outdoors', 'outdoors'), ('sports', 'sports'), ('videogames', 'video games')]

class SearchForm(Form):
    Profname = TextField("Name")
    about = TextField("About Me")
    age = TextField("Age")
    email = TextField("Email")
    phone = TextField("Phone Number")
    interests = SelectMultipleField("Interests", 
	choices = data,
        option_widget=widgets.CheckboxInput(),
        widget = widgets.ListWidget(prefix_label=True)
	)
    loc = TextField("Location")
    group = TextField("Group")
    empid = TextField("Employee ID")
    school = TextField("School")
    gradYear = TextField("Graduation Year")
    involv = TextField("Involvement")

