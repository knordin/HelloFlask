from flask import render_template, url_for, redirect, request, flash, render_template_string
from forms import CommentForm, LoginForm, SearchForm
from hello import app, db, login_manager, db_connection
from models import UserProfile, User
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, current_user
from sqlalchemy.sql import text
import datetime
import json
import unicodedata
import ast

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def index():
    data = request.values.keys()
    if len(data)>0:
        #do we have this profile already?
        existing = db_connection.execute("""SELECT p.comment_id, p.doc FROM user_profile p where p.doc.username = :x""", x=current_user.username).fetchone()[0]
        if existing:
            this_profile = UserProfile.get(existing)
            this_profile.doc = data[0]
            db.session.commit()
        else:
            db.session.add(UserProfile(data[0]))
            db.session.commit()
    	return redirect(url_for('viewprof', username=current_user.username))
    comments = UserProfile.query.order_by(db.desc(UserProfile.comment_id))
    return render_template('index.html', comments=comments, current_user=current_user)

@app.route('/viewprof/<username>', methods=['GET'])
@login_required
def viewprof(username):
	results = db_connection.execute("""SELECT p.doc FROM user_profile p WHERE p.doc.username = :x""", x=username)
	results = results.fetchone()[0]
	data = json.loads(results)
 	return render_template('viewprof.html', comments=data) 

@app.route("/search", methods=['GET','POST'])
@login_required
def search():
    form = SearchForm()
    if form.validate_on_submit():
        sql = """SELECT p.doc FROM user_profile p """
	where_clause = []
	for i in ['Profname','about','age','email','phone','loc','group','empid','school','gradYear','involv']:
	    if request.form[i] != "":
		where_clause.append("lower(p.doc." + i + ") like '%" + request.form[i] +"%' ")	
        for i in request.form.getlist('interests'):
	    where_clause.append("p.doc.inter." + i +" like 1")
	if len(where_clause) > 0:
	    all_wheres = " AND ".join(where_clause)
	    sql = sql + "WHERE " + all_wheres
	search_results = db_connection.execute(sql).fetchall()
	results =[]
	for i in range(len(search_results)):
            dict_string = json.loads(search_results[i][0])
	    results.append(dict_string)
	return render_template('results.html', comments=results)
    return render_template('search.html', form=form)

 
@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	username = request.form['username']
    	password = request.form['password']
    	user = User.get_by_username(username)
    	if user is not None:
    		if user.password == password:
    			login_user(user)
    			#flash("Logged in successfully.")
    			return redirect(request.args.get("next") or url_for('index'))
    	else: 
    		flash('Incorrect Username/Password Combination')
    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
	return User.get(int(user_id))




	
	
