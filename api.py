from flask import Flask, jsonify
from flask_restful import Api
from resources.post import PostsList, Post
from flask_cors import CORS, cross_origin
# from security import authenticate, identity
# from flask_jwt import JWT, jwt_required, JWTError


app = Flask(__name__)
CORS(app)
api = Api(app)
app.secret_key = 'test_app134679124578235689'

api.add_resource(Post, '/posts/<int:post_id>')
api.add_resource(PostsList, '/posts')

@app.route("/")
def index():
    return "API Working"

@app.route("/teste")
def testex():

    dicte = {
        "detail": "teste",
        "number": 2
    }

    return jsonify(dicte)

if __name__ == '__main__':
    # create_database('./db/data.db')
    app.run(host="0.0.0.0", port=5000, debug=True)