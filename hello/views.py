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
    #request.values is where the json for you to access
    data = request.values.keys()
    #print loginuser.user_id
    #profile_link = "/viewprof/{0}".format(User.user_id)
    print current_user
    #print profile_link
    if len(data)>0:
	print data[0]
    	db.session.add(UserProfile(data[0]))
	db.session.commit()
    	return redirect(url_for('index'))
    comments = UserProfile.query.order_by(db.desc(UserProfile.comment_id))
    return render_template('index.html', comments=comments)

@app.route('/viewprof', methods=['GET'])
def viewprof():
    #print username.__class__
    strusr = unicodedata.normalize('NFKD', username).encode('ascii','ignore')
    #print strusr.__class__
    s = text(
	"SELECT p.doc "
	    "FROM user_profile p "
	    "WHERE p.doc.Profname = :x " 
    )
    results = db.engine.execute("""SELECT p.doc FROM user_profile p WHERE p.doc.Profname = :x""", x=strusr).first().items()[0][1]
    print results
    data = json.loads(results)
    print data
    return "hello"
    #return render_template('viewprof.html', comments=data) 


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
		return redirect(request.args.get("next") or url_for('index'))
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




	
	
