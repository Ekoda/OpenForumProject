from app import db
from app.api import bp
from flask import jsonify, request
from app.models import User, Post, PostResponse
from app.api.errors import bad_request

@bp.route('/posts/<thread_hash>', methods=['GET'])
def get_posts(thread_hash):
    data = {
        'posts': [post.to_dict() for post in Post.query.filter_by(thread=thread_hash).all()]
    }
    return jsonify(data)

@bp.route('/post', methods=['POST'])
def post(data):
    pass

@bp.route('/postresponse', methods=['POST'])
def postresponse(data):
    pass

@bp.route('/vote', methods=['PUT'])
def vote(vote):
    pass