from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect('database/data.db')
    return conn

def create_table():
    conn = create_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS audit_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        auditor_name TEXT,
        audit_name TEXT,
        ce_rating TEXT,
        mca_rating TEXT,
        total_issue_classification_score INTEGER,
        area_impact_score REAL,
        key_control_failure_score REAL,
        num_issues INTEGER,
        percentage_self_identified REAL,
        total_action_plan_score INTEGER,
        management_support_score INTEGER
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        auditor_name = request.form['auditor_name']
        audit_name = request.form['audit_name']
        ce_rating = request.form['ce_rating']
        mca_rating = request.form['mca_rating']
        total_issue_classification_score = request.form['total_issue_classification_score']
        area_impact_score = request.form['area_impact_score']
        key_control_failure_score = request.form['key_control_failure_score']
        num_issues = request.form['num_issues']
        percentage_self_identified = request.form['percentage_self_identified']
        total_action_plan_score = request.form['total_action_plan_score']
        management_support_score = request.form['management_support_score']

        conn = create_connection()
        conn.execute('''
        INSERT INTO audit_data (auditor_name, audit_name, ce_rating, mca_rating, total_issue_classification_score,
                                area_impact_score, key_control_failure_score, num_issues, percentage_self_identified,
                                total_action_plan_score, management_support_score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (auditor_name, audit_name, ce_rating, mca_rating, total_issue_classification_score,
              area_impact_score, key_control_failure_score, num_issues, percentage_self_identified,
              total_action_plan_score, management_support_score))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
