from django.shortcuts import render

def main(request):
    template = 'main/first.html'
    return render(request, template)
