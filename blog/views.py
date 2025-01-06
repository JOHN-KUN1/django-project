from django.shortcuts import render
from .models import Blogs
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.

# def post_page(request):
#     context = {
#         'posts':Blogs.objects.all()
#     }
#     return render(request,'post/blog_home.html', context)
@method_decorator(login_required(login_url='/users/login'),name='dispatch')
class PostListView(ListView):
    model = Blogs
    template_name = 'blog/blog_home.html'
    context_object_name = 'posts'
    ordering = ["-date"]
@method_decorator(login_required(login_url='/users/login'),name='dispatch')

class PostDetailView(DetailView):
    model = Blogs

@method_decorator(login_required(login_url='/users/login'),name='dispatch')
class PostCreateView(CreateView):
    model = Blogs
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
@method_decorator(login_required(login_url='/users/login'),name='dispatch')
class PostUpdateView(UpdateView):
    model = Blogs
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
class PostDeleteView(DeleteView):
    model = Blogs
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
