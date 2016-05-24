#RYAN YUE
#69858941
import lab3_API_handler

class STEPS:
	"""This class represents the directions from location to location in the user's trip"""
	def __init__(self, json_response: dict):
		self.json_response = json_response

	def get_output(self) -> None:
		"""Loops through the json data and returns a string that consists of all the directions to go from location to location
		in the user's trip"""

		output_string = "DIRECTIONS\n"
		for direction in (self.json_response["route"]["legs"]):
			for maneuver in (direction["maneuvers"]):
				output_string += maneuver["narrative"] +"\n"
		print(output_string)

class TOTALDISTANCE:
	"""This class represents the total distance of the trip"""
	def __init__(self, json_response: dict):
		self.json_response = json_response

	def get_output(self) -> None:
		"""Returns the total distance of the trip in miles"""

		print("TOTAL DISTANCE: " + str(round(self.json_response["route"]["distance"])) + " miles\n")

class TOTALTIME:
	"""This class represents the total time of the trip"""
	def __init__(self, json_response: dict):
		self.json_response = json_response

	def get_output(self) -> None:
		"""Returns the total time it will take to complete the trip by car in minutes"""

		print("TOTAL TIME: " + str(round(self.json_response["route"]["time"]/60)) + " minutes \n")

class LATLONG:
	"""This class represents the latitude and longitude of all the locations in the trip"""
	def __init__(self, json_response: dict):
		self.json_response = json_response

	def get_output(self) -> None:
		"""Returns the latitude and lognitude of each location in the trip. Rounds the longitude to 2 decimal places"""

		output_string = "LATLONG\n"
		for location in (self.json_response["route"]["locations"]):
			latitude = location["latLng"]["lat"]
			longitude = location["latLng"]["lng"]
			if (latitude < 0):
				output_string += str(round(latitude*-1, 2)) + "S "
			else:
				output_string += str(round(latitude, 2)) + "N "
			if (longitude < 0):
				output_string += str(round(longitude*-1, 2)) + "W "
			else:
				output_string += str(round(longitude, 2)) + "E "
			output_string += "\n"
		print(output_string)

class ELEVATION:
	"""This class represents the elevations of all locations in the trip"""
	def __init__(self, json_response: dict):
		self.json_response = json_response
		self.elevation_response = []
		for latlng in self._get_latlng_list(self.json_response):
			self.elevation_response.append(lab3_API_handler.get_results(lab3_API_handler.build_elevation_url(latlng[0], latlng[1])))

	def _get_latlng_list(self, json_response: dict) -> list:
		"""Returns a list of tuples of latitude and longitude of each location in the trip. This function provides the input
		data needed to build the elevation url"""

		latlng_list = []
		for location in (json_response["route"]["locations"]):
			latitude = location["latLng"]["lat"]
			longitude = location["latLng"]["lng"]
			latlng_list.append((latitude, longitude))
		return latlng_list

	def get_output(self) -> None:
		"""Returns the elevation of a location in feet"""
		output_string = "ELEVATIONS\n"
		for elevation in self.elevation_response:
			output_string += str(round(elevation["elevationProfile"][0]["height"] * 3.28084)) + "\n"
		print(output_string)