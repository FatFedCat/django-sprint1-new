from django.shortcuts import render

def about(request):
    template = 'pages/about.html'
    render(request, template)

def rules(request):
    template = 'pages/rules.html'
    render(request, template)