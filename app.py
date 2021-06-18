import os
import re
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.validators import (
    InputRequired, Length, Email, EqualTo, DataRequired)
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

class RegistrationForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired(), Length(
        min=5, max=15, message='Name must be between \
            %(min)d and %(max)d characters long')])
    user_password = PasswordField(
        'user_password', validators=[DataRequired(), Length( min=8, max=20, \
            message='Password must be between  %(min)d and %(max)d characters \
                long.')])
    check_password = PasswordField('check_password', validators=[EqualTo(
        'user_password', message="Passwords don't match")])
    user_email = StringField('user_email', validators=[InputRequired(), Email(), \
        Length(max=120)])
  
class LoginForm(FlaskForm):
    user_name_login = StringField('user_name', validators=[DataRequired(), Length(
        min=5, max=15, message='Name must be between \
            %(min)d and %(max)d characters long')])
    user_password_login = PasswordField(
        'user_password', validators=[DataRequired()])
    

@app.route("/")
@app.route("/get_index")
def get_index():
    return render_template("index.html")


@app.route("/get_all_quotes")
def get_all_quotes():
    quotes = mongo.db.quotes.find()
    return render_template("quotes.html", quotes=quotes)


@app.route("/register", methods=["GET", "POST"])
def register():
    # refer to registration form
    form = RegistrationForm()
    
    # POST method
    if form.validate_on_submit():
        
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"user_name": form.user_name.data.lower()})
        
        # check if email exists
        existing_email = mongo.db.users.find_one(
            {"user_email": form.user_email.data.lower()})
        
        # if username exist
        if existing_user:
            flash("Username already exist")
            return redirect(url_for('register'))
        
        # if email exists
        if existing_email:
            flash("Email address already registered")
            return redirect(url_for('register'))
        
        # distionary of input values for mongo 
        register = {
            "user_name": form.user_name.data.lower(),
            "user_email": form.user_email.data.lower(),
            "user_password": generate_password_hash(form.user_password.data, \
                method='pbkdf2:sha512:52000', salt_length=16),
            "favourite_quotes": ""
        }
        
        # insert user into database
        mongo.db.users.insert_one(register)
        # update int id for user
        user_counter = int(mongo.db.user_counter.find_one("value"))
        user_counter = +1
        mongo.db.tasks.update({"value": user_counter})
        
        # user cookie session
        session["user"] = form.user_name.data.lower()
        flash("User registered succesfully")
        flash("cookie: {}".format(session['user']))
        
        return redirect(url_for('profile', username=session['user']))
        
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    # on submit check if user exist 
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"user_name": form.user_name_login.data.lower()})
        flash("user: {}".format(form.user_name_login.data))
        
        if existing_user:
            # check if password match
            if check_password_hash(existing_user["user_password"], \
                form.user_password_login.data):
                session["user"] = form.user_name_login.data.lower()
                flash("Welcome, {}".format(form.user_name_login.data))
                flash("cookie: {}".format(session['user']))
                return redirect(url_for('profile', username=session['user']))
            
            else:
                # password dont match
                flash("Incorrect login details-p")
                return redirect(url_for('login'))
    
        else:
            # incorrect username
            flash("Incorrect login details-un")
            return redirect(url_for('login'))
            
    return render_template("login.html", form=form)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    
    # find user name in mongo using session cookie. [only user_name]
    username = mongo.db.users.find_one({"user_name": session["user"]})["user_name"]
    
    #only render if session cookie exist
    if session['user']:
        # first to be retrieved on html, second from previous line
        return render_template("profile.html", user_name=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from cookie session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/my_qoutes/<username>")
def my_quotes(username):
    username = mongo.db.users.find_one({"user_name": session["user"]})["user_name"]
    quotes = mongo.db.quotes.find()
    
    return render_template("my_quotes.html", user_name=username, quotes=quotes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)