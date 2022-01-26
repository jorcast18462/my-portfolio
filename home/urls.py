from django.urls import path 
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('portfolio/', views.portfolio, name='portfolio'),

    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>/', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),

    path('send_email/', views.sendEmail, name='send_email'),
]
