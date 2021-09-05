from flask_app import app
from flask_app.controllers import users, openmics


if __name__ == "__main__":
    app.run(debug=True)
