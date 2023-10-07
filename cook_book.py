from pprint import pprint
with open ("recipes.txt", encoding='utf-8') as f:
    cook_book = {}
    lines = f.read().split("\n\n")
    for line in lines:
        dish = line.split("\n")[0]
        cook_book[dish] = []
        for ingredient in line.split("\n")[2:]:
            ingreadient_name,quantity,measure = ingredient.split(" | ")
            cook_book[dish].append({'ingreadient_name':ingreadient_name,'quantity':quantity,'measure':measure})

def get_shop_list_by_dishes(dishes,person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:

            for ingredient in cook_book[dish]:


                ingredient_name = ingredient['ingreadient_name']

                if ingredient['ingreadient_name'] not in shop_list.keys():
                    shop_list[ingredient['ingreadient_name']] = {'measure': ingredient['measure'],'quantity': int(ingredient['quantity']) * person_count}
                else:
                    shop_list[ingredient['ingreadient_name']] = {'measure': ingredient['measure'],
                                                                 'quantity': shop_list[ingredient_name]['quantity'] + (int(ingredient['quantity']) * person_count)}


        else:
            return "Такого блюда нет в книге рецептов"
    return shop_list

pprint(get_shop_list_by_dishes(["Омлет"],3))
pprint(get_shop_list_by_dishes(["Омлет","Фахитос"],2))