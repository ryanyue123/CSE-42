dict = {
	1: ["B", "F", "P", "V"],
	2: ["C", "G", "J", "K", "Q", "S", "X", "Z"],
	3: ["D", "T"],
	4: ["L"],
	5: ["M", "N"],
	6: ["R"],
}

def remove_double_number_letters(name: str):
	for letter in range(len(name)-1):
