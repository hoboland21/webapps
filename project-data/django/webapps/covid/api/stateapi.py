import http.client
import json
from datetime import datetime as dt
from datetime import date
from covid.models  import States, StateData
import urllib.request


def intcheck(val) :
	try :
		result = int(val)
	except :
		result = 0
	return result



class CovidStateApi(object) :
	def __init__(self) :
		self.states=States.objects.all().order_by("abbrev")
	
	def state(self,state) :
		fp = urllib.request.urlopen("http://coronavirusapi.com/getTimeSeriesJson/{}".format(state))
		self.data = json.loads(fp.read())
		fp.close()
		self.state = state
		return self.to_chart()


	def update_state_data(self) :
		for s in self.states :
			fp = urllib.request.urlopen("http://coronavirusapi.com/getTimeSeriesJson/{}".format(s.abbrev))
			recs = json.loads(fp.read())
			fp.close()
			curr_recs = StateData.objects.filter(states=s)
			for r in recs :
				if not curr_recs.filter(timestamp=r["seconds_since_epoch"])  :
					sd = StateData.objects.create(
						states=s, 
						timestamp=intcheck(r["seconds_since_epoch"]),
						positive=intcheck(r["positive"]),
						tested=intcheck(r["tested"]),
						deaths=intcheck(r["deaths"]) )
					sd.save()
	
	def latest_state_data(self,sortfield) :
		result= []
		
		for state in self.states :
			d = StateData.objects.filter(states=state).order_by("-timestamp")
			lastrec = d[0]
			lastrec.time = dt.fromtimestamp(lastrec.timestamp)
			result.append(lastrec) 
		if sortfield in ["death","positive","tested"] :
			return  sorted(result, key=lambda result: getattr(result,sortfield),reverse=True)
		else :
			return result
		


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
