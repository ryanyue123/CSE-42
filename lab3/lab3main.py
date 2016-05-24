#RYAN YUE
#69858941

import lab3_API_handler
import lab3_output

def get_user_input_locations():
	"""Prompts the user for the number of locations in the trip. Asks the user to specify each location and adds it to a list"""

	location_list = []
	input1 = input("")
	num_locations = int(input1)
	for i in range(num_locations):
		input2 = input("")
		location_list.append(input2)
	return location_list

def get_user_input_outputs():
	"""Prompts the user for the outputs that will be printed. Returns a list of options that the user entered"""

	output_list = []
	input3 = input("")
	num_outputs = int(input3)
	for i in range(num_outputs):
		input4 = input("")
		output_list.append(input4)
	print("")
	return output_list

def handle_json(location_list: list):
	"""Takes a list of the locations, and sends a request to MAPQUEST to get the corresponding json information about the
	trip. Returns the json response as a dictionary"""

	url = lab3_API_handler.build_directions_url(location_list)
	return lab3_API_handler.get_results(url)

def print_output(outputs: list) -> None:
	"""Takes in a list of the desired outputs and prints out the corresponding information. Prints the MapQuest copyright statement"""
	for i in outputs:
		i.get_output()
	print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")

def check_route(json_response: dict) -> bool:
	"""Checks to see if a route exists. If route exists, returns True. Otherwise, prints the error message and returns False"""
	if (json_response["info"]["statuscode"] == 0):
		return True
	else:
		print("NO ROUTE FOUND")
		return False

def handle_output(output_list: list, json_response: dict) -> None:
	"""Takes in a list of strings, representing the desired output fields. Creates an object for each desired output, initialized with the json data,
	 and prints the resulting output string"""

	outputs = []
	if (check_route(json_response)):
		for i in output_list:
			output_class = eval("lab3_output." + i)
			outputs.append(output_class(json_response))
		print_output(outputs)

if __name__ == '__main__':
	location_list = get_user_input_locations()
	output_list = get_user_input_outputs()
	json_response = handle_json(location_list)
	if json_response != None:
		handle_output(output_list, json_response)
	else:
		print("MAPQUEST ERROR")