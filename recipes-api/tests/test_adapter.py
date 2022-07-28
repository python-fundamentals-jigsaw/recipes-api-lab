from src.adapter import *

sample_meal = {'idMeal': '52772', 'strMeal': 'Teriyaki Chicken Casserole', 'strDrinkAlternate': None, 
'strCategory': 'Chicken', 'strArea': 'Japanese',
 'strInstructions': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wvpsxx1468256321.jpg', 'strTags': 'Meat,Casserole', 'strYoutube': 'https://www.youtube.com/watch?v=4aZr5hZXP_s',
  'strIngredient1': 'soy sauce', 'strIngredient2': 'water', 'strIngredient3': 'brown sugar', 'strIngredient4': 'ground ginger', 'strIngredient5': 'minced garlic', 'strIngredient6': 'cornstarch', 'strIngredient7': 'chicken breasts', 'strIngredient8': 'stir-fry vegetables', 'strIngredient9': 'brown rice', 'strIngredient10': '', 'strIngredient11': '', 'strIngredient12': '', 'strIngredient13': '', 'strIngredient14': '', 'strIngredient15': '', 'strIngredient16': None, 'strIngredient17': None, 'strIngredient18': None,
  'strIngredient19': None, 'strIngredient20': None, 'strMeasure1': '3/4 cup', 'strMeasure2': '1/2 cup', 'strMeasure3': '1/4 cup', 'strMeasure4': '1/2 teaspoon', 'strMeasure5': '1/2 teaspoon', 'strMeasure6': '4 Tablespoons', 'strMeasure7': '2', 'strMeasure8': '1 (12 oz.)', 'strMeasure9': '3 cups', 'strMeasure10': '', 'strMeasure11': '',
 'strMeasure12': '', 'strMeasure13': '', 'strMeasure14': '', 'strMeasure15': '', 'strMeasure16': None, 'strMeasure17': None, 'strMeasure18': None, 'strMeasure19': None, 'strMeasure20': None, 'strSource': None, 'strImageSource': None, 'strCreativeCommonsConfirmed': None, 'dateModified': None}

sample_meals = [{'strMeal': 'Brown Stew Chicken', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg', 'idMeal': '52940'}, {'strMeal': 'Chicken & mushroom Hotpot', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuuspp1511297945.jpg', 'idMeal': '52846'}, {'strMeal': 'Chicken Alfredo Primavera', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/syqypv1486981727.jpg', 'idMeal': '52796'}, {'strMeal': 'Chicken Basquaise', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wruvqv1511880994.jpg', 'idMeal': '52934'}, {'strMeal': 'Chicken Congee', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529446352.jpg', 'idMeal': '52956'}, {'strMeal': 'Chicken Handi', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wyxwsp1486979827.jpg', 'idMeal': '52795'}, {'strMeal': 'Kentucky Fried Chicken', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xqusqy1487348868.jpg', 'idMeal': '52813'}, {'strMeal': 'Kung Pao Chicken', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1525872624.jpg', 'idMeal': '52945'}, {'strMeal': 'Pad See Ew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuuspp1468263334.jpg', 'idMeal': '52774'}, {'strMeal': 'Piri-piri chicken and slaw', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/hglsbl1614346998.jpg', 'idMeal': '53039'}, {'strMeal': 'Thai Green Curry', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sstssx1487349585.jpg', 'idMeal': '52814'}]

def test_meal_recipe():
    meal_name = 'Pizza'
    recipe = meal_recipe(meal_name)
    assert recipe == '1 Preheat the oven to 230°C.\r\n\r\n2 Add the sugar and crumble the fresh yeast into warm water.\r\n\r\n3 Allow the mixture to stand for 10 – 15 minutes in a warm place (we find a windowsill on a sunny day works best) until froth develops on the surface.\r\n\r\n4 Sift the flour and salt into a large mixing bowl, make a well in the middle and pour in the yeast mixture and olive oil.\r\n\r\n5 Lightly flour your hands, and slowly mix the ingredients together until they bind.\r\n\r\n6 Generously dust your surface with flour.\r\n\r\n7 Throw down the dough and begin kneading for 10 minutes until smooth, silky and soft.\r\n\r\n8 Place in a lightly oiled, non-stick baking tray (we use a round one, but any shape will do!)\r\n\r\n9 Spread the passata on top making sure you go to the edge.\r\n\r\n10 Evenly place the mozzarella (or other cheese) on top, season with the oregano and black pepper, then drizzle with a little olive oil.\r\n\r\n11 Cook in the oven for 10 – 12 minutes until the cheese slightly colours.\r\n\r\n12 When ready, place the basil leaf on top and tuck in!'

def test_meal_names_and_ids():
    names_and_ids = meal_names_and_ids(sample_meals)
    assert names_and_ids == [{'name': 'Brown Stew Chicken', 'id': '52940'}, {'name': 'Chicken & mushroom Hotpot', 'id': '52846'}, {'name': 'Chicken Alfredo Primavera', 'id': '52796'}, {'name': 'Chicken Basquaise', 'id': '52934'}, {'name': 'Chicken Congee', 'id': '52956'}, {'name': 'Chicken Handi', 'id': '52795'}, {'name': 'Kentucky Fried Chicken', 'id': '52813'}, {'name': 'Kung Pao Chicken', 'id': '52945'}, {'name': 'Pad See Ew', 'id': '52774'}, {'name': 'Piri-piri chicken and slaw', 'id': '53039'}, {'name': 'Thai Green Curry', 'id': '52814'}]

def test_find_ingredients_from_returns_a_list_of_meal_ingredients():
    ingredients = find_ingredients_from(sample_meal)
    assert ingredients == ['soy sauce', 'water', 'brown sugar', 'ground ginger', 
    'minced garlic', 'cornstarch', 'chicken breasts', 'stir-fry vegetables', 'brown rice']

def test_ingredients_and_measurements():
    str_ingredients = [f'strIngredient{i}' for i in range(1, 20)]
    ingredients = find_ingredient_measurements(sample_meal)
    assert ingredients == {'soy sauce': '3/4 cup', 'water': '1/2 cup', 'brown sugar': '1/4 cup',
     'ground ginger': '1/2 teaspoon', 'minced garlic': '1/2 teaspoon', 'brown rice': '3 cups'
     'cornstarch': '4 Tablespoons', 'chicken breasts': '2', 'stir-fry vegetables': '1 (12 oz.)'}
