from flask import render_template, url_for, redirect, request, flash
from forms import CommentForm, LoginForm
from hello import app, db, login_manager
from models import UserProfile, User
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, current_user
from sqlalchemy.sql import text
import datetime
import json
import unicodedata

@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.values.keys()
    if len(data)>0:
	print data[0]
    	db.session.add(UserProfile(data[0]))
	db.session.commit()
    	return redirect(url_for('index'))
    comments = UserProfile.query.order_by(db.desc(UserProfile.comment_id))
    return render_template('index.html', comments=comments, current_user=current_user)

@app.route('/viewprof/<username>', methods=['GET'])
def viewprof(username):
	print current_user.username
	results = db.engine.execute("""SELECT p.doc FROM user_profile p WHERE p.doc.username = :x""", x=current_user.username).first().items()[0][1]
	print results
	data = json.loads(results)
 	return render_template('viewprof/<username>', comments=data) 


@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	username = request.form['username']
    	password = request.form['password']
    	user = User.get_by_username(username)
    	if user is not None:
    		if user.password == password:
    			login_user(user)
    			flash("Logged in successfully.")
    			return redirect(request.args.get("next") or url_for('index'))
    	else: 
    		flash("Incorrect Username/Password Combination")
    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
	return User.get(int(user_id))




	
	
