from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Cart
from .forms import ProductForm
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


@login_required()
def cart_view(request):
    current_user = request.user
    current_cart = Cart.objects.filter(buyer=current_user.id)
    context = {
            "cart_list": current_cart
    }
    return render(request, 'cart.html', context)


def product_list_view(request):
    size = int(request.GET.get('size', 10))
    page_number = request.GET.get('page')
    products = Product.objects.all()
    paginator = Paginator(products, size)
    page_obj = paginator.get_page(page_number)
    featured = Product.objects.filter(featured=True)
    context = {
            "products": products,
            "featured_products": featured,
            "page_obj": page_obj
    }

    return render(request, 'products/product_list.html', context)


def product_delete_view(request, id):
    product = Product.objects.get(id=id)

    if request.POST:
        product.delete()
        return redirect('/products/')

    context = {'product': product}
    return render(request, 'products/product_delete.html', context)


def product_edit_view(request, id):
    product = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance=product)

    if request.POST and form.is_valid():
        form.save()
        return redirect('/products/')

    context = {'form': form}
    return render(request, 'products/product_create.html', context)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    product.count_views += 1
    product.save()
    if request.POST:  # Para adicionar produto ao carrinho de compras
        amount = int(request.POST.get('amount', 1))
        if amount > product.total_in_stock:
            messages.error(request, f"Sorry, we only have {product.total_in_stock} in stock.")
        else:
            messages.success(request, 'Your product was added in cart.')
    context = {
            'product': product
    }
    return render(request, 'products/product_detail.html', context)



def product_create_view(request):
   form = ProductForm(request.POST or None)
   if form.is_valid():
       form.save()
       form = ProductForm()
   context = {
           'form': form
   }
   return render(request, 'products/product_create.html', context)

@login_required()
def product_buy_view(request, id):  # funcao para fechar compra
    product = Product.objects.get(id=id)
    amount = int(request.POST.get('amount', 1))

    if request.POST:
        product.sell(amount)  # retirada de estoque do banco de dados
        try:
            product.save()
            messages.success(request, 'Order successfully completed.')
            return redirect('/products/')
        except IntegrityError:
            messages.error(request, f"Sorry, we only have {product.total_in_stock} in stock.")

    context = {'product': product}
    return render(request, 'products/product_buy.html', context)


