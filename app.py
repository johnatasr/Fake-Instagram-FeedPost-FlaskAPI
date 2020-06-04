import argparse
import os
from flask import Flask, jsonify, make_response
from flask_restful import Api
from resources.post import PostsList, Post
from flask_cors import CORS, cross_origin
from db.database import create_database


app = Flask(__name__)
api = Api(app)
app.secret_key = 'test_app134679124578235689'

api.add_resource(Post, '/posts/<int:post_id>')
api.add_resource(PostsList, '/posts')


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


@app.route("/")
def index():
    return "API Working"


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="Api FakePost Insta")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        create_database('./db/data.db')
        CORS = CORS(app)
        app.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        # create_database('./db/data.db')
        app.run(host='0.0.0.0', port=PORT, debug=False)
