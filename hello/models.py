from hello import db

class Profile(db.Model):
    comment_id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True)
    text = db.Column(db.Text, nullable=False)
    def __init__(self, text):
        self.text = text

