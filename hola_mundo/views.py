from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1>¡Hola Mundo, estoy usando Django!</h1><p>Programación en Python</p>")
