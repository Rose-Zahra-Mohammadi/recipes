from flask import session, request, render_template, redirect, flash
from flask_app import app
# from flask_app.models.

@app.route("/display/recipe")
def display_recipe():
    return render_template("recipe.html")

@app.route("/recipe/new", methods = ['POST'])
def create_recipe():
    pass

@app.route("/dashboard")
def display_recipes():
    recipes = Recipe.get_all()
    return render_template("dashboard.html", recipes = recipes)