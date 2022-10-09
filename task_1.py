with open('recipes.txt', 'rt', encoding='utf8') as file:
    cook_book = {}
    for l in file:
        dish = l.strip()
        ingredients = []
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingr = file.readline()
            ingredients_name, quantity, measure = ingr.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredients_name, 'quantity': int(quantity), 'measure': measure})
        blank_line = file.readline()
        cook_book.update({dish: ingredients})
print(cook_book)