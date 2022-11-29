from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


def news(request):
    data = {
        'article': Article,
    }
    return render(request, 'news/news.html', data)


class ShowNewsView(ListView):
    model = Article
    template_name = 'news/news.html'
    context_object_name = 'article'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Новости'
        return ctx


class NewsDetailView(DetailView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = Article.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'image', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateNewsView, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CreateNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Новая статья'
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'image', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UpdateNewsView, self).form_valid(form)

    def test_func(self):
        # article = self.get_object()
        # if self.request.user == article.author:
        if self.request.user.is_staff:
            return True
        return False

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(UpdateNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Редактирование статьи'
        return ctx


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/news'

    def test_func(self):
        # article = self.get_object()
        # if self.request.user == article.author:
        if self.request.user.is_staff:
            return True
        return False
