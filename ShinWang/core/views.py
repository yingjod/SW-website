from django.shortcuts import render

from item.models import Category, Item

def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    catrgories = Category.objects.all()

    return render(request, 'core/index.html',{
      'categories':catrgories,
      'items':items, 
    })

def contact(request):
    return render(request, 'core/contact.html')