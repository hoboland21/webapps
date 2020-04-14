import http.client
import json
from datetime import datetime as dt
from datetime import date
from covid.models  import States
import urllib.request

class CovidStateApi(object) :
	def __init__(self) :
		self.states=States.objects.all().order_by("abbrev")
	
	def state(self,state) :
		fp = urllib.request.urlopen("http://coronavirusapi.com/getTimeSeriesJson/{}".format(state))
		self.data = json.loads(fp.read())
		fp.close()
		self.state = state
		return self.to_chart()


	def date_prep(self,datestr) :
		d = dt.strptime(datestr[:-6],"%Y-%m-%dT%H:%M:%S")
		return int(d.timestamp() / (3600 * 24))


	def chart_prep(self) :
		data_clean = {}

		for d in self.data :
			t_epoch = d["seconds_since_epoch"]
			t = date.fromtimestamp(t_epoch).isoformat()
			try:
				data_clean[t].append(d)
			except:
				data_clean[t] = []
				data_clean[t].append(d)


		return data_clean



	def to_chart(self) :
		cp = self.chart_prep()
		result = {"all":[],"labels":[],"tested":[],"positive":[],"deaths":[]}
		for k in sorted(cp.keys()) :
			result["labels"].append(k)
			result["tested"].append(cp[k][0]["tested"]) 
			result["positive"].append(cp[k][0]["positive"]) 
			d = cp[k][0]["deaths"]
			if cp[k][0]["deaths"] == None :
				d = 0
			result["deaths"].append(d)
		result["state"]=self.state
		result["state_name"]=self.states.get(abbrev=self.state).name

		return result
