from hello import db
from flask.ext.login import LoginManager, UserMixin, login_required

class Profile(db.Model):
    comment_id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True)
    text = db.Column(db.Text, nullable=False)
    def __init__(self, text):
        self.text = text

class User(UserMixin):
    user_database = {"JohnDoe": ("JohnDoe", "John"), "JaneDoe": ("JaneDoes", "Jane")}
    
    def __init__(self, username, password):
	self.id = username
	self.password = password
   
    @classmethod
    def get(cls, id):
	return cls.user_database.get(id)
