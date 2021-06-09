import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

class LoginForm(FlaskForm):
    user_name = StringField('user_name')
    user_password = PasswordField('user_password')
    check_password = PasswordField('check_password')
    user_email = StringField('user_email')

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
    form = LoginForm()
    
    if form.validate_on_submit():
        return "<h1> The username is {}. The password is {}. The check is {}. The email is {}.".format(form.user_name.data, form.user_password.data, form.check_password.data, form.user_email.data)
    
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