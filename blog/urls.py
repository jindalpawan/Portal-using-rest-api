from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('allposts/', views.AllPosts.as_view(), name='AllPosts'),
    path('deletepost/<int:pk>/', views.DeletePost.as_view(), name='deletepost'),
    path('users/login/', views.AuthViewSet.as_view({'post': 'login'})),
    path('users/logout/', views.AuthViewSet.as_view({'post': 'logout'})),
    path('users/register/', views.AuthViewSet.as_view({'post': 'register'})),
]