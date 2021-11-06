from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    db = 'emails'
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod      # create email
    def save(cls,data):
        query = 'insert into email(email) value (%(email)s);'
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):  # select all emails
        query = 'select * from email;'
        results = connectToMySQL(cls.db).query_db(query)
        all_emails = []
        for emails in results:
            all_emails.append(cls(emails))
        return all_emails
    
    @classmethod   # destroy email
    def destroy(cls,data):
        query = 'delete from email where id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)
    
    
    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM email WHERE email = %(email)s;"
        results = connectToMySQL('emails').query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!")
            is_valid=False
        return is_valid

