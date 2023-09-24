from django.shortcuts import render

# Create your views here.

def showauthors(request):
    return render(request, "Authors\\authors.html")
