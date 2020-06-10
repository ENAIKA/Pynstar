from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'^$',views.welcome,name = "welcome"),
    # url(r'home/',views.landing,name = "landingpage"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photo/(\d+)',views.photo,name ='photo'),
    url(r'^uploadphoto/(\d+)',views.uploadphoto,name ='uploadphoto'),
    url(r'^photos/',views.allphotos,name ='allphotos'),
    url(r'^userprofile/(?P<user_id>[0-9]+)',views.userprofile,name ='userprofile'),
    url(r'^today/$',views.today_posts,name='newpics'),
    url(r'updateprofile/(?P<user_id>[0-9]+)/',views.updateprofile,name='updateprofile'),
    # url(r'photo/(\d+)/like',PostLikedToggle.as_view(), name="like_toggle"),
    url(r'photo/(?P<user_id>[0-9]+)/like', views.increment_counter, name='liked'),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.registerPage, name="django_registration_register"),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='change-password.html'),name='password_reset'), 
    # path('change_password/', auth_views.PasswordChangeView.as_view(),name='password_reset'),
    # path('change_password/',PasswordChangeView.as_view(),name='password_reset')
    url(r'login/',views.login_view,name="login"), 

]
 
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)