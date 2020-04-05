import http.client
import json
from datetime import datetime as dt


class CovidApi(object) :
	def __init__(self) :
		self.conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")
		self.headers = {
    		'x-rapidapi-host': "covid-193.p.rapidapi.com",
    		'x-rapidapi-key': "f1e4ff9f6amsh88d6e4b7ba4478ap1eabc0jsne03f4d7e0136"
    	}

	def countries(self) :
		self.conn.request("GET", "/countries", headers=self.headers)
		res = self.conn.getresponse()
		data = json.loads(res.read())
#		print(data.decode("utf-8"))
		return data

	def current(self) :
		self.conn.request("GET", "/statistics", headers=self.headers)
		res = self.conn.getresponse()
		data = json.loads(res.read())
#		print(data.decode("utf-8"))
		return data

	def date_prep(self,datestr) :
		d = dt.strptime(datestr[:-6],"%Y-%m-%dT%H:%M:%S")
		return int(d.timestamp() / (3600 * 24))


	def chart_prep(self) :
		data_clean = {}

		for d in self.data["response"] :
#			t = self.date_prep(d["time"])
			t = d["day"]
			try:
				data_clean[t].append(d)
			except:
				data_clean[t] = []
				data_clean[t].append(d)

		return data_clean


	def to_chart(self) :
		cp = self.chart_prep()
		result = {"all":[],"newdeaths":[],
			"recovered":[],"deaths":[],
			"critical":[],"labels":[], "barcolor":[]}
		for k in sorted(cp.keys()) :
			nd = cp[k][0]['deaths']['new']
			try: 
				ndeath = int(nd)
			except:
				ndeath=0

			result["newdeaths"].append(ndeath)
			result["barcolor"].append("orange")
			result["deaths"].append(cp[k][0]['deaths']['total'])
			result["critical"].append(cp[k][0]['cases']['critical'])
			result["recovered"].append(cp[k][0]['cases']['recovered'])
			result["labels"].append(cp[k][0]['day'])
			result["all"].append(cp[k])
		result["country"] = self.country	
		return result


	def history(self,country) :
		self.country = country
		self.conn.request("GET", "/history?country={}".format(country), headers=self.headers)
		res = self.conn.getresponse()
		self.data = json.loads(res.read())
		self.chart_prep()
		return self.data
