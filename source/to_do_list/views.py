from django.shortcuts import render, get_object_or_404, redirect
from to_do_list.models import Article
from to_do_list.validate_char_field import article_validate
from to_do_list.forms import ArticleForm
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        articles = Article.objects.all()
        context = {'articles': articles}
        return context

class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs.get('pk'))
        return context


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)

        if form.is_valid():
            status = form.cleaned_data['status'].get()
            type = form.cleaned_data['type'].get()
            article = Article.objects.create(
                description=form.cleaned_data.get('description'),
                detailed_description=form.cleaned_data.get('detailed_description'),
                status=status,
                type=type,
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', {'form': form})



class ArticleUpdateView(TemplateView):
    template_name = 'article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        form = ArticleForm(initial={
            'description': article.description,
            'detailed_description': article.detailed_description,
            'created_at': article.created_at,
            'status': article.status,
            'type': article.type
        })
        context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.description = form.cleaned_data.get('description')
            article.detailed_description = form.cleaned_data.get('detailed_description')
            article.created_at = form.cleaned_data.get('created_at')
            article.status = form.cleaned_data['status'].first()
            article.type = form.cleaned_data['type'].first()

            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_update.html', {'form': form})


class ArticleDeleteView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return render(request, 'article_delete.html', {'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        article.delete()
        return redirect('index')

