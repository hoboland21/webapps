from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse
from .api.covidapi import CovidApi as CA
from .api.stateapi import CovidStateApi as CAS

# Create your views here.


STATES= ["AK","AL","AR","AZ","CA","CO","CT","DC",
"DE","FL","GA","HI","IA","ID","IL","IN",
"KS","KY","LA","MA","MD","ME","MI","MN",
"MO","MS","MT","NC","ND","NE","NH","NJ",
"NM","NV","NY","OH","OK","OR","PA","PR",
"RI","SC","SD","TN","TX","UT","VA","VT",
"WA","WI","WV","WY"]



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

	if "all_state_select" in request.POST:
		alldata = API.all_states()

	data = API.state(state)
	result["STATES"] = STATES
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
