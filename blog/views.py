from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated

class HomePage(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		posts= Post.objects.all().order_by('create_date').reverse()
		if posts:
			serialize= PostSerializer(posts, many=True)
			return Response(serialize)
		data={'Error': "No posts"}
		return Response(data)


