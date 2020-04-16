import http.client

def population(country) :
	conn = http.client.HTTPSConnection("world-population.p.rapidapi.com")

	headers = {
	    'x-rapidapi-host': "world-population.p.rapidapi.com",
	    'x-rapidapi-key': "f1e4ff9f6amsh88d6e4b7ba4478ap1eabc0jsne03f4d7e0136"
	    }

	conn.request("GET", "/population?country_name={}".format(country), headers=headers)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8")) 