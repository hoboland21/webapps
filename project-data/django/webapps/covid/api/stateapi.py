import http.client
import json
from datetime import datetime as dt
import urllib.request


class CovidStateApi(object) :
	def __init__(self) :
		pass
	def state(self,state) :
		fp = urllib.request.urlopen("http://coronavirusapi.com/getTimeSeriesJson/{}".format(state))
		data = json.loads(fp.read())
		fp.close()
		return data

	def date_prep(self,datestr) :
		d = dt.strptime(datestr[:-6],"%Y-%m-%dT%H:%M:%S")
		return int(d.timestamp() / (3600 * 24))


	def chart_prep(self) :
		data_clean = {}

		for d in self.data :
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
			pass
		return result
