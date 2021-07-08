from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Blog
from .forms import ReviewForm


class Home(ListView):
    model = Blog
    template_name = "blogsite/index.html"
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blogs"
        return context

    def get_queryset(self):
        return Blog.objects.filter(draft=False)


class Detail(DetailView):
    model = Blog
    template_name = "blogsite/detail.html"
    context_object_name = "blog_obj"
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'url': self.object.url})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class AddReview(View):
    def post(self, request, url):
        blog = Blog.objects.get(url=url)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.blog = blog
            form.save()
            messages.info(request, "✔️ Ваш комментарий был успешно написан, после проверки администрацией  он будет добавлен!")
        return redirect("blog:blog_home")