from django.shortcuts import render, redirect, get_list_or_404
from card.models import carddetails
from django.utils import timezone
from django.views.decorators.http import require_POST
from comment.models import commentcount, Reply
from likes.models import likecount
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import CardSerializer



class CardSerializerView(generics.ListAPIView):
	lookup_field= 'pk'
	serializer_class = CardSerializer
	def get_queryset(self):
		context =carddetails.objects.all()
		return context

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
		
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if not serializer.is_valid(raise_exception=False):
			context = {"success": "False",
				"message": "New Card Could not be created",
				"error": "Error 202",
				"data":"N/A"}
			return Response(context)
		self.perform_create(serializer)
		context = {"Success": "True",
			"message": "Data Created",
			"error": "",
			"data":serializer.data}
		return Response(context)