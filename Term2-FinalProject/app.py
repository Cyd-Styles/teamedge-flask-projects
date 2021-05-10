from flask import Flask, render_template, request, redirect, url_for, current_app as app
from sense_emu import SenseHat
from time import sleep
import sqlite3

sense = SenseHat()

y = (255, 255, 0) # YELLOW color
o = (255, 128, 0) # ORANGE color
w = (255, 255, 255) # WHITE color
r = (255, 0, 0 ) # RED color
c = (139, 69, 19) # BROWN / CAFE color

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/name',methods = ['POST', 'GET'])
def name():
   if request.method == 'POST':
       user = request.form['nm']
       conn = sqlite3.connect('./static/data/storednames.db')
       curs = conn.cursor()
       curs.execute("INSERT INTO name (name) VALUES((?))",(name,))
       conn.commit()

       conn.close()
       return render_template('name.html', name = name)

#        print(user)
#        sense.show_message(user)
#        return render_template('name.html', name = user)
#    else:
#       user = request.args.get('nm')
#       return render_template('name.html', name = user)

@app.route('/message',methods = ['POST', 'GET'])
def message():
    if request.method == 'POST':
        message = request.form['msg']
        conn = sqlite3.connect('./static/data/storedmessages.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO message (message) VALUES((?))",(message,))
        conn.commit()

        conn.close()
        return render_template('message_page.html', message = message)

    #     print(message)
    #     sense.show_message(message)
    # return render_template("message_page.html", message = message)

# @app.route('/drawing', methods = ['POST', 'GET'])
# def drawing():
#     if request.method == 'POST':
#         drawing = request.form['draw']
#         sense.set_pixels(heart)
#     return render_template*("drawing.html", drawing = heart)


# # connects database and inserts the name and message
# conn = sqlite3.connect('./static/data/Term2-FinalProject.db')
# curs = conn.cursor()
# curs.execute("INSERT INTO messages VALUES((?))", (name, message))
# conn.commit()

# # close database connection
# conn.close()

@app.route('/allnames')
def allnames():
    # connect to db
    conn = sqlite3.connect('./static/data/collectednames.db')
    curs = conn.cursor()
    names = []
    rows = curs.execute("SELECT * from names")
    for row in rows:
        name = {'name': row[0]}
        names.append(name)
    conn.close()
    return render_template('allnames.html', names = names)

@app.route('/allmessages')
def allmessages():
    # connect to db
    conn = sqlite3.connect('./static/data/collectedmessages.db')
    curs = conn.cursor()
    message = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'message': row[0]}
        messages.append(message)
    conn.close()
    return render_template('allmessages.html', messages = messages)


heart = [
w, r, r, w, w, r, r, w,
r, o, o, r, r, o, o, r,
r, o, y, o, o, y, o, r,
r, o, y, y, y, y, o, r,
w, r, o, y, y, o, r, w,
w, r, o, y, y, o, r, w,
w, w, r, o, o, r, w, w,
w, w, w, r, r, w, w, w
]

# mario = [
#     w, w, r, r, r, r, w, w,
#     w, r, r, r, r, r, r, w,
#     w, c, c, y, y, k, w, w, 
#     c, y, c, 

# ]
sense.set_pixels(heart)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')