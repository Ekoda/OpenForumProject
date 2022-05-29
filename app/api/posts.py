from app import db
from app.api import bp
from flask import jsonify, request, url_for
from app.models import Post, PostResponse
from app.api.errors import bad_request, request_not_found

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
def get_post_response(id):
    return jsonify(PostResponse.query.get_or_404(id).to_dict())


@bp.route('/posts/<int:id>/responses', methods=['GET'])
def get_response_to_post(id):
    data = {
        'responses': Post.query.get(id).responses_to_dict()
    }
    if len(data['responses']) > 0:
        return jsonify(data)
    return request_not_found('No response data to thread id: ' + str(id))


@bp.route('/posts', methods=['POST'])
def post():
    data = request.get_json() or {}
    if 'thread' not in data or 'body' not in data or 'user_id' not in data:
        return bad_request('Must include thread, body, and user ID')
    post = Post()
    post.from_dict(data)
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response


@bp.route('/posts/responses', methods=['POST'])
def postresponse():
    pass


@bp.route('/posts/vote', methods=['PUT'])
def vote():
    pass