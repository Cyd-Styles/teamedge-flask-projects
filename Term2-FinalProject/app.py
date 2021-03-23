from flask import Flask, render_template, request, redirect, url_for, current_app as app
from sense_emu import SenseHat
from time import sleep

sense = SenseHat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/name',methods = ['POST', 'GET'])
def name():
   if request.method == 'POST':
      user = request.form['nm']
      return render_template('name.html', name = user)
   else:
      user = request.args.get('nm')
      sense.show_message(name)
      return render_template('name.html', name = user)

@app.route('/message',methods = ['POST', 'GET'])
def message():
    if request.method == 'POST':
        message = request.form['msg']
        print(message)
    sense.show_message(message)
    return render_template("message_page.html", message = message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')