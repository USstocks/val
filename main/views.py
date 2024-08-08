from django.shortcuts import render

def first(request):
    template = 'main/first.html'
    return render(request, template)

