from django.shortcuts import render
from django.views.generic import View,CreateView,UpdateView,ListView,DetailView,TemplateView,DeleteView
from blog_app.models import Blog,Comment,Like
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.
class CreateBlog(CreateView,LoginRequiredMixin):
    model = Blog
    fields = ['blog_title','blog_content','blog_image']
    template_name = 'blog_app/createblog.html'

    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))

class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog_app/bloglist.html'
    #queryset = Blog.objects.order_by('-publish_date')
