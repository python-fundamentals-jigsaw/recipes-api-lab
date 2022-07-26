from src.client import *

def test_recipe_url_returns_the_url_to_search_by_meal_name():
    meal_name = 'pizza'
    assert recipe_url(meal_name) == "https://www.themealdb.com/api/json/v1/1/search.php?s=pizza"

def test_main_ingredient_url_returns_the_url_to_search_by_ingredient():
    main_ingredient = 'chicken'
    assert main_ingredient_url(main_ingredient) == 'https://www.themealdb.com/api/json/v1/1/filter.php?i=chicken'
    
def test_request_by_recipe():
    results = request_by_recipe('pizza')
    assert results['meals'][0]['strMeal'] == 'Pizza Express Margherita'

def test_request_by_main_ingredient():
    results = request_by_main_ingredient('cheese')
    assert results['meals'][0]['strMeal'] == 'Big Mac'

def test_request_by_id():
    results = request_by_id('52772')
    assert results['meals'][0]['idMeal'] == '52772'