from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.painting import Painting

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# ======================================================= #
# ==== START OF LOGIN AND REGISTRATION =========#
# ======================================================= #


# ======================================================= #
# ==== BASE =========#
# ======================================================= #

@app.route("/")
def index():
    return render_template('index.html')

# ======================================================= #
# ==== LOGIN =========#
# ======================================================= #


@app.route("/register", methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect("/")
    data1 = {
        "email": request.form['email']
    }
    if User.get_by_email(data1):
        flash("Email already exsists! please use different email to register")
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    new_user_id = User.save(data)
    session["user_id"] = new_user_id
    return redirect('/dashboard')


# ======================================================= #
# ==== LOGIN =========#
# ======================================================= #


@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

# ======================================================= #
# ==== LOGOUT =========#
# ======================================================= #


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ======================================================= #
# ==== END OF LOGIN AND REGISTRATION =========#
# ======================================================= #


# ======================================================= #
# ==== DASHBOARD =========#
# ======================================================= #

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")
    # the if condition above can ONLY go in render routes. NOT REDIRECT ROUTES.#
    data = {
        "id": session['user_id']
    }
    logged_user = User.user_info(data)
    paintings = Painting.all_paintings()
    return render_template("dashboard.html", user=logged_user, paintings=paintings)
