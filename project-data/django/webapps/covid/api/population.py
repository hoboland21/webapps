import http.client
from covid.models import *
import json
import urllib.parse
class PopulationApi(object) :
	def __init__(self) :

		self.conn = http.client.HTTPSConnection("world-population.p.rapidapi.com")

		self.headers = {
		    'x-rapidapi-host': "world-population.p.rapidapi.com",
		    'x-rapidapi-key': "f1e4ff9f6amsh88d6e4b7ba4478ap1eabc0jsne03f4d7e0136"
		    }

	def population(self,country) : 

		self.conn.request("GET", "/population?country_name={}".format(country), headers=self.headers)
		res = self.conn.getresponse()
		data = json.loads(res.read())
		return data

	def loadDB(self) :
		Countries.objects.all().delete()
		self.conn.request("GET", "/allcountriesname", headers=self.headers)
		res = self.conn.getresponse()
		data = json.loads(res.read())
		for d in data["body"]["countries"] :
			self.conn.request("GET", "/population?country_name={}".format(urllib.parse.quote_plus(d)), headers=self.headers)
			res2 = self.conn.getresponse()
			data2 = json.loads(res2.read())
			country = Countries.objects.create(name=data2["body"]["country_name"], population=data2["body"]["population"], 
				ranking=data2["body"]["ranking"] )
			country.save()


'''
conn.request("GET", "/allcountriesname", headers=headers)


conn.request("GET", "/population?country_name=Mexico", headers=headers)


conn.request("GET", "/worldpopulation", headers=headers)


def initialize_state_db() :
    States.objects.all().delete()
    for s in STATES :
        state = States.objects.create(abbrev=s )
        state.save()
    for s in STATE_NAMES :
        smodel = States.objects.get(abbrev=s[0])
        smodel.name = s[1]
        smodel.save()
    for s in state_links :
        smodel = States.objects.get(abbrev=s[1])
        smodel.url = s[0]
        smodel.save()

'''