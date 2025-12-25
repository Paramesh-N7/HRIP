import pandas as pd
from extensions import db
from sqlalchemy import text

def load_dataframe(query, columns):
    return pd.DataFrame(query, columns=columns)


def engagement_by_employee():
    query = db.session.execute(
        text("""
            SELECT e.name, AVG(sr.rating) AS engagement_score
            FROM employee e
            JOIN survey_response sr ON e.id = sr.employee_id
            GROUP BY e.name
        """)
    ).fetchall()

    return load_dataframe(query, ["Employee", "Engagement Score"])


def engagement_by_department():
    query = db.session.execute(
        text("""
            SELECT e.department, AVG(sr.rating) AS engagement_score
            FROM employee e
            JOIN survey_response sr ON e.id = sr.employee_id
            GROUP BY e.department
        """)
    ).fetchall()

    return load_dataframe(query, ["Department", "Engagement Score"])


def engagement_by_category():
    query = db.session.execute(
        text("""
            SELECT s.category, AVG(sr.rating) AS engagement_score
            FROM survey s
            JOIN survey_response sr ON s.id = sr.survey_id
            GROUP BY s.category
        """)
    ).fetchall()

    return load_dataframe(query, ["Category", "Engagement Score"])

def combined_insights():
    query = db.session.execute(text("""
        SELECT 
            e.name,
            AVG(sr.rating) AS engagement,
            AVG(CASE WHEN pq.trait = 'C' THEN pr.rating END) AS conscientiousness,
            AVG(CASE WHEN pq.trait = 'E' THEN pr.rating END) AS extraversion
        FROM employee e
        LEFT JOIN survey_response sr ON e.id = sr.employee_id
        LEFT JOIN psychometric_response pr ON e.id = pr.employee_id
        LEFT JOIN psychometric_question pq ON pq.id = pr.question_id
        GROUP BY e.name
    """)).fetchall()

    return pd.DataFrame(
        query,
        columns=[
            "Employee",
            "Engagement",
            "Conscientiousness",
            "Extraversion"
        ]
    )
