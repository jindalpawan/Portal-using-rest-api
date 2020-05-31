from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
	path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
]
