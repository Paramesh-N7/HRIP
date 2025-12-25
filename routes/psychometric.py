from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from extensions import db
from models.psychometric_question import PsychometricQuestion
from models.psychometric_response import PsychometricResponse

psych_bp = Blueprint("psychometric", __name__, url_prefix="/psychometric")


@psych_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_questions():
    if current_user.role not in ["Admin", "HR"]:
        abort(403)

    if request.method == "POST":
        q = PsychometricQuestion(
            question=request.form["question"],
            trait=request.form["trait"]
        )
        db.session.add(q)
        db.session.commit()
        return redirect(url_for("psychometric.create_questions"))

    return render_template("psychometric/create.html")


@psych_bp.route("/take/<int:employee_id>", methods=["GET", "POST"])
@login_required
def take_test(employee_id):
    if current_user.role == "Employee" and current_user.employee_id != employee_id:
        abort(403)

    questions = PsychometricQuestion.query.all()

    if request.method == "POST":
        for q in questions:
            rating = request.form.get(str(q.id))
            response = PsychometricResponse(
                employee_id=employee_id,
                question_id=q.id,
                rating=int(rating)
            )
            db.session.add(response)

        db.session.commit()
        return redirect(url_for("psychometric.thank_you"))

    return render_template("psychometric/take.html", questions=questions)


@psych_bp.route("/thank-you")
@login_required
def thank_you():
    return render_template("psychometric/thank_you.html")
