from flask import Flask, render_template, request, redirect, url_for, current_app as app
from sense_emu import SenseHat
from time import sleep
from flask_apscheduler import APScheduler
import sqlite3

sense = SenseHat

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def entertasks():
    return render_template('tasks.html')

@app.route('/submitted-tasks', methods=['POST'])
def store_tasks():
    #get posted form data using names assigned in HTML
    subject = request.form['task-type']
    name = request.form['task-name']
    deadline = request.form['task-due-date']
    #connect to database and insert subject, name, and deadline
    conn = sqlite3.connect('./static/data/tasks-app.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks (subjects, tasknames, deadlines) VALUES((?), (?), (?))", (subject, name, deadline))
    conn.commit()
    #close database connection
    conn.close()
    #render template with success message
    return render_template('store_tasks.html', subjects = subject, tasknames = name, deadlines = deadline)

@app.route('/all-tasks')
def all():
    #connect to DB
    conn = sqlite3.connect('./static/data/tasks-app.db')
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * from tasks")
    for row in rows:
        task = {'subject': row[0], 'names':row[1], 'deadlines':row[2]}
        tasks.append(task)
    conn.close()
    return render_template('all_tasks.html', tasks = tasks)



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')