from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('post/show', views.AllPosts.as_view({'GET': 'showpost'}), name='showPosts'),
    path('post/deletepost/<int:pk>/', views.AllPosts.as_view({'POST': 'deletepost'}), name='deletepost'),
    path('users/login/', views.AuthViewSet.as_view({'post': 'login'})),
    path('users/logout/', views.AuthViewSet.as_view({'get': 'logout'})),
    path('users/register/', views.AuthViewSet.as_view({'post': 'register'})),
]