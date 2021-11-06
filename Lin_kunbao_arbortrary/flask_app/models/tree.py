from flask.helpers import send_file
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from . import user

class Tree:
    db = 'arbortrary'

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.reason = data['reason']
        self.date_planted = data['date_planted']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None


    @classmethod
    def save(cls,data):
        query = "INSERT INTO trees (name, location, reason, date_planted, user_id) VALUES (%(name)s,%(location)s,%(reason)s,%(date_planted)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod # get all from table trees
    def get_all(cls):
        query = "SELECT * FROM trees LEFT JOIN users on users.id = user_id;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_trees = []
        print(results)
        for row in results:
            this_tree = cls(row)
            user_info ={
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            } 
            this_user = user.User(user_info)
            this_tree.user = this_user
            all_trees.append(this_tree)
        return all_trees

    
    @classmethod  
    def get_one(cls,data):
        query = "SELECT * FROM trees WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod  
    def update(cls, data):
        query = "UPDATE trees SET name=%(name)s, location=%(location)s, reason=%(reason)s, date_planted = %(date_planted)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod 
    def destroy(cls,data):
        query = "DELETE FROM trees WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod 
    def get_user_trees(cls,data):
        query = 'select * from trees left join users on trees.user_id = users.id where users.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        trees = []
        for tree in results:
            trees.append(cls(tree))
        return trees

    @staticmethod
    def validate_tree(tree):
        is_valid = True
        if len(tree['name']) < 5:
            is_valid = False
            flash("Tree Name must be at least 5 characters","tree")
        if len(tree['location']) < 3:
            is_valid = False
            flash("location must be at least 3 characters","tree")
        if len(tree['reason']) > 50:
            is_valid = False
            flash("Reason max 50 characters","tree")
        if tree['date_planted'] == "":
            is_valid = False
            flash("Please enter a date","tree")
        return is_valid
