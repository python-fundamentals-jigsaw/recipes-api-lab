import requests

def recipe_url(meal_name):
    return f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"

def request_by_recipe(meal_name):
    url = recipe_url(meal_name)
    response = requests.get(url)
    return response.json()

def main_ingredient_url(main_ingredient):
    return f"https://www.themealdb.com/api/json/v1/1/filter.php?i={main_ingredient}"

def request_by_main_ingredient(main_ingredient):
    url = main_ingredient_url(main_ingredient)
    response = requests.get(url)
    return response.json()

def id_url(id):
    return f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"

def request_by_id(id):
    url = id_url(id)
    response = requests.get(url)
    return response.json()