from django.shortcuts import render, get_object_or_404
from django.views.generic import (
CreateView,
DetailView,
ListView,
UpdateView,
DeleteView
)
from django.urls import reverse
from .forms import ArticleModelForm
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'blog/article_form.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_form.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article_list')
