from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_0 = request.GET.get('sort', 'id')
    if sort_0 == 'name':
        sort_0 = 'name'
    elif sort_0 == 'min_price':
        sort_0 = 'price'
    elif sort_0 == 'max_price':
        sort_0 = '-price'
    phones = Phone.objects.all().order_by(sort_0)

    context = {
        'phones': phones,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    for phone in phones:
        if phone.slug == slug:
            need_phone = phone
    context = {
        "phone": need_phone,
    }
    return render(request, template, context)
