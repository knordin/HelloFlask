from hello import db
from flask.ext.login import LoginManager, UserMixin, login_required
from sqlalchemy import CheckConstraint


class UserProfile(db.Model):
    comment_id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True)
    doc = db.Column(db.Text, nullable=True)
    __table_args__ =(CheckConstraint('DOC IS JSON', name='ensure_json'), {})
    def __init__(self, text):
        self.doc = text

class User(db.Model):
    user_id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    
    def __init__(self, username, password):
	self.id = username
	self.password = password
   
    @classmethod
    def get(cls, id):
        return User.query.filter_by(username=id).first()


