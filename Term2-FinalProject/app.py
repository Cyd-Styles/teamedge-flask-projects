from flask import Flask, render_template, request, redirect, url_for, current_app as app
from sense_emu import SenseHat
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
      return render_template('name.html', name = user)

@app.route('/message',methods = ['POST', 'GET'])
def message():
    if request.method == 'POST':
        message = request.args.get('msg')
        return render_template("message_page.html", name = message)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')