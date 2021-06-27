import os
from urllib.parse import quote
from flask import (
    Flask, config, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.validators import (
    InputRequired, Length, Email, EqualTo, DataRequired)
from flask_censor import Censor
from numpy import random
import datetime
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
censor = Censor(app=app)


# user registration forms
class RegistrationForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired(), Length(
        min=5, max=15, message='Name must be between \
            %(min)d and %(max)d characters long')])
    user_password = PasswordField(
        'user_password', validators=[DataRequired(), Length(
            min=8, max=20, message='Password must be between  %(min)d and \
                %(max)d characters long.')])
    check_password = PasswordField(
        'check_password', validators=[EqualTo(
            'user_password', message="Passwords don't match")])
    user_email = StringField(
        'user_email', validators=[InputRequired(), Email(), Length(max=120)])


# user login form
class LoginForm(FlaskForm):
    user_name_login = StringField(
        'user_name', validators=[DataRequired(), Length(
            min=5, max=15, message='Name must be between \
                %(min)d and %(max)d characters long')])
    user_password_login = PasswordField(
        'user_password', validators=[DataRequired()])


# change password form
class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(
        'current_password',
        validators=[DataRequired()])
    new_password = PasswordField(
        'new_password', validators=[DataRequired(), Length(
            min=8, max=20, message='Password must be between \
                %(min)d and %(max)d characters long.')])
    confirm_new_password = PasswordField(
        'confirm_new_password', validators=[EqualTo(
            'new_password', message="Passwords \
                don't match")])


# add quote form
class AddQuoteForm(FlaskForm):
    latin_text = StringField('latin_text', validators=[DataRequired(), Length(
        min=3, max=150, message='Phrase must be between \
            %(min)d and %(max)d characters long')])
    english_text = StringField(
        'english_text', validators=[DataRequired(), Length(
            min=3, max=150, message='Text must be between \
                %(min)d and %(max)d characters long.')])
    author = StringField('author', validators=[DataRequired()])


# add author form
class AddAuthorForm(FlaskForm):
    author_name = StringField('latin_text', validators=[DataRequired(), Length(
        min=3, max=150, message='Phrase must be between \
            %(min)d and %(max)d characters long')])
    era_lived = StringField('english_text', validators=[DataRequired(), Length(
        min=3, max=150, message='Text must be between \
            %(min)d and %(max)d characters long.')])
    description = StringField('description', validators=[DataRequired()])
    img = StringField('img', validators=[DataRequired()])


# index route
@app.route("/")
@app.route("/get_index")
def get_index():
    quotes = mongo.db.quotes.find()
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

    return render_template(
        "index.html",
        quotes=quotes,
        day=day,
        month=month,
        year=year)


# all quotes route
@app.route("/get_all_quotes")
def get_all_quotes():
    authors_c = mongo.db.authors.find()
    quotes_c = mongo.db.quotes.find()

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)

    return render_template("quotes.html", quotes=quotes, authors=authors)


# sorted by name quotes route
@app.route("/get_sorted_by_names")
def get_sorted_by_names():
    authors_c = mongo.db.authors.find()
    quotes_c = mongo.db.quotes.find().sort([('latin_text', 1)])

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)
    return render_template("quotes.html", quotes=quotes, authors=authors)


# sorted by favourites quotes route
@app.route("/get_sorted_by_favourite")
def get_sorted_by_favourite():
    authors_c = mongo.db.authors.find()
    quotes_c = mongo.db.quotes.find().sort("num_of_likes", -1)

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)
    return render_template("quotes.html", quotes=quotes, authors=authors)


# sorted by newest quotes route
@app.route("/get_sorted_by_newest")
def get_sorted_by_newest():
    authors_c = mongo.db.authors.find()
    quotes_c = mongo.db.quotes.find().sort("_id", -1)

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)
    return render_template("quotes.html", quotes=quotes, authors=authors)


# search bar
@app.route("/search", methods=["GET", "POST"])
def search():
    authors_c = mongo.db.authors.find()
    query = request.form.get("query")
    quotes_c = mongo.db.quotes.find({"$text": {"$search": query}})

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)

    return render_template("quotes.html", quotes=quotes, authors=authors)


# add quote to favourites
@app.route("/add_to_favourites", methods=['POST'])
def add_to_favourites():

    if session['user']:
        username = request.args.get('username')
        id = request.args.get('id')
        # updeate users list
        mongo.db.quotes.update_one(
            {'_id': ObjectId(id)},
            {'$push': {'users_liked': username}}, upsert=True)
        # update num of users
        mongo.db.quotes.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$inc': {'num_of_likes': 1}})

    return redirect(url_for('get_all_quotes'))


# remove favourite quote
@app.route("/remove_from_favourites", methods=['POST'])
def remove_from_favourites():

    if session['user']:
        username = request.args.get('username')
        id = request.args.get('id')
        # remove name from list
        mongo.db.quotes.update_one(
            {'_id': ObjectId(id)}, {'$pull': {'users_liked': username}})
        # decrease counter
        # update num of users
        mongo.db.quotes.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$inc': {'num_of_likes': -1}})

    return redirect(url_for('get_all_quotes'))


# user's quotes route
@app.route("/my_qoutes/<username>")
def my_quotes(username):
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]
    authors_c = mongo.db.authors.find()
    quotes_c = mongo.db.quotes.find()

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)

    return render_template(
        "my_quotes.html", user_name=username,
        quotes=quotes,
        authors=authors)


# user's favourite quotes route
@app.route("/favourite_quotes/<username>")
def favourite_quotes(username):
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]
    authors_c = mongo.db.authors.find()
    quotes_c = mongo.db.quotes.find()

    # convert cursor
    authors = []
    for object in authors_c:
        authors.append(object)

    quotes = []
    for object in quotes_c:
        quotes.append(object)

    return render_template(
        "favourite_quotes.html",
        user_name=username,
        quotes=quotes,
        authors=authors)


# random qoute route
@app.route("/random_qoute")
def random_quote():
    quotes = mongo.db.quotes.find()
    random_id = random.randint(quotes.count())

    return render_template(
        "random_quote.html", quotes=quotes, random_id=random_id)


# add qoute route
@app.route("/add_quote", methods=["GET", "POST"])
def add_quote():
    if session['user']:
        # refer to registration form
        form = AddQuoteForm()

        # POST method
        if form.validate_on_submit():

            # dictionary of input values for mongo
            quote = {
                "latin_text": form.latin_text.data.lower(),
                "english_text": form.english_text.data.lower(),
                "added_by": session['user'],
                "num_of_likes": 0,
                "author": form.author.data.lower(),
                "users_liked": []
            }

            # insert user into database
            mongo.db.quotes.insert_one(quote)
            flash("Quote added")
            return redirect(url_for("my_quotes", username=session['user']))

    return render_template("add_quote.html", form=form)


# update quote
@app.route("/change_quote/<quote_id>", methods=["GET", "POST"])
def change_quote(quote_id):
    if session['user']:
        form = AddQuoteForm()
        quote = mongo.db.quotes.find_one({"_id": ObjectId(quote_id)})

        # POST method
        if form.validate_on_submit():

            # dictionary of input values for mongo
            submit = {
                "latin_text": form.latin_text.data.lower(),
                "english_text": form.english_text.data.lower(),
                "added_by": session['user'],
                "num_of_likes": quote['num_of_likes'],
                "author": form.author.data.lower(),
                "users_liked": quote['users_liked']
            }

            # insert user into database
            mongo.db.quotes.update({"_id": ObjectId(quote_id)}, submit)
            flash("Quote updated")
            return redirect(url_for("my_quotes", username=session['user']))

    return render_template("change_quote.html", quote=quote, form=form)


# delete quote page route
@app.route("/delete_quote_page/<quote_id>", methods=['GET', 'POST'])
def delete_quote_page(quote_id):
    if session['user']:
        quote = mongo.db.quotes.find_one({"_id": ObjectId(quote_id)})

    return render_template("delete_quote_page.html", quote=quote)


# delete quote funcionality
@app.route("/delete_quote/<quote_id>")
def delete_quote(quote_id):
    if session['user']:
        flash("Quote deleted")
        mongo.db.quotes.delete_one({"_id": ObjectId(quote_id)})
        return redirect(url_for("my_quotes", username=session['user']))


# user registration
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

        # dictionary of input values for mongo
        register = {
            "user_name": form.user_name.data.lower(),
            "user_email": form.user_email.data.lower(),
            "user_password": generate_password_hash(
                form.user_password.data,
                method='pbkdf2:sha512:52000',
                salt_length=16),
            "favourite_quotes": ""
        }

        # insert user into database
        mongo.db.users.insert_one(register)

        # user cookie session
        session["user"] = form.user_name.data.lower()
        flash("User registered succesfully")
        # flash("cookie: {}".format(session['user']))
        return redirect(url_for('profile', username=session['user']))

    return render_template("register.html", form=form)


# user login route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # on submit check if user exist
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"user_name": form.user_name_login.data.lower()})

        if existing_user:
            # check if password match
            if check_password_hash(existing_user["user_password"],
                                   form.user_password_login.data):

                    session["user"] = form.user_name_login.data.lower()
                    flash("Welcome, {}".format(form.user_name_login.data))
                    # flash("cookie: {}".format(session['user']))
                    return redirect(
                        url_for('profile', username=session['user']))

            else:
                # password dont match
                flash("Incorrect login details")
                return redirect(url_for('login'))

        else:
            # incorrect username
            flash("Incorrect login details")
            return redirect(url_for('login'))

    return render_template("login.html", form=form)


# user profile route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # only render if session cookie exist
    if session['user']:
        # find user name in mongo using session cookie. [only user_name]
        username = mongo.db.users.find_one(
            {"user_name": session["user"]})["user_name"]
        # first to be retrieved on html, second from previous line
        return render_template("profile.html", user_name=username)

    return redirect(url_for("login"))


# change password
@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    # only render if session cookie exist
    if session['user']:
        form = ChangePasswordForm()
        username = mongo.db.users.find_one({"user_name": session["user"]})
        # POST method
        if form.validate_on_submit():
            # check if password match
            if check_password_hash(username["user_password"],
                                   form.current_password.data):
                    flash("Password updated!")
                    # generate new password hash
                    new_password = generate_password_hash(
                        form.new_password.data, method='pbkdf2:sha512:52000',
                        salt_length=16)
                    mongo.db.users.update_one(
                        {'user_name': username['user_name']},
                        {"$set": {'user_password': new_password}})

            else:
                flash("Password not changed - incorrect old pasword provided!")
            return redirect(url_for('profile', username=session['user']))

    return render_template("change_password.html", form=form)


# user logout route
@app.route("/logout")
def logout():
    # remove user from cookie session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# delete user account page route
@app.route("/delete_page")
def delete_page():
    # only render if session cookie exist
    if session['user']:
        return render_template("delete_page.html")


# delete user account funcionality
@app.route("/delete_user")
def delete_user():

    flash("Account deleted")
    session.pop("user")
    mongo.db.users.delete_one({"user_name": session["user"]})
    return redirect(url_for("register"))


# admin's authors page
@app.route("/authors")
def authors():
    authors = mongo.db.authors.find()
    # internal server error
    if session['user'] == 'admin':
        return render_template("authors.html", authors=authors)


# add author route
@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    if session['user'] == 'admin':
        # refer to form
        form = AddAuthorForm()
        # POST method
        if form.validate_on_submit():
            # dictionary of input values for mongo
            author = {
                "author_name": form.author_name.data.lower(),
                "era_lived": form.era_lived.data.lower(),
                "description": form.description.data.lower(),
                "img": form.img.data,
                }

            # insert author into database
            mongo.db.authors.insert_one(author)
            flash("Author added")
            return redirect(url_for("authors", username=session['user']))

    return render_template("add_author.html", form=form)


# update author
@app.route("/change_author/<author_id>", methods=["GET", "POST"])
def change_author(author_id):
    if session['user'] == 'admin':
        form = AddAuthorForm()
        author = mongo.db.authors.find_one({"_id": ObjectId(author_id)})
        # POST method
        if form.validate_on_submit():
            # dictionary of input values for mongo
            submit = {
                "author_name": form.author_name.data.lower(),
                "era_lived": form.era_lived.data.lower(),
                "description": form.description.data.lower(),
                "img": form.img.data,
            }

            # insert user into database
            mongo.db.authors.update({"_id": ObjectId(author_id)}, submit)
            flash("Author updated")
            return redirect(url_for("authors"))

    return render_template("change_author.html", author=author, form=form)


# delete author page route
@app.route("/delete_author_page/<author_id>", methods=['GET', 'POST'])
def delete_author_page(author_id):
    if session['user'] == 'admin':
        author = mongo.db.authors.find_one({"_id": ObjectId(author_id)})
        return render_template("delete_author_page.html", author=author)


# delete author funcionality
@app.route("/delete_author/<author_id>/")
def delete_author(author_id):
    if session['user'] == 'admin':
        flash("Author deleted")
        mongo.db.authors.delete_one({"_id": ObjectId(author_id)})
        return redirect(url_for("authors"))


@app.errorhandler(404)
def page_not_found(err):
        error_msg = err
        flash("This is weird. It is not here!")
        return render_template("error_404.html", error_msg=error_msg)


@app.errorhandler(500)
def server_error(err):
    error_msg = err
    flash("Something's not quite right.")
    return render_template("error_500.html", error_msg=error_msg)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
