from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST', 'GET'])
def results():
    results = {
        "name": request.form["name"],
        "locat": request.form["locat"],
        "lang": request.form["lang"],
        "textArea": request.form["textArea"]
    }
    print(request.form)
    return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
