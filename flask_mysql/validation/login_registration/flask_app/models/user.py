from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = 'login_registration'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod   #method that create a new user
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod #method that search user in database by email
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])


    @staticmethod
    def validate_register(user):
        is_valid = True
        query = 'select * from users where email = %(email)s;'
        results = connectToMySQL('login_registration').query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.",'register')
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!",'register')
            is_valid=False
        if len(user['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.",'register')
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.",'register')
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.",'register')
        if user['password'] != user['confirm']:
            flash("Passwords don't match","register")
        return is_valid
        
