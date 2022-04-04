#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post, PostResponse, UserNotifications
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_password_hashing(self):
        u = User(username='kappa')
        u.set_password('lynx')
        self.assertFalse(u.check_password('airplane'))
        self.assertTrue(u.check_password('lynx'))

if __name__ == '__main__':
    unittest.main(verbosity=2)