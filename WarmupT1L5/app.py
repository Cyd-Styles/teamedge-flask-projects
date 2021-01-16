from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cydney')
def about():
    name = 'Cydney'
    description = 'This is my website!'
    friends = ['Arianna', 'Khia', 'Xiovalis', 'Brianna']
    return render_template('index.html', greeting=name, description=description)<h1>About</h1><p>Some other content</p>'





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

