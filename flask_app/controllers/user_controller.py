from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def display_login_registration():
    return render_template("index.html")


@app.route("/user/new", methods = ['POST'])
def create_user():
    data = {
        "email" : request.form['email']
    }

    result = User.get_one(data)
    if result == None:
        # Add the new user
        data = {
            "email" : request.form['email'],
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "password" : bcrypt.generate_password_hash(request.form['password'])
        }
        User.create(data)
        session['email'] = request.form['email']
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['user_id'] = user_id
        return redirect("/dashboard")
    else:
        # return an error message with flash
        pass


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/login", methods = ['POST'])
def login():
    data = {
        "email" : request.form['email']
    }

    result = User.get_one(data)

    if result == None:
        pass
    else:
        if not bcrypt.check_password_hash(result.password, request.form['password']):
            pass
        else:
            session['email'] = result.email
            session['first_name'] = result.first_name
            session['last_name'] = result.last_name
            session['user_id'] = result.id
            return redirect("/dashboard")