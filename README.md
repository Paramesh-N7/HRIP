HR Analytics & Psychometric Assessment Platform
A full-stack HR Intelligence Platform built using Flask, PostgreSQL, SQLAlchemy, Pandas, and Chart.js that enables organizations to manage employees, conduct engagement surveys, run psychometric assessments, and derive actionable HR insights through analytics dashboards.
 
Features
Authentication & Roles
•	Secure login system using Flask-Login
•	Role-based access: Admin, HR, Employee
•	User–Employee mapping with access control

Employee Management
•	Admin-only CRUD operations for employees
•	Automatic employee login provisioning
•	Secure role enforcement

Engagement Surveys
•	Admin/HR-created survey questions
•	Employees can submit responses securely
•	Category-based engagement analysis

Psychometric Assessment (OCEAN Model)
•	Personality assessment based on Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
•	Automated trait scoring
•	Radar chart visualization

HR Analytics (Pandas-Powered)
•	Employee-level engagement scores
•	Department & category-wise analysis
•	Combined engagement + personality insights

Dashboards & Visualizations
•	Interactive charts using Chart.js
•	Role-specific dashboards
•	Clean, HR-friendly UI

Reporting
•	Export engagement reports as CSV
•	Downloadable PDF reports for leadership & compliance
 
Layer	Technology
Backend	Flask, Flask-Login, Flask-Migrate
Database	PostgreSQL
ORM	SQLAlchemy
Analytics	Pandas
Visualization	Chart.js
Auth	Role-based access control
Deployment	Gunicorn, Render

 
Project Structure
hr_platform/
├── analytics/
│   └── hr_reports.py
├── models/
├── routes/
├── templates/
├── utils/
├── migrations/
├── app.py
├── config.py
└── requirements.txt
 
Setup (Local)
git clone <repo-url>
cd hr_platform
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask db upgrade
python app.py
Visit: http://127.0.0.1:5000
 
Use Cases
•	Employee engagement analysis
•	L&D insights
•	Leadership potential identification
•	Burnout risk detection
•	HR analytics & reporting
 
License
MIT License
