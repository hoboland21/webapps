from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse
from .api.covidapi import CovidApi as CA
from .api.stateapi import CovidStateApi as CAS
from .api.population import PopulationApi as POP

from covid.models import *


# Create your views here.

fix_dict = {
	"USA":"United States",
	"UK":"United Kingdom",
	"S-Korea":"South Korea",
	"Saudi-Arabia":"Saudi Arabia",
	"Czechia" : "Czech Republic (Czechia)",
	"UAE" : "United Arab Emirates",
	"Dominican-Republic":"Dominican Republic",
}
def quick_check(country) :
	cdata = Countries()
	if country in fix_dict :
		cdata = Countries.objects.get(name=fix_dict[country])
	return cdata

def dashboard(request) :
	result = {}
	test = CA()

	if "load_country_db" in request.POST:
		population =  POP()
		population.loadDB()


	if "country_select" in request.POST:
		country = request.POST["country_select"]
	else :
		country = "All"
	result["country"] = country

	data = test.current()["response"]
	
	result["current"] = data
	result["sorted"] = []

	for x in sorted(data, key=lambda item: item["cases"]["total"],reverse=True):
		
		try:
			x["cdata"] = Countries.objects.get(name=x["country"])
		except:
			x["cdata"] = quick_check(x["country"])

		result["sorted"].append(x)

	return  render(request,'dashboard.html',context=result)




class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, country, format=None):
		dataset =  CA()

		dataset.history(country)
		data = dataset.to_chart()

		return Response(data)



def dash2(request) :
	result = {}

	API= CAS()

	if "state_select" in request.POST:
		state = request.POST["state_select"]
	else :
		state = "OR"

	result["state"] = state


	data = API.state(state)
	result["states"] = States.objects.all().order_by("abbrev")
	result["current"] = data
	result["chart"] = API.to_chart()

	return  render(request,'dash2.html',context=result)




class Chart2Data(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, state, format=None):
		dataset = CAS()
		data= dataset.state(state)
		return Response(data)
