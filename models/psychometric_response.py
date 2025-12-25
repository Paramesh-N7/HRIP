from extensions import db
from datetime import datetime

class PsychometricResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("psychometric_question.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1–5
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
