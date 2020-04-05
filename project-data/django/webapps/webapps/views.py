from django.shortcuts import render

# Create your views here.

def welcome(request) :
	result = {}

	return  render(request,'welcome.html',context=result)
