from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

AUTOR = {'Имя': 'Александр',
        'Отчество': 'Николаевич',
        'Фамилия': 'Кожанов',
        'телефон': '8-925-**-**-**',
        'email': '***@gmail.com'}

ITEMS = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #     <strong>Автор</strong>: <i>Кожанов А.Н.</i>"""
    # return HttpResponse(text)
    context = {
        'name': "Александр",
        'email': "***@gmail.com"
    }
    return render(request, "index.html", context)

def about(request):
    text = f'<p>Имя: <b>{AUTOR["Имя"]}</b><br>\
        Отчество: <b>{AUTOR["Отчество"]}</b><br>\
        Фамилия: <b>{AUTOR["Фамилия"]}</b><br>\
        телефон: <b>{AUTOR["телефон"]}</b><br>\
        email: <b>{AUTOR["email"]}</b>\
        <p><a href="/"><b> Home </b></a> <b>/</b>\
              <a href="/items"><b> Items </b></a>'
    return HttpResponse(text)

def get_items(request):
    # data = []
    # for item in ITEMS:
    #     data.append(f'''<li><a href="/item/{item['id']}">{item['name']}</li><br>''')
    # result = f'<h1>список товаров</h1><ol><br>{"".join(data)}</ol>'
    # return HttpResponse(result)
    context = {
        'items': ITEMS
    }
    return render(request, 'items-list.html', context)

def get_item(request, id):
    for item in ITEMS:
        if item['id'] == id:
    #         result = f'<p>{item["name"]} - {item["quantity"]} шт<br>\
    #             <a href="/items"> Назад к списку товаров</a>'
    #         return HttpResponse(result)
    
            context = {
                'items': ITEMS,
                'id': id
            }
            return render(request, 'item.html', context)
    return HttpResponseNotFound(f'<p>Товар с id={id} не найден')
        