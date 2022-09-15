from django.shortcuts import render, redirect
from products.models import Products
from .models import User, Client_Subscribe

# Create your views here.


def index(request):

    trending_products = Products.objects.order_by('name')[:8]

    if request.method == 'POST':

        subscribtion_email = Client_Subscribe.objects.create(
            name=request.user,
            email=request.POST.get('client_email')
        )

        return redirect('index')

    context = {
        'products': trending_products
    }
    return render(request, 'index.html', context)


def login(request):
    page = 'login'
    context = {
        'page': page
    }

    return render(request, 'login_register.html', context)


def register(request):

    context = {

    }

    return render(request, 'login_register.html', context)
