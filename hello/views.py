from flask import render_template, url_for, redirect, request, flash
from forms import CommentForm, LoginForm
from hello import app, db, login_manager, db_connection
from models import UserProfile, User
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, current_user
from sqlalchemy.sql import text
import datetime
import json
import unicodedata
import ast

@app.route('/myprofile', methods=['GET', 'POST'])
def index():
    print "current user", current_user.username
    data = request.values.keys()
    print data
    if len(data)>0:
	print data[0]
        #do we have this profile already?
        existing = db_connection.execute("""SELECT p.comment_id, p.doc FROM user_profile p where p.doc.Profname = :x""", x=current_user.username).fetchone()[0]
        print "existing", existing
        if existing:
            this_profile = UserProfile.get(existing)
            this_profile.doc = data[0]
            db.session.commit()
        else:
            db.session.add(UserProfile(data[0]))
            db.session.commit()
    	return redirect(url_for('index'))
    comments = UserProfile.query.order_by(db.desc(UserProfile.comment_id))
    return render_template('index.html', comments=comments, current_user=current_user)

@app.route('/viewprof/<username>', methods=['GET'])
def viewprof(username):
	print current_user.username
	print current_user.is_anonymous()
	print current_user.is_anonymous
	results = db_connection.execute("""SELECT p.doc FROM user_profile p WHERE p.doc.username = :x""", x=current_user.username)
	results = results.fetchone()[0]
	data = json.loads(results)
        print data
 	return render_template('viewprof.html', comments=data) 

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/search", methods=['POST'])
def search_post(): 
    sql = """SELECT p.doc FROM user_profile p """
    where_clause = []
    for i in ['Profname','about','age','email','phone','loc','group','empid','school','gradYear','involv']:
	if request.form[i] != "":
	    where_clause.append("lower(p.doc." + i + ") like '%" + request.form[i] +"%' ")
    if len(where_clause) > 0:
        all_wheres = " AND ".join(where_clause)
	sql = sql + "WHERE " + all_wheres
    print "SQL!!!!", sql
    search_results = db_connection.execute(sql).fetchall()
    print search_results
    results = []
    for i in range(len(search_results)):
        dict_string = ast.literal_eval(search_results[i][0])
        results.append(dict_string)
    return render_template('results.html', comments=results)
 
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
    			flash("Logged in successfully.")
    			return redirect(request.args.get("next") or url_for('index'))
    	else: 
    		flash("Incorrect Username/Password Combination")
    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
	return User.get(int(user_id))




	
	
