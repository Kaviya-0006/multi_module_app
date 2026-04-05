from flask import Flask, request, jsonify, render_template, redirect
from database import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

with app.app_context():
    db.create_all()

# Dashboard
@app.route("/")
def dashboard():
    count = User.query.count()
    return render_template("dashboard.html", count=count)

# Login page
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username,password=password).first()

        if user:
            return redirect("/")
        else:
            return "Invalid Login"

    return render_template("login.html")


# Register page
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"]
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


# View users
@app.route("/users")
def users():

    all_users = User.query.all()

    return render_template("users.html", users=all_users)


if __name__ == "__main__":
    app.run(port=5000,debug=True)