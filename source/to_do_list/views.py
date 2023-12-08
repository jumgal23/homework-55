from django.shortcuts import render, get_object_or_404, redirect
from to_do_list.models import Article
from to_do_list.validate_char_field import article_validate
from to_do_list.forms import ArticleForm


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article': article})


def article_create_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})
    elif request.method == "POST":
        form = ArticleForm(data=request.POST)

        if form.is_valid():
            article = Article.objects.create(
                status=form.cleaned_data.get('status'),
                description=form.cleaned_data.get('description'),
                detailed_description=form.cleaned_data.get('detailed_description'),
                created_at=form.cleaned_data.get('created_at')
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            'status': article.status,
            'description': article.description,
            'detailed_description': article.detailed_description,
            'created_at': article.created_at
        })
        return render(request, 'article_update.html', {'form': form})
    elif request.method == "POST":

        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.status = form.cleaned_data.get('status')
            article.description = form.cleaned_data.get('description')
            article.detailed_description = form.cleaned_data.get('detailed_description')
            article.created_at = form.cleaned_data.get('created_at')
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_update.html', {'form': form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
