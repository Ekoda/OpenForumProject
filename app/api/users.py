from app import app, db
from flask import jsonify, request
from app.models import User
from app.api.errors import bad_request
from app.email import send_password_reset_email

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    data = User.query.get_or_404(id).to_dict()
    return jsonify(data)
    
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    return response

@app.route('/api/resetpassword', methods=['POST'])
def api_reset_password():
    data = request.get_json() or {}
    if 'email' not in data:
        return bad_request('must include email')
    if not User.query.filter_by(email=data['email']).first():
        return bad_request('there is no Open Forum account with that email adress')
    user = User.query.filter_by(email=data['email']).first()
    send_password_reset_email(user)
    response = jsonify('Successfully reset password, check email for instructions')
    response.status_code = 201
    return response

@app.route('/api/create_password', methods=['POST'])
def create_a_new_password():
    data = request.get_json() or {}
    if 'token' not in data:
        return bad_request('must include token')
    if 'password' not in data:
        return bad_request('must include password')
    user = User.verify_reset_password_token(data['token'])
    if not user:
        return bad_request('invalid token')
    user.user.set_password(data['password'])
    db.session.commit()
    response = jsonify('Successfully changed password')
    response.status_code = 201
    return response