from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from extensions import db
from models.employee import Employee
from utils.permissions import admin_required
from models.user import User

employee_bp = Blueprint("employee", __name__, url_prefix="/employees")

@employee_bp.route("/")
@login_required
def list_employees():
    employees = Employee.query.all()
    return render_template("employee/list.html", employees=employees)

@employee_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_employee():
    if request.method == "POST":
        emp = Employee(
            name=request.form["name"],
            email=request.form["email"],
            department=request.form["department"],
            role=request.form["role"],
            salary=float(request.form["salary"])
        )
        db.session.add(emp)
        db.session.flush()  # get emp.id before commit

        # Create employee login
        user = User(
            email=emp.email,
            role="Employee",
            employee_id=emp.id
        )
        user.set_password(request.form["password"])

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("employee.list_employees"))

    return render_template("employee/add.html")

@employee_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_employee(id):
    emp = Employee.query.get_or_404(id)

    if request.method == "POST":
        emp.name = request.form["name"]
        emp.department = request.form["department"]
        emp.role = request.form["role"]
        emp.salary = float(request.form["salary"])

        db.session.commit()
        return redirect(url_for("employee.list_employees"))

    return render_template("employee/edit.html", employee=emp)

@employee_bp.route("/delete/<int:id>")
@login_required
@admin_required
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for("employee.list_employees"))
