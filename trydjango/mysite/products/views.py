from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# from django.http import JsonResponse
from .models import Product
from .forms import ProductForm, RawProductForm

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
    # return JsonResponse(list(products.values()), safe=False)


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


def product_buy_view(request, id):
    product = Product.objects.get(id=id)
    amount = int(request.POST.get('amount', 1))

    if request.POST:
        product.sell(amount) # TODO: tratar exception de integridade.
        product.save()
        return redirect('/products/')

    context = {'product': product}
    return render(request, 'products/product_buy.html', context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#             'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)



