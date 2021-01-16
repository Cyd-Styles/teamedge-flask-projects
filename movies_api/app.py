from flask import Flask, request, json, jsonify, render_template, current_app as app
import os

app = Flask(__name__, static_folder="static")

movies_data = os.path.join(app.static_folder, 'data', 'movies.json')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>Some other content</p>'

@app.route('/api/v1/movies', methods=['GET'])
def api_movies_all():
    #using with allows for opening and closing of the file
    with open(movies_data, 'r') as jsondata:
        movies = json.load(jsondata)
        #no need to return an HTML template
        return jsonify(movies)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

