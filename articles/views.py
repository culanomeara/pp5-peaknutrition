from django.shortcuts import render

from django.views.generic import (View,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)

from .models import Article


class all_articles(ListView):
    """
    A class for the Article List view
    """
    model = Article
    queryset = Article.objects.all()
    template_name = 'articles.html'


class article_detail(DetailView):
    """
    A class for the Article Detail view
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
            },
        )
