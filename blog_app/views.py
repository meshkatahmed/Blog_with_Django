from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request,'blog_app/bloglist.html',context={})
