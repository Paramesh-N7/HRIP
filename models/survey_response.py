from extensions import db
from datetime import datetime

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=False)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
