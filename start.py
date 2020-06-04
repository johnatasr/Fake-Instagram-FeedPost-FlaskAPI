from flask import Flask
from flask_restful import Api
from resources.post import PostsList, Post
from flask_cors import CORS, cross_origin
from db.database import create_database


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    app.secret_key = 'test_app134679124578235689'

    api.add_resource(Post, '/posts/<int:post_id>')
    api.add_resource(PostsList, '/posts')

    @app.route("/")
    def index():
        return "API Working"

    create_database()

    return app