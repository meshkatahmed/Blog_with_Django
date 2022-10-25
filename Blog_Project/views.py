from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return HttpResponseRedirect(reverse('blog_app:bloglist'))
