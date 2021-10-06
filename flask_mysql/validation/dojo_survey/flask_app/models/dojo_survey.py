from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo_survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)
    
    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo_survey(results[0])


    @staticmethod
    def is_valid(dojo_survey):
        is_valid = True
        if len(dojo_survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo_survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(dojo_survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(dojo_survey['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid

