from rest_framework import serializers
from rest_framework.response import Response
from card.models import carddetails
from likes.models import likecount

class likecountSerializer(serializers.ModelSerializer):
	class Meta:
		model = likecount
		fields= '__all__'

class CardSerializer(serializers.ModelSerializer):
#	x = likecountSerializer(many=True)
	class Meta:
		model = carddetails
		fields = [
		'pk',
		'model_pic',
		'user' ,
		'title' ,
		'description', 
		'pub_date',
		'private',
#		'x',
		]
		read_only_fields=['user']


	#def to_representation(self):
	#	context = self.