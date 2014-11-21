from flask import render_template, url_for, redirect, request
from forms import CommentForm
from hello import app, db
from models import Profile
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
