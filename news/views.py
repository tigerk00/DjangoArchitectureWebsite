from django.views.generic import ListView, DetailView
from .models import News


class Home(ListView):
    model = News
    template_name = "newssite/index.html"
    context_object_name = "news"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "News"
        return context

    def get_queryset(self):
        return News.objects.filter(draft=False)

class Detail(DetailView):
    model = News
    template_name = "newssite/detail.html"
    context_object_name = "news_obj"
    slug_field = 'url'

    def get_object(self, queryset=None):
        return News.objects.get(url=self.kwargs.get("url"))



