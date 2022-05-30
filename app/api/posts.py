from app import db
from app.api import bp
from flask import jsonify, request, url_for, abort
from app.models import Post, PostResponse
from app.api.errors import bad_request, request_not_found
from app.api.auth import token_auth

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    return jsonify(Post.query.get_or_404(id).to_dict())


@bp.route('/posts/<thread_hash>', methods=['GET'])
def get_posts(thread_hash):
    data = {
        'posts': [post.to_dict() for post in Post.query.filter_by(thread=thread_hash).all()]
    }
    if len(data['posts']) > 0:
        return jsonify(data)
    return request_not_found('No post data on thread: ' + thread_hash)


@bp.route('/posts/responses/<int:id>', methods=['GET'])
def get_response(id):
    return jsonify(PostResponse.query.get_or_404(id).to_dict())


@bp.route('/posts/<int:id>/responses', methods=['GET'])
def get_response_to_post(id):
    data = {
        'responses': Post.query.get(id).responses_to_dict()
    }
    if len(data['responses']) > 0:
        return jsonify(data)
    return request_not_found('No response data found in relation to thread id: ' + str(id))


@bp.route('/post', methods=['POST'])
@token_auth.login_required
def post():
    data = request.get_json() or {}
    if 'thread' not in data or 'body' not in data:
        return bad_request('Must include thread, body')
    data['user_id'] = token_auth.current_user().id
    post = Post()
    post.from_dict(data)
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response


@bp.route('/posts/<int:id>/respond', methods=['POST'])
@token_auth.login_required
def respond_to(id):
    data = request.get_json() or {}
    if 'body' not in data:
        return bad_request('Must include the id of the post which is being responded to and body')
    data['response_to_id'] = id   
    data['user_id'] = token_auth.current_user().id
    post_response = PostResponse()
    post_response.from_dict(data)
    db.session.add(post_response)
    db.session.commit()
    response = jsonify(post_response.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_response_to_post', id=post_response.id)
    return response


@bp.route('/posts/vote', methods=['PUT'])
@token_auth.login_required
def vote():
    pass


@bp.route('/posts/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_post(id):
    pass


@bp.route('/posts/<int:id>/responses', methods=['DELETE'])
@token_auth.login_required
def delete_response(id):
    pass