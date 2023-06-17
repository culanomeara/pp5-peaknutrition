from django.shortcuts import render, get_object_or_404

from .models import Article


def all_articles(request):
    """
    Article view
    """
    articles = Article.objects.all()

    return render(
        request,
        "articles/articles.html",
        {
            "articles": articles,
        },
    )


def article_detail(request, slug):
    """
    Article Detail view
    """
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "articles/article_detail.html",
        {
            "article": article,
        },
    )
