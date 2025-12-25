from flask import redirect, url_for
from flask_login import current_user

def redirect_after_login():
    if current_user.role in ["Admin", "HR"]:
        return redirect(url_for("employee.list_employees"))

    if current_user.role == "Employee":
        return redirect(
            url_for("survey.take_survey", employee_id=current_user.employee_id)
        )

    return redirect(url_for("auth.login"))
