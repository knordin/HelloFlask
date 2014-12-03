from flask import render_template, url_for, redirect, request, flash
from forms import CommentForm, LoginForm
from hello import app, db, login_manager
from models import Profile, User
from flask.ext.login import LoginManager, UserMixin, login_required, login_user
import datetime
import json

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
    contents = comments.first().text

    data = json.loads(contents)
    return render_template('viewprof.html', comments=data)

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
	user = load_user(request)
	if user is not None:
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("index"))
	else: 
		flash("Incorrect Username/Password Combination")
    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(request):
	username = request.form['username']
	password = request.form['password']

	user = User.get(username)
	if user is not None:
		if user.password == password:
			return user
	else:
		return None


# @app.route('/upload/', methods=['GET', 'POST'])
# def upload():
# 	form = PhotoForm()
# 	if form.validate_on_submit():
# 		filename = secure_filename(form.photo.data.filename)
# 		form.photo.data.save('uploads/' + filename)



	
	
