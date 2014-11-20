from flask import render_template, url_for, redirect, request
from forms import CommentForm
from hello import app, db
from models import Profile
import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
   # request.values is where the json for you to access
   # print dir(request)
   # print request.values 

    form = CommentForm()
    if form.validate_on_submit():
        comment = Profile(
            form.text.data
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('index'))
    comments = Profile.query.order_by(db.desc(Profile.comment_id))
    return render_template('index.html', comments=comments, form=form)
