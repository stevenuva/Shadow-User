"""
    File name: main.py
    Python Version: 3.6.5
"""

# Source: Python Flask Tutorial
# https://youtu.be/MwZwr5Tvyxo

from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

# initiate Flask application
app = Flask(__name__, template_folder='./templates')

app.config["SECRET_KEY"] = "8f32b53e980b69ae31ef1485"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userData.db"

# initiate database
db = SQLAlchemy(app)

# classes to store specific data to the database


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="user", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"

# routes to different webpages


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', searchNav=False)


@app.route("/about")
def about():
    return render_template('about.html', title='FAQ')


@app.route("/account")
def account():
    return render_template('account.html')


@app.route("/catalogue")
@app.route("/catalogue/<searchInput>", methods=["GET", "POST"])
def catalogue(searchInput="none"):
    return render_template('catalogue.html', searchNav=False, searchInput=searchInput)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '12345':
            flash('Logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password!', 'danger')
    return render_template("login.html", title="Login", navbar=False, form=form, css="css/login.css")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", navbar=False, form=form, css="css/login.css")


@app.route("/account-project")
def project():
    return render_template("account-project.html", title="FAQ")

# account of the fake user seen in the demo video


@app.route("/account-derrick")
def projectUser1():
    return render_template("project-user1.html", title="FAQ")


# run flask application directly
if __name__ == '__main__':
    app.run(debug=True)
