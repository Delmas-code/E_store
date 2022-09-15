from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Products, Category


# Create your views here.

def shop(request):
    products = Products.objects.all()
    category = Category.objects.all()

    paginator = Paginator(products, per_page=6)
    # page_object = paginator.get_page(page)

    # the page request var
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    context = {
        'products': paginator_queryset,
        'page_request_var': page_request_var,
        'category': category,

    }

    return render(request, 'shop.html', context)


def cart(request):
    context = {}

    return render(request, 'cart.html', context)


def checkout(request):
    context = {}

    return render(request, 'checkout.html', context)


def detail(request, id):
    product = get_object_or_404(Products, id=id)
    context = {
        'product': product
    }

    return render(request, 'detail.html', context)


@login_required(login_url="admin")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="admin")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("shop")


@login_required(login_url="admin")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("shop")


@login_required(login_url="admin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("shop")


@login_required(login_url="admin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("shop")


@login_required(login_url="admin")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
