from copy import deepcopy

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
}


def service_assistant(request, dish_name):

    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe': {}
    }

    for key in DATA.keys():
        if dish_name in key:
            context["recipe"] = deepcopy(DATA[dish_name])
            for key, value in context["recipe"].items():
                context["recipe"][key] = value * servings

    return render(request, 'calculator/index.html', context)