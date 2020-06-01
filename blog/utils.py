from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

def get_and_authenticate_user(email, password):
	user = authenticate(username=username, password=password)
	if user is None:
		raise serializers.ValidationError("Invalid username/password. Please try again!")
	return user


def create_user_account(email,username, password, first_name="",last_name=""):
    user = User.objects.create_user(email=email,username=username, password=password, first_name=first_name,last_name=last_name)
    return user