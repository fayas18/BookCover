from django.shortcuts import render

def home(request):
    return render(request, 'bookcover/index.html')