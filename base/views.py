from django.shortcuts import render


def principal(request):
    titulo="Bienvenido"
    context={
        "titulo": titulo
    }
    return render(request, "index.html", context)

