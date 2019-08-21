from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'admin'}

    users = [
        {
            'username': 'admin',
            'first_name': 'Admin',
            'last_name': 'Adminsky'
        },
        {
            'username': 'algol',
            'first_name': 'Alexander',
            'last_name': 'Golovnya'
        },
        {
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'Testov'
        },

    ]

    return render_template('index.html', title='Home', user=user, users=users)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
