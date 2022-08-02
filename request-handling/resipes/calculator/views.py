from django.http import HttpResponse

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных

def calculate_view(request, dish_get):
    servings = int(request.GET.get('servings', 1))
    send_dish = {}
    for dish, ingredients in DATA.items():
        if dish_get == dish:
            for ingredient, count in ingredients.items():
                send_dish[ingredient] = count * servings
    context = {
        'recipe': send_dish
    }

    return render(request, 'index.html', context)


def home_view(request):
    return HttpResponse('Рецепты')
