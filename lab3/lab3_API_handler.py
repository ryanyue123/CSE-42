#RYAN YUE
#69858941

import json
import urllib.parse
import urllib.request

API_KEY = "yPtTxu7w5XkuTtMltrV7wYE4dGZu9YSM"
MAPQUEST_URL_BASE = "http://open.mapquestapi.com/"

def build_directions_url(location_list: list) -> str:
	"""Builds a url that consists of the desired parameters for routing. This includes the all the locations in the trip"""

	url = MAPQUEST_URL_BASE + "directions/v2/route?"
	query_parameters = [("key", API_KEY), ("outFormat", "json"), ("unit", "m")]
	for i in range(len(location_list)):
		if (i == 0):
			query_parameters.append(("from", location_list[0]))
		else:
			query_parameters.append(("to", location_list[i]))
	return _build_url(url, query_parameters)

def build_elevation_url(latitude: float, longitude: float) -> str:
	"""Builds a url that is used to retrieve the elevation of a location based on latitude and longitude"""

	url = MAPQUEST_URL_BASE + "elevation/v1/profile?"
	query_parameters = [("key", API_KEY), ("outFormat", "json"), ("latLngCollection", str(latitude) + "," + str(longitude))]
	return _build_url(url, query_parameters)

def _build_url(url_base: str, query_parameters: list) -> str:
	"""returns the url and the query parameters in proper url format"""

	return url_base + urllib.parse.urlencode(query_parameters)

def get_results(url: str) -> dict:
	"""Requests a response with the given url. Converts the response string into json format"""

	response = None
	try:
		response = urllib.request.urlopen(url)
		json_text = response.read().decode(encoding = 'utf-8')
		return json.loads(json_text)
	except:
		return response
	finally:
		if response != None:
			response.close()