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



def sortdata(data, sortfield) :
	if sortfield in [ "total", "critical", "active", "recovered"] :
		return sorted(data, key=lambda item: item["cases"][sortfield],reverse=True)
	elif sortfield  ==  "deaths" :
		return sorted(data, key=lambda item: item["deaths"]["total"],reverse=True)
	else :
		return sorted(data, key=lambda item: item["country"],reverse=False)



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
	sortbin = []
	
	if "sortfield" in request.POST :
		sortfield = request.POST["sortfield"]
		result["sort_select"] =  sortfield
	elif "sort_select" in request.POST :
		sortfield = request.POST["sort_select"]
		result["sort_select"] =  sortfield
	else :
		sortfield = "total"


	for x in sortdata(data,sortfield) :
		
		try:
			x["cdata"] = Countries.objects.get(name=x["country"])
		except:
			x["cdata"] = quick_check(x["country"])

		sortbin.append(x)


	if sortfield == "population" :
		result["sorted"] = sorted(sortbin, key=lambda sortbin: sortbin["cdata"].population,reverse=True)
	else :
		result["sorted"] = sortbin	
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

	if "synch_data" in request.POST:
		API.update_state_data()

	if "state_select" in request.POST:
		state = request.POST["state_select"]
	else :
		state = "OR"

	result["state"] = state

	data = API.state(state)
	result["states"] = States.objects.all().order_by("abbrev")
	result["current"] = data
	result["chart"] = API.to_chart()


	if "sortfield" in request.POST :
		sortfield = request.POST["sortfield"]
		result["sort_select"] =  sortfield
	elif "sort_select" in request.POST :
		sortfield = request.POST["sort_select"]
		result["sort_select"] =  sortfield
	else :
		sortfield = "deaths"





	result["latest"] = API.latest_state_data(sortfield)

	return  render(request,'dash2.html',context=result)




class Chart2Data(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, state, format=None):
		dataset = CAS()
		data= dataset.state(state)
		return Response(data)
