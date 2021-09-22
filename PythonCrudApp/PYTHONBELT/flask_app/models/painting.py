from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # holds single instance of a user
        self.posted_by = {}

    @staticmethod
    def validate_painting(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('name must be at least 3 characters long')
            is_valid = False
        if len(data['description']) < 10:
            flash('Description must be at least 10 characters long')
            is_valid = False
        if len(data['price']) < 1:
            flash('price must be at least 1 number long')
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO paintings (name, description, price, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(price)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL("belt").query_db(query, data)

    @classmethod
    def all_paintings(cls):
        query = "SELECT * FROM paintings;"
        results = connectToMySQL("belt").query_db(query)
        paintings = []
        for one_painting in results:
            paintings.append(cls(one_painting))
        
        return paintings

    @classmethod
    def one_painting(cls, data):
        query = "SELECT * FROM paintings JOIN users ON users.id = user_id WHERE paintings.id = %(id)s;"
        results = connectToMySQL("belt").query_db(query, data)

        painting = cls(results[0])
        user_data = {
            "id": results[0]['id'],
            "first_name": results[0]['first_name'],
            "last_name": results[0]['last_name'],
            "email": results[0]['email'],
            "password": results[0]['password'],
            "created_at": results[0]['users.created_at'],
            "updated_at": results[0]['users.updated_at']
        }

        painting.posted_by = user.User(user_data)
        return painting

    @classmethod
    def update_painting(cls, data):
        query = "UPDATE paintings SET name = %(name)s, description = %(description)s, price = %(price)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL("belt").query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s"
        results = connectToMySQL("belt").query_db(query, data)
        return results
