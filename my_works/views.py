from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Work


class Home(ListView):
    model = Work
    template_name = "myworkssite/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My Works"
        return context

    def get_queryset(self):
        return Work.objects.filter(draft=False)

class Detail(DetailView):
    model = Work
    template_name = "myworkssite/detail.html"
    context_object_name = "my_obj"
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_success_url(self):
        return reverse('my_works_detail', kwargs={'url': self.object.url})


