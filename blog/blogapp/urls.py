from django.urls import path

from blogapp import views

urlpatterns = [
    path('home/', views.HomePageView, name = 'home'),
    path('post/new/', views.PostCreateView, name = 'post_new'),
    path('post/<slug:slug>', views.PostDetailView, name = 'post'),

]