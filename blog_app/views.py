from django.shortcuts import render
from django.views.generic import View,CreateView,UpdateView,ListView,DetailView,TemplateView,DeleteView
from .models import Blog,Comment,Like
from .forms import CommentForm
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

@login_required
def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Like.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked=True
    else:
        liked=False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_app:blogdetails',kwargs={'slug':slug}))
    return render(request,'blog_app/blogdetails.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})

@login_required
def liked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog,user=user)
    if not already_liked:
        like_post = Like(blog=blog,user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('blog_app:blogdetails',kwargs={'slug':blog.slug}))

@login_required
def unliked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog_app:blogdetails',kwargs={'slug':blog.slug}))
