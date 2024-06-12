from flask import *
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from .helpers import *

auth = Blueprint('auth',__name__)


@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            session['username'] = user.username
            return redirect('/')
        error_message = 'Invalid email or password'
        return render_template('login.html', error_message=error_message)
    return render_template('login.html')


@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        # Check if email is valid
        if not is_valid_email(email):
            error_message = 'Invalid email format'
            return render_template('signup.html', error_message=error_message)

        # Validate password complexity
        if not is_valid_password(password):
            error_message = f'Password must be at least {MIN_PASSWORD_LENGTH} characters long with at least ' \
                            f'{MIN_LOWERCASE_CHARS} lowercase characters and include at least {MIN_SPECIAL_CHARS}' \
                            f' special character'
            return render_template('signup.html', error_message=error_message)

        # Check if passwords match
        if not passwords_match(password, confirm_password):
            error_message = 'Passwords do not match'
            return render_template('signup.html', error_message=error_message)

        # Check if email already exists in the database
        existing_user = get_user_by_email(email)
        if existing_user:
            error_message = 'Email already exists'
            return render_template('signup.html', error_message=error_message)

        # If email is valid and not already in use, proceed with user creation
        new_user = create_user(username, email, password)
        login_user(new_user)
        session['username'] = username
        return render_template('login.html')
    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect('/')


