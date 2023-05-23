from django.shortcuts import render

def index(request):
    return render(request, 'YHJ/index.html')

