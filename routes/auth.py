from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from models.user import User
from extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        user = User(email=email, role=role)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            from utils.redirects import redirect_after_login
            return redirect_after_login()


        return "Invalid credentials"

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
