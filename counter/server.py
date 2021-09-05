from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/', methods=['POST', 'GET'])
def index():
    views = session.get('views', None)

    if not views:
        session['views'] = 1
    else:
        session['views'] += 1

    return render_template("index.html")


@app.route('/reset', methods=['POST', 'GET'])
def reset():
    session.clear()
    return redirect("/")


@app.route('/add', methods=['POST', 'GET'])
def counterPlus2():
    session['views'] += 2
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
