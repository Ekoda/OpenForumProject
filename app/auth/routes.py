from flask import render_template, redirect, url_for, request
from flask_login import logout_user, current_user
from app import db
from app.auth import bp
from app.models import User

@bp.route('/signup', methods=['GET'])
def signup():
    return render_template('auth/signup.html', title='Sign up')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Route for initial forgot password page
@bp.route('/resetpassword', methods=['GET'])
def resetpassword():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template('auth/resetpassword.html', title='Request Reset Password')

# Route from reset password email token
@bp.route('/create_password/<token>', methods=['GET'])
def create_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    return render_template('auth/create_password.html', title='Create Password')
