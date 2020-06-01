from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from blog import views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginn/', obtain_auth_token, name='login'),
    #url(r'^', include(router.urls)),
    path('', include('blog.urls')),
    #path('registration/', include('rest_auth.registration.urls')),


]
