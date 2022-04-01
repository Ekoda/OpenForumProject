from app import app, db
from app.models import PostResponse, User, Post, UserNotifications

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'PostResponse': PostResponse, 'UserNotification': UserNotifications}