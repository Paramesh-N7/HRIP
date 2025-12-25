from flask import Flask, render_template
from config import Config
from extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # -------- Landing Page --------
    from flask_login import current_user
    from utils.redirects import redirect_after_login

    @app.route("/")
    def home():
        if current_user.is_authenticated:
            return redirect_after_login()
        return render_template("home.html")

    # -------- Blueprints --------
    from routes.auth import auth_bp
    from routes.employee import employee_bp
    from routes.survey import survey_bp
    from routes.reports import reports_bp
    from routes.psychometric import psych_bp
    
    app.register_blueprint(psych_bp)  
    app.register_blueprint(reports_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(survey_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
