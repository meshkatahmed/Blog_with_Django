from django.urls import path
from . import views
app_name = 'blog_app'
urlpatterns = [
    path('',views.blog_list,name='bloglist'),
    path('write/',views.CreateBlog.as_view(),name='createblog'),
]
