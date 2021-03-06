from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/rainbow')
def rainbow_links():
    link = 'http://0.0.0.0:5000/'
    color_link = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('rainbow.html', link = link, color_link = color_link)
@app.route('/red')
def red():
    color = 'Red'
    return render_template('index.html', color = color)

@app.route('/orange')
def orange():
    color = 'Orange'
    return render_template('index.html', color = color)

@app.route('/yellow')
def yellow():
    color = 'Yellow'
    return render_template('index.html', color = color)

@app.route('/green')
def green():
    color = 'Green'
    return render_template('index.html', color = color)

@app.route('/blue')
def blue():
    color = 'Blue'
    return render_template('index.html', color = color)

@app.route('/indigo')
def indigo():
    color = 'Indigo'
    return render_template('index.html', color = color)

@app.route('/violet')
def violet():
    color = 'Violet'
    return render_template('index.html', color = color)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')