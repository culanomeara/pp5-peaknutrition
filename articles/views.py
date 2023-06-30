from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages

from .models import Article
from .forms import ArticleForm


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


@login_required
def add_article(request):
    """ Add an article to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.slug = slugify(article.title)
            article = form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('article_detail', args=[article.slug]))
        else:
            messages.error(request, 'Failed to add article')
    else:
        form = ArticleForm()

    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, slug):
    """ Edit a article in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.slug = slugify(article.title)
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('article_detail', args=[article.slug]))
        else:
            messages.error(request, 'Failed to update article')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.title}')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, slug):
    """ Delete an article from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, slug=slug)
    article.delete()
    messages.success(request, 'Article deleted!')
    return redirect(reverse('articles'))
