from extensions import db

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100))
