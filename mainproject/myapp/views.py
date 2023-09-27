from django.shortcuts import render


def my_view(request):
    context = {"name": "Welcome! This is my server project"}
    return render(request, "myapp/index.html", context)
