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


# Home Page w/ Form
@app.route('/')
def add_tasks():
    return render_template('form.html')

# Task Display Page
@app.route('/tasks', methods=['POST', 'GET'])
def view_tasks():
    if request.method == 'POST':
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
        #connect to DB
        conn = sqlite3.connect('./static/data/tasks-app.db')
        curs = conn.cursor()
        tasks = []
        rows = curs.execute("SELECT * FROM tasks ORDER BY deadlines DESC;")
        for row in rows:
            task = {'rowid': row[0], 'subject': row[1], 'names':row[2], 'deadlines':row[3]}
            tasks.append(task)
            print(task)
        conn.close()
        # render template with success message
        return render_template('all_tasks.html', tasks = tasks)



@app.route('/tasks/delete/<id>')
def delete(id):
    conn = sqlite3.connect('./static/data/tasks-app.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM tasks WHERE rowid = VALUES(?)", (id,))
    conn.commit()
    #close database connection
    conn.close()
    #connect to DB
    conn = sqlite3.connect('./static/data/tasks-app.db')
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * FROM tasks WHERE rowid = (?)", (id, ))
    for row in rows:
        task = {'rowid': row[0], 'subject': row[1], 'names':row[2], 'deadlines':row[3]}
        tasks.append(task)
        print(task)
    conn.close()
    return render_template('all_tasks.html', tasks = tasks)

@app.route('/tasks/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    # conn = sqlite3.connect('./static/data/tasks-app.db')
    # curs = conn.cursor()
    # #curs.execute("UPDATE FROM tasks SET subjects = subject, tasknames = names, deadlines = deadlines WHERE rowid = VALUES(?)", (id, ))
    # conn.commit()
    #close database connection
    #conn.close()
    #connect to DB
    conn = sqlite3.connect('./static/data/tasks-app.db')
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * FROM tasks WHERE rowid = (?)", (id, ))
    for row in rows:
        task = {'rowid': row[0], 'subject': row[1], 'names':row[2], 'deadlines':row[3]}
        tasks.append(task)
        print(task)
    conn.close()
    return render_template('edit_tasks.html', tasks = tasks)


# @app.route('/deleteTask/<btn>')
# def delete(btn):
#     print('button ' + str(btn) + ' was pressed')
#     return render_template('all_tasks.html')





        
        





if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')