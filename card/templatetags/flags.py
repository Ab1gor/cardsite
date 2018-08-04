from django import template
from django.template import Library

register = Library()

def flags(value):
	data =value
	return data

register.filter('flags',flags)