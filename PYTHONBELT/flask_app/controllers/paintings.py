from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_app.models.painting import Painting


# ======================================================= #
# ==== CREATE =========#
# ======================================================= #

@app.route("/paintings/new")
def create_painting():
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")

    user_id = session['user_id']
    return render_template("create_painting.html", user_id=user_id)

# ======================================================= #
# ==== ADD painting ROUTE =========#
# ======================================================= #


@app.route("/add_painting", methods=["POST"])
def add_painting():
    if not Painting.validate_painting(request.form):
        return redirect("/paintings/new")
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "price": request.form['price'],
        "user_id": request.form['user_id']
    }
    # make sure data is lined correctly and not in the if condition #
    Painting.save(data)
    return redirect("/dashboard")


# ======================================================= #
# ==== SHOW painting ROUTES =========#
# ======================================================= #

@app.route("/painting/<int:id>")
def view_one(id):
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")

    data = {
        "id": id
    }
# watch the stupid indentation with DATA!!!! when this was over on more to the right it came up as being called before assigned or something. fixing indents worked
    painting = Painting.one_painting(data)

    return render_template("view_painting.html", painting=painting)

# ======================================================= #
# ==== EDIT painting ROUTES =========#
# ======================================================= #


@app.route("/painting/<int:id>/edit")
def edit_one(id):
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")

    data = {
        "id": id
    }
# watch the stupid indentation with DATA!!!! when this was over on more to the right it came up as being called before assigned or something. fixing indents worked
    painting = Painting.one_painting(data)
    return render_template("edit_painting.html", painting=painting)


@app.route("/update_painting/<int:id>", methods=["POST"])
def update_painting(id):
    if not Painting.validate_painting(request.form):
        return redirect(f"/painting/{id}/edit")
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "price": request.form['price'],
        "id": id
    }
    Painting.update_painting(data)

    return redirect("/dashboard")

# ======================================================= #
# ==== DELETE painting ROUTES =========#
# ======================================================= #


@app.route("/paintings/delete/<int:id>")
def delete_painting(id):
    data = {
        "id": id
    }
    Painting.delete(data)
    return redirect("/dashboard")
