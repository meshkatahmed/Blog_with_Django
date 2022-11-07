from django.urls import path
from . import views
app_name = 'blog_app'
urlpatterns = [
    path('',views.BlogList.as_view(),name='bloglist'),
    path('write/',views.CreateBlog.as_view(),name='createblog'),
    path('details/<slug>/',views.blog_details,name='blogdetails'),
    path('liked/<pk>/',views.liked,name='likedpost'),
    path('unliked/<pk>/',views.unliked,name='unlikedpost'),
]
