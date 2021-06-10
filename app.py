import os
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
        'user_password', validators=[DataRequired(), Length( min=8, max=20, message='Password \
            must be between  %(min)d and %(max)d characters long.')])
    check_password = PasswordField('check_password', validators=[EqualTo(
        'user_password', message="Passwords don't match")])
    user_email = StringField('user_email', validators=[InputRequired(), Email(), Length(
        max=120)])
  

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
    form = RegistrationForm()
    
    if form.validate_on_submit():
        
        existing_user = mongo.db.users.find_one(
            {"user_name": form.user_name.data.lower()})
        
        existing_email = mongo.db.users.find_one(
            {"user_email": form.user_email.data.lower()})
        
        if existing_user:
            flash("Username already exist")
            return redirect(url_for('register'))
        
        if existing_email:
            flash("Email address already registered")
            return redirect(url_for('register'))
        
        register = {
            "user_name": form.user_name.data.lower(),
            "user_email": form.user_email.data.lower(),
            "user_password": generate_password_hash(form.user_password.data, \
                method='pbkdf2:sha512:52000', salt_length=16),
            "favourite_quotes": ""
        }
        # insert user into database
        mongo.db.users.insert_one(register)
        # user cookie session
        session["user"] = form.user_name.data.lower()
        flash("User registered succesfully")
        
        """
        return "<h1> The username is {}. The password is {}. The check is {}. \
            The email is {}. Hash is {}".format(form.user_name.data, \
                form.user_password.data, form.check_password.data, form.user_email.data, \
                generate_password_hash(form.user_password.data, \
                method='pbkdf2:sha512:52000', salt_length=16))
    """
    """
    if request.method == "POST":
    
        # check if name/email already registered
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("user_name").lower()})
        existing_email = mongo.db.users.find_one(
            {"user_password": request.form.get("user_password").lower()})
        
        if existing_user or existing_email:
            flash("Username or password already exist")
            return redirect("register")
        
        register = {
            "user_name": request.form.get("user_name").lower(),
            "user_email": request.form.get("user_email").lower(),
            "user_password": generate_password_hash(request.form.get("user_password"))
        }
    """
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)