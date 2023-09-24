from django.shortcuts import render

# Create your views here.

def showbooks(request):
    return render(request, "Books\\books.html")
