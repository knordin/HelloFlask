from flask import render_template, url_for, redirect, request
from forms import CommentForm, LoginForm
from hello import app, db, login_manager
from models import Profile
from flask.ext.login import LoginManager, UserMixin, login_required
import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
   # request.values is where the json for you to access
    data = request.values.keys()
    if len(data)>0:
	print data[0]
    	db.session.add(Profile(data[0]))
	db.session.commit()
    	return redirect(url_for('index'))
    comments = Profile.query.order_by(db.desc(Profile.comment_id))
    return render_template('index.html', comments=comments)

@app.route('/viewprof', methods=['GET'])
def viewprof():
    comments = Profile.query.order_by(db.desc(Profile.comment_id))
    return render_template('viewprof.html', comments=comments)

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
	login_user(user)
	flash("Logged in successfully.")
	return redirect(request.args.get("next") or url_for("index"))
    return render_template('login.html', form=form)

@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
	token = request.args.get('token')
    if token is not None:
	username,password = token.split(":")
	user_entry = User.get(username)
	if(user_entry is not None):
	    user = User(user_entry[0], user_entry[1])
	    if(user.password == password):
		return user
    return None
	
