from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name= 'login_app'

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('userprofilechange/',views.user_profile_change,name='changeprofileinfo'),
    path('password/',views.pass_change,name='passwordchange'),
    path('profilepicchange/',views.profile_pic_change,name='profilepicchange'),
]

urlpatterns += staticfiles_urlpatterns()
