from pprint import pprint

# Выбранная реализация работает при любом количестве пустых строк между рецептами в файле рецептов
def parse_recipes() -> dict:
    with open('recipes.txt', encoding='utf-8') as text:
        recipes_library = {}
        ids = ['ingredient_name', 'quantity', 'measure']
        filtered_text = filter(bool, map(str.strip, text))
        for item in filtered_text:
            recipes_library[item] = []
            supplies = next(filtered_text)
            for num in range(int(supplies)):
                recipy_list = next(filtered_text).split(' | ')
                recipy_dict = {id: value for id, value in zip(ids, recipy_list)}
                recipes_library[item].append(recipy_dict)
                continue
            continue
    return recipes_library

# print(parse_recipes())

# Реализовано согласно логике: Заказ ['Омлет', 'Омлет', 2] - 2 клиента хотят по 2 омлета
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shop_list = {}
    for dish in dishes:
        for ingredients in parse_recipes()[dish]:
            if ingredients['ingredient_name'] not in shop_list.keys():
                shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'], \
                    'quantity': int(ingredients['quantity']) * person_count}
            else:
                shop_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
    return shop_list

   
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
