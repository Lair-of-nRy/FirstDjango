from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = """<h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>Кожанов А.Н.</i>"""
    return HttpResponse(text)

def about(request):
    text = """<p>Имя: Александр<br>
        Отчество: Николаевич<br>
        Фамилия: Кожанов<br>
        телефон: 8-925-**-**-**<br>
        email: ***@gmail.com"""
    return HttpResponse(text)