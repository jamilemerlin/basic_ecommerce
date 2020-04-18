from django.urls import path
from products.views import product_list_view, product_detail_view, product_create_view, product_edit_view, product_buy_view, product_delete_view

app_name = "products"
urlpatterns = [
    path('', product_list_view, name="product_list"),
    path('create/', product_create_view, name="product_create"),
    path('<int:id>/', product_detail_view, name="product_detail"),
    path('<int:id>/edit', product_edit_view, name="product_edit"),
    path('<int:id>/buy', product_buy_view, name="product_buy"),
    path('<int:id>/delete', product_delete_view, name="product_delete")
]