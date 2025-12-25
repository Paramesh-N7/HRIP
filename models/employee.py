from extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100))
    role = db.Column(db.String(100))
    salary = db.Column(db.Float)

    # Relationship (not required but useful)
    user = db.relationship("User", backref="employee", uselist=False)
