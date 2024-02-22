from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import TemplateView ,RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
# Create your views here.


# Function Base view show a templates
'''
def indexView(request):
    """
    a funcation based view to show index page
    """
    name ="ali"
    context = {"name":name}
    return render(request,"index.html",context)
'''


class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context
    
'''FBV for redirect
from django.shortcuts import redirect
def redirectToDjango(request):
    return redirect('https://www.djangoproject.com')
'''

class RedirectToDjango(RedirectView):
    url = "https://www.djangoproject.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

class Postlist(ListView):
    model = Post
    #queryset = Post.objects.all()
    paginate_by = 2
    context_object_name = 'posts'
    ordering = 'id'

    #def get_queryset(self):
       # posts = Post.objects.filter(status=True) 
        #return posts


