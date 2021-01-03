# server.py

# Imports
import pymongo
import datetime
from flask import Flask, jsonify, abort

# Constants
app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb://localhost:27017"
)
DB = client['menahem']


@app.route('/<page>')
def test(page):
    collection = DB.get_collection(page)
    if not collection:
        abort(404)
    data = list(collection.find({}, {'_id': False}))
    return jsonify({'time': datetime.datetime.now().strftime('%H:%M:%S'), 'data': data})


if __name__ == '__main__':
    app.run(port=8000)

