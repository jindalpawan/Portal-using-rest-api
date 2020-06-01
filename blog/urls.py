from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('post/show/', views.AllPosts.as_view(), name='showPosts'),
    path('post/create/', views.CreatePost.as_view(), name='createPosts'),
    path('post/deletepost/<int:pk>/', views.DeletePost.as_view(), name='deletepost'),
    path('users/login/', views.AuthViewSet.as_view({'post': 'login'})),
    path('users/logout/', views.AuthViewSet.as_view({'get': 'logout'})),
    path('users/register/', views.AuthViewSet.as_view({'post': 'register'})),
]