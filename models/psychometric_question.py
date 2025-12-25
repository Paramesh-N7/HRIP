from extensions import db

class PsychometricQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    trait = db.Column(db.String(1), nullable=False)  # O, C, E, A, N
