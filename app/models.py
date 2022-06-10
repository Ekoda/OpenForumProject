from app import db, login
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt
from time import time
from flask import current_app, url_for
import os
import base64

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    notifications = db.relationship('UserNotifications', backref='author', lazy='dynamic')
    post_responses = db.relationship('PostResponse', backref='author', lazy='dynamic')
    image = db.Column(db.String(64), default='static/images/default.jpg') # Link to user image
    color = db.Column(db.String(64), default='#FFFFFF') # User Hex color
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
            'id' : self.id,
            'username': self.username,
            'image': self.image,
            'color': self.color
        }
        if include_email:
            data['email'] = self.email

        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'color', 'image']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])
    
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def __repr__(self):
        return '<User{}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread = db.Column(db.String(127), index=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    score = db.Column(db.Integer, index=True, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    responses = db.relationship('PostResponse', backref='main', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'username': User.query.get(self.user_id).username,
            'color': User.query.get(self.user_id).color,
            'image': User.query.get(self.user_id).image,
            'thread': self.thread,
            'body': self.body,
            'score': self.score,
            'user_id': self.user_id,
            'timestamp': self.timestamp,
            'responses': [response.to_dict() for response in self.responses.all()],
            '_links': {
                'self': url_for('api.get_post', id=self.id),
                'responses': url_for('api.get_response_to_post', id=self.id),
                'thread': url_for('api.get_posts', thread_hash=self.thread),
                'respond_to': url_for('api.respond_to', id=self.id),
                'post_to_thread': url_for('api.post')
            }
        }
        return data
    
    def responses_to_dict(self):
        return [response.to_dict() for response in self.responses.all()]

    def from_dict(self, data):
        for field in ['thread', 'body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class PostResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_to_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    response_to_user_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.String(140))
    score = db.Column(db.Integer, index=True, default=0)

    def to_dict(self):
        parent_user_id = Post.query.get(self.response_to_id).user_id
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'username': User.query.get(self.user_id).username,
            'color': User.query.get(self.user_id).color,
            'image': User.query.get(self.user_id).image,
            'response_to_username': User.query.get(parent_user_id).username,
            'response_to_color': User.query.get(parent_user_id).color,
            'response_to_id': self.response_to_id,
            'timestamp': self.timestamp,
            'body': self.body,
            'score': self.score,
            '_links': {
                'self': url_for('api.get_response', id=self.id),
                'parent_post': url_for('api.get_post', id=self.response_to_id),
                'thread': url_for('api.get_posts', thread_hash=Post.query.get(self.response_to_id).thread),
                'respond_to': url_for('api.respond_to', id=Post.query.get(self.response_to_id).id)
            }
        }
        return data

    def from_dict(self, data):
        for field in ['response_to_id', 'body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Post Response {}>'.format(self.body)

class UserNotifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<User Notifications{}>'.format(self.body)
    
