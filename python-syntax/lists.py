vegan_nonos = ['eggs','meat','milk','fish','figs']
pie_ingredients = ['flour','apples','sugar','eggs','salt','fish']
allergic = ['fish','peanuts']

for food in pie_ingredients:
    if food in allergic:
        print(f"dont eat that {food} you gonna die")
    if food in vegan_nonos:
        print(f'dis {food} not vegan friendly lul')
    else:
        print(f"dis {food} going in da pie")