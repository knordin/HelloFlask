from flask import render_template, url_for, redirect, request, flash, render_template_string
from forms import LoginForm, SearchForm, genSearchForm
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
    # logic for the edit my profile page
    # pull text from input fields and rewrite JSON entry in the DB associated with that profile
    form = SearchForm()
    if form.validate_on_submit():
	# creating dictionary to store text from input text fields
        s = {}
	for i in ['Profname','about','age','email','phone','loc','group','empid','school','gradYear','involv', 'picture']:
	    if request.form[i] != "":
		s[i] = request.form[i]
	    else:
		s[i] = ''
	s['inter'] = {}
	s['username'] = current_user.username
	for i in ['exploring', 'nightlife', 'outdoors', 'sports', 'videogames']:
	    if i in request.form.getlist('interests'):
		s['inter'][i] = 1
	    else:	
		s['inter'][i] = 0
	#converting dictionary to JSON
	json_string = json.dumps(s)
	#checking if a profile with the username already exists in the db
	result = db_connection.execute("""SELECT p.comment_id, p.doc FROM user_profile p WHERE p.doc.username = :x""", x=current_user.username).fetchone()[0] 
	if result:
	    this_profile = UserProfile.get(result)
	    this_profile.doc = json_string
	    db.session.commit()
	else:
	    db.session.add(UserProfile(json_string))
	    db.session.commit()
	return redirect(url_for('viewprof', username = current_user.username))
    return render_template('index.html', form=form)

@app.route('/viewprof/<username>', methods=['GET'])
@login_required
def viewprof(username):
    # logic for the view profile page
    # pull profile from the DB and return the results
    results = db_connection.execute("""SELECT p.doc FROM user_profile p WHERE p.doc.username = :x""", x=username)
    results = results.fetchone()[0]
    data = json.loads(results)
    return render_template('viewprof.html', comments=data) 

@app.route('/gensearch', methods=['GET','POST'])
@login_required
def gensearch():
    # logic for the general search page
    # creates SQL query based on text input and searches all fields in the JSON doc
    # example SQL statement created will look like:
    #     SELECT doc
    #     from user_profile
    #     where json_textcontains(doc, '$', 'jane')
    form = genSearchForm()
    if form.validate_on_submit():
	sql = """SELECT p.doc FROM user_profile p """
	if request.form['searchInput'] != "":
	    sql = sql + "WHERE json_textcontains(p.doc, '$', '" + request.form['searchInput'] +  "')"	
	search_results = db_connection.execute(sql).fetchall()
	results =[]
	for i in range(len(search_results)):
            dict_string = json.loads(search_results[i][0])
	    results.append(dict_string)
	return render_template('results.html', comments=results)
    return render_template('generalsearch.html', form=form)

@app.route("/search", methods=['GET','POST'])
@login_required
def search():
    # logic for the search page
    # creates sql query based on input fields in the search page, executes sql query on the DB, redirects to the results page
    # example sql statement created will look like this:
    #	SELECT p.doc 
    #	FROM user_profile p 
    #	WHERE lower(p.doc.Profname) like '%j%'  
    #	AND lower(p.doc.gradYear) like '%2014%'  
    #	AND p.doc.inter.outdoors like 1
    form = SearchForm()
    if form.validate_on_submit():
        sql = """SELECT p.doc FROM user_profile p """
	where_clause = []
        # search through each input field to check if there was inputted text
	# if yes, create a sql statement to search the JSON field for that text
	for i in ['Profname','about','age','email','phone','loc','group','empid','school','gradYear','involv']:
	    if request.form[i] != "":
		where_clause.append("lower(p.doc." + i + ") like '%" + request.form[i] +"%' ")	
        for i in request.form.getlist('interests'):
	    where_clause.append("p.doc.inter." + i +" like 1")
	# append all the AND sequel clauses
	# add in the WHERE clause followed by all the AND clauses
	if len(where_clause) > 0:
	    all_wheres = " AND ".join(where_clause)
	    sql = sql + "WHERE " + all_wheres	
	# execute the sql statement on the DB and return the results page showing all the matches
	search_results = db_connection.execute(sql).fetchall()
	results =[]
	for i in range(len(search_results)):
            dict_string = json.loads(search_results[i][0])
	    results.append(dict_string)
	return render_template('results.html', comments=results)
    return render_template('search.html', form=form)

@app.route("/", methods=['GET', 'POST'])
def login():
    # logic for login
    # confirms username & password combination is in DB before granting access to the rest of the application
    form = LoginForm()
    if form.validate_on_submit():
    	username = request.form['username']
    	password = request.form['password']
    	user = User.get_by_username(username)
    	if user is not None:
    		if user.password == password:
    			login_user(user)
    			return redirect(request.args.get("next") or url_for('index'))
    	else: 
    		flash('Incorrect Username/Password Combination')
    return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
	return User.get(int(user_id))




	
	
