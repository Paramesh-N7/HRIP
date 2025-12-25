from flask import Blueprint, render_template, send_file
from flask_login import login_required
from analytics.hr_reports import (
    engagement_by_employee,
    engagement_by_department,
    engagement_by_category
)

reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


@reports_bp.route("/")
@login_required
def dashboard():
    emp_df = engagement_by_employee()
    dept_df = engagement_by_department()
    cat_df = engagement_by_category()

    return render_template(
        "reports/dashboard.html",
        emp_table=emp_df.to_html(index=False),
        dept_table=dept_df.to_html(index=False),
        cat_table=cat_df.to_html(index=False),
        dept_df=dept_df
    )


@reports_bp.route("/export/engagement")
@login_required
def export_engagement():
    df = engagement_by_employee()
    file_path = "employee_engagement_report.csv"
    df.to_csv(file_path, index=False)
    return send_file(file_path, as_attachment=True)

from analytics.hr_reports import combined_insights
@reports_bp.route("/combined")
@login_required
def combined_report():
    df = combined_insights()
    return render_template(
        "reports/combined.html",
        table=df.to_html(index=False)
    )
