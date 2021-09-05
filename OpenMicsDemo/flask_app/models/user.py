import re
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.openmic import OpenMic

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("must be more than 3 characters")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("must be more than 3 characters")
            is_valid = False
        if len(data['password']) < 5:
            flash("must be more than 5 characters")
            is_valid = False
        if data['password'] != data['conf_pass']:
            flash('passwords must match')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("email must be valid")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("openmics_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL("openmics_schema").query_db(query, data)

    @classmethod
    def user_info(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("openmics_schema").query_db(query, data)
        return cls(results[0])
