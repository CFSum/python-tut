from flask import Flask, request, flash, url_for, redirect, render_template
from database import db_session
from models import User
app = Flask(__name__)
app.config['SECRET_KEY'] = "macam yes"


@app.route('/')
def get_all_users():

    all_users = User.query.all()

    context = {
    'all_users': all_users,
    }
    return render_template('all_users.html', context = context)


@app.route('/user/<name>')
def show_user(name):

    user = User.query.filter(User.name == name).first()

    context = {
    'user': user,
    }
    return render_template('show_user.html', context = context)

@app.route('/user/<name>/<comments>')
def write_comment(name, comments):

    user

    context = {
    'user': user,
    }

    return render_template('comment.html', context = context)
    pass

@app.route('/try', methods = ['GET', 'POST'])
def write_user():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['password'] or not request.form['comments']:
            flash('Please enter all the fields', 'error')
        else:
            new_user = User(request.form['name'], request.form['email'],request.form['password'], request.form['comments'])

            db_session.add(new_user)
            db_session.commit()

            context = {
                'new_user': new_user,
            }

            flash('Recorded')
    return redirect(url_for('form.html' ))


@app.route('/new-user/<name>/<email>/<password>/<comments>')
def create_user(name, email, password, comments):
    new_user = User(name, email, password, comments)
    db_session.add(new_user)
    db_session.commit()

    context = {
        'new_user': new_user,
    }

    return render_template('new_user_created.html', context = context)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
