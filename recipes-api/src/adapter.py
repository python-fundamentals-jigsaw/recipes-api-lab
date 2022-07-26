from src.client import *

def meal_names_and_ids(meals):
    return [{'name': meal['strMeal'], 'id': meal['idMeal']} for meal in meals]

def meal_recipe(meal_name):
    recipe_response = request_by_recipe(meal_name)['meals'][0]
    return recipe_response['strInstructions']

def find_ingredients_from(meal):
    str_ingredients = [f'strIngredient{i}'for i in range(1, 20)]
    return [meal[str_ingredient] for str_ingredient in str_ingredients if meal[str_ingredient]]

def find_ingredient_measurements(meal):
    ingredients = find_ingredients_from(meal)
    str_measures = [f'strMeasure{i}' for i in range(1, len(ingredients)) ]
    measurements = [meal[str_measure] for str_measure in str_measures if meal[str_measure]]
    return dict(zip(ingredients, measurements))

