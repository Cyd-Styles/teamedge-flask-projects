from flask import Flask, request, json, jsonify, render_template, current_app as app
import os

app = Flask(__name__, static_folder="static")

movies_data = os.path.join(app.static_folder, 'data', 'movies.json')
movie_titles = os.path.join(app.static_folder, 'data', 'movies.json', 'title')
#movies_years = os.path.join(app.static_folder, 'data', 'movies.json', 'year')
events_data = os.path.join(app.static_folder, 'data', 'events.json')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>I shall remain a secret...</p>'

@app.route('/display_movies')
def display_movies():

    greeting="Check Out These Cool Movies!!!"
    results = []
    with open(movies_data, 'r') as jsondata:
        movie_titles = json.load(jsondata)
    return render_template('display_movies.html', greeting=greeting, movie_titles=movie_titles)

@app.route('/api/v1/movies', methods=['GET'])
def api_movies_all():
    #using with allows for opening and closing of the file
    with open(movies_data, 'r') as jsondata:
        movies = json.load(jsondata)
        #no need to return an HTML template
        return jsonify(movies)

# Why can't I use the second API with a different app.route?

@app.route('/api/v1/events', methods=['GET'])
def api_events_all():
     #using with allows for opening and closing of the file
     with open(events_data, 'r') as jsondata:
         events = json.load(jsondata)
         #no need to return an HTML template
         return jsonify(events)

@app.route('/api/v1/movies/search', methods=['GET'])
def api_search():

# How do I query search using titles and cast names?
    results=[] #a list to hold our results

    with open(movies_data, 'r') as jsondata:
        movies = json.load(jsondata)

     #request.args returns a dictionary of all query terms in the URL
    if 'cast' in request.args:
        cast = request.args['cast'] 

        #Loop through all the movies in our JSON list.
        for movie in movies:
            #if the cast query matches, then add them to the results
            if cast in movie['cast']:
                results.append(movie)
# Why is it that when I try using the query for searching genres it doesn't register
    if 'genres' in request.args:
        genres = request.args['genres'] 

        #Loop through all the movies in our JSON list.
        for movie in movies:
            #if the genres query matches, then add them to the results
            if genres in movie['genres']:
                results.append(movie)
   
    if 'year' in request.args:
        year = request.args['year']

        for movie in movies:
            #the year is a integer, so we convert to a string    
            if (year == str(movie['year'])):
                results.append(movie)

    if 'title' in request.args:
        #introduce lower() to make sure we ignore case in the search
        title_search = request.args['title'].lower()
         
        for movie in movies:
            for s in movie["title"]:

                if title_search in s.lower():
                    print("we found a match!!")
                    results.append(movie)    
    #introduce a way to check if the results are empty and inform the user.
    if (len(results) < 1):
        return "Sorry, your query did not find any matches."
    else:
        return (jsonify(results))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

