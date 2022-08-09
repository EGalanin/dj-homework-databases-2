from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            obj = Phone.objects.all().order_by('name')
        if sort == 'min_price':
            obj = Phone.objects.all().order_by('price')
        if sort == 'max_price':
            obj = Phone.objects.all().order_by('-price')
    else:
        obj = Phone.objects.all()

    context = {'phones': obj}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
