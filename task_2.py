cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гуада', 'quantity': 100, 'measure': 'г'}
        ],
    'Фахитос': [
        {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
        {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ]
    }
def get_shop_list_by_dishes():
    str_ = input('Введите название блюд через запятую и нажмите Enter: ')
    dishes = str_.split(', ')
    person_count = int(input('Введите количество персон: '))
    shop_list ={}
    for i in dishes:
        for i_ in cook_book[i]:
            if i_['ingredient_name'] in shop_list:
                i_['quantity'] = i_['quantity'] + i_['quantity']
            shop_list.update({i_['ingredient_name']:{'measure': i_['measure'], 'quantity' : (i_['quantity'] * person_count)}})
    print(shop_list)


get_shop_list_by_dishes()
