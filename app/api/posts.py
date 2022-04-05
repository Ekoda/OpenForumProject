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


# Example structure of get_posts
thread_data = {
    'posts': [
        {
            'id': 'id_1',
            'thread': 'thread_1', # This will be the hash of the website link
            'body': 'body_1',
            'timestamp': 'timestamp_1',
            'score': 'score_1',
            'user_id': 'user_id_1',
            'user_color': 'user_color_1',
            'responses': [{
                'response_id': 'response_id_1',
                'user_id': 'user_id_response',
                'user_color': 'user_color_response',
                'body': 'response_body_1',
                'score': 'response_score_1',
                'timestamp': 'response_timestamp_1'
            }]}
        ]}
        