from sqlalchemy import func

@psych_bp.route("/results/<int:employee_id>")
@login_required
def results(employee_id):
    if current_user.role == "Employee":
        abort(403)

    results = (
        db.session.query(
            PsychometricQuestion.trait,
            func.avg(PsychometricResponse.rating)
        )
        .join(PsychometricResponse,
              PsychometricQuestion.id == PsychometricResponse.question_id)
        .filter(PsychometricResponse.employee_id == employee_id)
        .group_by(PsychometricQuestion.trait)
        .all()
    )

    return render_template(
        "psychometric/results.html",
        results=results
    )
