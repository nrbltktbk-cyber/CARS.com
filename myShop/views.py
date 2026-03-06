from django.shortcuts import render
from .models import Category, Product

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'myShop/categories.html', {'categories': categories})

def products_view(request):
    product = Product.objects.all()
    return render(request, 'myShop/products.html', {'products': product})

def category_products_view(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'myShop/category_products.html', {'products': products})
