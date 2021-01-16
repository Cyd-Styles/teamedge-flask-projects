from flask import flask, render_template, request, json, jsonify, current_app as app 
from datetime import date
import os
import requests


app = Flask(__name__)
json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path, 'r') as raw_json:
    json_info = json.load(raw_json)


@app.route('/')
def about():
    return '<p>Flask Server is Running</p>'

@app.route('/nasa')
def nasa_image():
    today = str(data.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=0hnWqUOzCWnNqLNddglJPGiG56sTs0PXg2hPY7MV&date=' + today)

    data = response.json()

    return render_template('nasa.html', data=data)



    if __name__ == '_main__':
        app.run(debug = True, host = '127.0.0.1')