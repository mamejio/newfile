from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProductForm, OrderForm

def homepage(request):
    return render(request, 'pages/homepage.html')

def products(request):
    product = Product.objects.all()
    return render(request, 'pages/products.html', {'product': product})

def about(request):
    return render(request, 'pages/about.html')

def order(request):
    order = OrderItem.objects.all()
    return render(request, 'pages/order.html', {'order':order})

def addOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    context = {
        'form':form
    }
    return render(request, 'pages/addOrder.html', context)

def editOrder(request, pk):
    order = OrderItem.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order')
    context = {
        'form':form
    }
    return render(request, 'pages/editOrder.html', context)

def deleteOrder(request, pk):
    order = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order')
    context = {
        'order':order
    }
    return render(request, 'pages/deleteOrder.html', context)

def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form':form
    }
    return render(request, 'pages/addProduct.html', context)



def editProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {
        'form':form
    }
    return render(request, 'pages/editProduct.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {
        'product':product
    }
    return render(request, 'pages/deleteProduct.html', context)




