from django.urls import path, include

from . import views

app_name = "authTest"
urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name = "logout"),
    path('login/', views.login, name = 'login'),
    path('sign-up/', views.sign_up, name = "sign_up"),
    path('create-post/', views.create_post, name = 'create-post'),
    

]