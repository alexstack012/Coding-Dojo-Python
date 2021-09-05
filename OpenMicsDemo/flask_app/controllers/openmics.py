from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_app.models.openmic import OpenMic


# ======================================================= #
# ==== CREATE =========#
# ======================================================= #

@app.route("/openmics/create")
def create_openmic():
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")

    user_id = session['user_id']
    return render_template("create_openmic.html", user_id=user_id)

# ======================================================= #
# ==== ADD OPENMIC ROUTE =========#
# ======================================================= #


@app.route("/add_openmic", methods=["POST"])
def add_openmic():
    if not OpenMic.validate_openmic(request.form):
        return redirect("/openmics/create")
    data = {
        "venue": request.form['venue'],
        "type": request.form['type'],
        "date": request.form['date'],
        "description": request.form['description'],
        "user_id": request.form['user_id']
    }
    # make sure data is lined correctly and not in the if condition #
    OpenMic.save(data)
    return redirect("/dashboard")


# ======================================================= #
# ==== SHOW OPENMIC ROUTES =========#
# ======================================================= #

@app.route("/openmic/<int:id>")
def view_one(id):
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")

    data = {
        "id": id
    }
# watch the stupid indentation with DATA!!!! when this was over on more to the right it came up as being called before assigned or something. fixing indents worked
    openmic = OpenMic.one_openmic(data)
    return render_template("view_openmic.html", openmic=openmic)

# ======================================================= #
# ==== EDIT OPENMIC ROUTES =========#
# ======================================================= #


@app.route("/openmic/edit/<int:id>")
def edit_one(id):
    if "user_id" not in session:
        flash("Please register / login before you can proced to the website")
        return redirect("/")

    data = {
        "id": id
    }
# watch the stupid indentation with DATA!!!! when this was over on more to the right it came up as being called before assigned or something. fixing indents worked
    openmic = OpenMic.one_openmic(data)
    return render_template("edit_openmic.html", openmic=openmic)


@app.route("/update_openmic/<int:id>", methods=["POST"])
def update_openmic(id):
    if not OpenMic.validate_openmic(request.form):
        return redirect(f"/openmic/edit/{id}")
    data = {
        "venue": request.form['venue'],
        "type": request.form['type'],
        "date": request.form['date'],
        "description": request.form['description'],
        "id" : id
    }
    OpenMic.update_openmic(data)

    return redirect("/dashboard")

# ======================================================= #
# ==== DELETE OPENMIC ROUTES =========#
# ======================================================= #

@app.route("/openmics/delete/<int:id>")
def delete_openmic(id):
    data= {
        "id" : id
    }
    OpenMic.delete(data)
    return redirect("/dashboard")