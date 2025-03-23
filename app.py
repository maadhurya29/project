from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['MovieAnalytics']
collection = db['MoviesData']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    genre = request.form.get('Genre')
    # Query MongoDB for movies/series with the given genre
    results = collection.find({'Genre': genre})

    # Convert MongoDB cursor to a list for easier JSON serialization
    results_list = list(results)
    return jsonify(results_list)

if __name__ == '__main__':
    app.run(debug=True)
