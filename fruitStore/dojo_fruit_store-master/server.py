from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    # firstName = request.form["first_name"]
    order_info = {
        "firstName": request.form["first_name"],
        "lastName": request.form["last_name"],
        "email": request.form["student_id"],
        "strawberry": request.form["strawberry"],
        "raspberry": request.form["raspberry"],
        "apple": request.form["apple"]
    }

    print(request.form)
    return render_template("checkout.html", order_info=order_info)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
