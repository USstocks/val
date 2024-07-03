from django.shortcuts import render


def industries(request):
    template = 'pages/industries.html'
    return render(request, template)


def spx(request):
    template = 'pages/spx.html'
    return render(request, template)
