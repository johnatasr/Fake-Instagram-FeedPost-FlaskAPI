from models.post import PostModel
from flask_restful import Resource
from flask.json import jsonify


class Post(Resource):

    def get(self, post_id):
        post_obejct = PostModel.find_post(post_id)
        if post_obejct:
            post = [p.json() for p in post_obejct]
            response = jsonify({'post': post})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            return {'message': 'No post found!'}, 404


class PostsList(Resource):

    def get(self):
        posts_obj = PostModel.find_all_posts()
        if posts_obj:
            posts = [post.json() for post in posts_obj]
            response = jsonify({'post': posts})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            return {'message': 'No posts found!'}, 404

