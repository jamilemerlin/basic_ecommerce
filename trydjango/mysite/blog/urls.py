from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('create/', ArticleCreateView.as_view(), name="article_create"),
    path('<int:id>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:id>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article_delete")
]