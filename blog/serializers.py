from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields =['title', 'author', 'content', 'crate_date']


class AuthUserSerializer(serializers.ModelSerializer):
	auth_token = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = ('id','username' ,'email', 'first_name', 'last_name','auth_token')

	def get_auth_token(self, obj):
		Token.objects.filter(user=obj).delete()
		token = Token.objects.create(user=obj)
		return token.key


class EmptySerializer(serializers.Serializer):
	pass



class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username', 'email', 'password', 'first_name', 'last_name')

	def validate_data(self, value):
		user = User.objects.filter(email=email)
		if user:
			raise serializers.ValidationError("Email is already taken")

		u = User.objects.filter(username=username)
		if u:
			raise serializers.ValidationError("Username is already taken")
