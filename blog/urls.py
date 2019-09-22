from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.home, name='blog-page'),
    path('about/', views.about, name='blog-about')
]
