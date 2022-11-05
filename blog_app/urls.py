from django.urls import path
from . import views
app_name = 'blog_app'
urlpatterns = [
    path('',views.BlogList.as_view(),name='bloglist'),
    path('write/',views.CreateBlog.as_view(),name='createblog'),
]
