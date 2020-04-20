from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from products.models import Product
from .models import Banner, Services, Video, Testimonial

class PagesView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        context = {
            'my_text': 'This is about us',
            'my_number': 1234,
            'my_list': [123, 456, 789, 'abc'],
            'this_is_true': True
        }
        return render(request, self.template_name, context)


def home_view(request):
    featured_products = Product.objects.filter(featured=True)
    bestsellers_products = Product.objects.order_by('-count_sells')[:3]
    most_viewed_products = Product.objects.order_by('-count_views')[:3]
    banners = Banner.objects.all()[:3]
    services = Services.objects.all()[:3]
    videos = Video.objects.all()[:1]
    testimonials = Testimonial.objects.all()[:1]

    context = {
            "featured_products": featured_products,
            "bestsellers_products": bestsellers_products,
            "most_viewed_products": most_viewed_products,
            "banners": banners,
            "services": services,
            "videos": videos,
            "testimonials": testimonials

    }
    return render(request, 'home.html', context)

# def about_view(request, *args, **kwargs):
#     my_context = {
#             'my_text': 'This is about us',
#             'my_number': 1234,
#             'my_list': [123, 456, 789, 'abc'],
#             'this_is_true': True
#     }
#     return render(request, 'about.html', my_context)


# def home_view(request, *args, **kwargs):
#     print(args, kwargs)
#     print(request.user)
#     # return HttpResponse('<h1>Hello World</h1>')
#     return render(request, 'home.html', {})


# def contact_view(request, *args, **kwargs):
#     return render(request, 'contact.html', {})


# def social_view(request, *args, **kwargs):
#    return render(request, 'social.html', {})




