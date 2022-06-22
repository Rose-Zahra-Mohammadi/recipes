from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.controllers import recipe_controller

class Recipe:
    def __init__(self, data):
        self.id = data['data']
        self.name = data['name']
        self.description['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.under_thirty = data['under_thirty']
        self.user_id = data['user_id']

    @classmethod
    def create(cls,data):
        query =  "INSERT INTO recipes(name, description, instructions, under_thirty, user_id) "
        query += "VALUES(%(name)s, %(description)s, %(instructions)s, %(udner_thirty)s, %(user_id)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query =  "SELECT * "
        query += "FROM recipes;"

        result = connectToMySQL(DATABASE).query_db(query)

        recipes = []

        if len(result) > 0:
            for recipe in result:
                recipes.append(cls(recipe))
        return recipes