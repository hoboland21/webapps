from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse
from .api.covidapi import CovidApi as CA

# Create your views here.


def dashboard(request) :
	result = {}

	test = CA()
#	result["countries"] = test.countries()
	
	data = test.current()["response"]
	
	result["current"] = data
	result["sorted"] = []
	for x in sorted(data, key=lambda item: item["cases"]["total"],reverse=True):
		result["sorted"].append(x)

	if "country_select" in request.POST:
		country = request.POST["country_select"]
		result["highlight"] = country
		result["hidata"] =test.history(country)
	return  render(request,'dashboard.html',context=result)


class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, country, format=None):
		dataset =  CA()

		dataset.history(country)
		data = dataset.to_chart()

#		data = { 
#			"all": dataset.data,
#			"deaths": dataset.deaths,
#			"critical":dataset.critical,
#			"cases":dataset.cases,
#			"labels":dataset.labels
#			}

		return Response(data)