#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post, PostResponse, UserNotifications
from app.api import users, posts, errors
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class AutomatedTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.client = None
    
    def test_password_hashing(self):
        u = User(username='kappa')
        u.set_password('lynx')
        self.assertFalse(u.check_password('airplane'))
        self.assertTrue(u.check_password('lynx'))

    def test_get_user_api(self):
        user = User(username='kappa')
        db.session.add(user)
        db.session.commit()
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code,  200)
        self.assertEqual(response.json['username'], 'kappa')
        self.assertEqual(response.json['id'], 1)
    
    def test_get_posts_api(self):
        user = User(username='test_user')
        post = Post(thread='test_thread', body='test body', score=7, user_id=1)
        post_response = PostResponse(user_id=1, response_to_id=1, body='test response body', score=2)
        db.session.add(user); db.session.add(post); db.session.add(post_response)
        db.session.commit()
        response = self.client.get('api/posts/test_thread')
        self.assertEqual(response.status_code,  200)
        self.assertEqual(response.json['posts'][0]['thread'], 'test_thread')
        self.assertEqual(response.json['posts'][0]['color'], '#FFFFFF')
        self.assertEqual(response.json['posts'][0]['image'], 'images/default.jpg')
        self.assertEqual(response.json['posts'][0]['responses'][0]['body'], 'test response body')
        self.assertEqual(response.json['posts'][0]['responses'][0]['username'], 'test_user')



if __name__ == '__main__':
    unittest.main(verbosity=2)