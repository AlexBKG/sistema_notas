from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Bienvenido al Sistema de Notas!</h1>")
