# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html", num=3)


@app.route('/play/<int:x>')
def number(x):
    num = x
    return render_template("index.html", num=num)


@app.route('/play/<int:x>/<color>')
def numberColor(x, color):
    num = x
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
