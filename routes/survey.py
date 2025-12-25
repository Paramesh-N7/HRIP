from flask import Blueprint, abort, render_template, request, redirect, url_for
from flask_login import login_required
from extensions import db
from models.survey import Survey
from models.survey_response import SurveyResponse
from models.employee import Employee
from sqlalchemy import func
from flask_login import current_user

survey_bp = Blueprint("survey", __name__, url_prefix="/survey")

# -------------------------
# Admin: Create questions
# -------------------------
@survey_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_survey():
    if request.method == "POST":
        question = request.form["question"]
        category = request.form["category"]

        survey = Survey(question=question, category=category)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for("survey.list_survey"))

    return render_template("survey/create.html")


# -------------------------
# List survey questions
# -------------------------
@survey_bp.route("/")
@login_required
def list_survey():
    surveys = Survey.query.all()
    return render_template("survey/list.html", surveys=surveys)


# -------------------------
# Employee takes survey
# -------------------------

@survey_bp.route("/take/<int:employee_id>", methods=["GET", "POST"])
@login_required
def take_survey(employee_id):

    # Prevent employees from accessing others' surveys
    if current_user.role == "Employee" and current_user.employee_id != employee_id:
        abort(403)

    surveys = Survey.query.all()

    if request.method == "POST":
        for survey in surveys:
            rating = request.form.get(str(survey.id))
            response = SurveyResponse(
                employee_id=employee_id,
                survey_id=survey.id,
                rating=int(rating)
            )
            db.session.add(response)

        db.session.commit()
        return redirect(url_for("survey.results"))

    return render_template("survey/take.html", surveys=surveys)


# -------------------------
# View raw results
# -------------------------
@survey_bp.route("/results")
@login_required
def results():
    responses = SurveyResponse.query.all()
    return render_template("survey/results.html", responses=responses)


# ==============================
# ENGAGEMENT ANALYTICS ROUTES
# ==============================

@survey_bp.route("/engagement/employee")
@login_required
def employee_engagement():
    results = (
        db.session.query(
            Employee.name,
            func.avg(SurveyResponse.rating).label("score")
        )
        .join(SurveyResponse, Employee.id == SurveyResponse.employee_id)
        .group_by(Employee.name)
        .all()
    )
    return render_template("survey/employee_engagement.html", results=results)


@survey_bp.route("/engagement/department")
@login_required
def department_engagement():
    results = (
        db.session.query(
            Employee.department,
            func.avg(SurveyResponse.rating).label("score")
        )
        .join(SurveyResponse, Employee.id == SurveyResponse.employee_id)
        .group_by(Employee.department)
        .all()
    )
    return render_template("survey/department_engagement.html", results=results)


@survey_bp.route("/engagement/category")
@login_required
def category_engagement():
    results = (
        db.session.query(
            Survey.category,
            func.avg(SurveyResponse.rating).label("score")
        )
        .join(SurveyResponse, Survey.id == SurveyResponse.survey_id)
        .group_by(Survey.category)
        .all()
    )
    return render_template("survey/category_engagement.html", results=results)
