from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse
from .api.covidapi import CovidApi as CA
from .api.stateapi import CovidStateApi as CAS
from .api.stateapi import STATE_NAME_DICT
from .api.state import STATES, STATE_NAMES, state_links
# Create your views here.




def dashboard(request) :
	result = {}
	test = CA()

	if "country_select" in request.POST:
		country = request.POST["country_select"]
	else :
		country = "All"
	result["country"] = country

	data = test.current()["response"]
	
	result["current"] = data
	result["sorted"] = []

	for x in sorted(data, key=lambda item: item["cases"]["total"],reverse=True):
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
	result["state_name"] = STATE_NAME_DICT[state]

	if "all_state_select" in request.POST:
		alldata = API.all_states()

	data = API.state(state)
	result["states"] = STATE_NAMES
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
