from itertools import chain
from django.shortcuts import render
from django.views.generic import ListView
from .models import Architecture, Style, Architector


## ARCHITECTURE
class Home(ListView):
    model = Architecture
    template_name = "architecturesite/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home Of Architecture"
        return context

    def get_queryset(self):
        return Architecture.objects.filter(draft=False)


def arch_detail(request, url):
    arch_obj = Architecture.objects.get(url=url)
    return render(request, "architecturesite/arch_detail.html", {"arch_obj":arch_obj})
## ENDARCHITECTURE


### STYLES
def styles(request):
    styles = Style.objects.filter(draft=False)
    return render(request, "architecturesite/styles.html", {"styles":styles})

def style_detail(request,url):
    style_obj = Style.objects.get(url=url)
    return render(request, "architecturesite/style_detail.html", {"style_obj":style_obj})
### ENDSTYLES

### ARCHITECTORS
def architectors(request):
    architectors = Architector.objects.filter(draft=False)
    return render(request, "architecturesite/architectors.html", {"architectors": architectors})

def architector_detail(request, url):
    style_obj = Style.objects.get(url="rokoko")
    architector_obj = Architector.objects.get(url=url)
    return render(request, "architecturesite/architector_detail.html", {"architector_obj": architector_obj, "style_obj":style_obj})
## ENDARCHITECTORS


### SEARCH
class Search(ListView):
    template_name = "architecturesite/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("s")
        architectures = Architecture.objects.filter(title__contains=query, draft=False)
        styles = Style.objects.filter(name__contains=query, draft=False)
        architectors = Architector.objects.filter(name__contains=query, draft=False)

        return {"architectures": architectures, "styles": styles, "architectors": architectors}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["s"] = f"s={self.request.GET.get('s')}"
        return context
