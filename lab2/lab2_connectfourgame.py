#Ryan Yue 69858941
#Hubert Cheng 12885496

import connectfour

def getUserInput():
	"""Asks the user for their input on which column to drop or pop and keeps on prompting
	the user if it is invalid. Returns the action and col_num as two different strings"""

	while(True):
		user_input = input("Enter DROP or POP followed by a column number (1-7): ")
		try:
			action, col_num = stringToAction(user_input)
			if (action == "DROP" or action == "POP"):
				if (col_num <= connectfour.BOARD_COLUMNS and col_num >= 1):
					return action, col_num
		except:
			pass
		print("Please enter a valid move")

def stringToAction(input_str: str):
	"""Takes in the user input string and breaks it up into two strings: action and col_num"""

	action = input_str[:input_str.index(" ")].upper()
	col_num = eval(input_str[input_str.index(" ") + 1:])
	return action, col_num


def printBoard(gamestate: connectfour.GameState):
	"""Takes in the gamestate and prints out the board with ., R, or Y depending on the gamestate"""

	print("\n")
	for i in range(1,connectfour.BOARD_COLUMNS+1):
		print(i, end="\t")
	print("\n")	
	for i in range(connectfour.BOARD_ROWS):
		for j in range(connectfour.BOARD_COLUMNS):
			position = gamestate.board[j][i]
			if (position == 0):
				print(".", end="\t")
			elif (position == 1):
				print("R", end="\t")
			else:
				print("Y", end="\t")
		print("\n")

def checkMove(gamestate: connectfour.GameState, choice: str, col_num: str):
	"""Takes in the user"s choice and see if the move is valid by calling drop or pop from connectfour
	If no expection is raised when checking the move then it will return True otherwise False"""

	if choice == "DROP":
		try:
			connectfour.drop(gamestate, col_num-1)
			return True
		except connectfour.InvalidMoveError:
			return False
	elif choice == "POP":
		try:
			connectfour.pop(gamestate, col_num-1)
			return True
		except connectfour.InvalidMoveError:
			return False
	return False

def makeMove(gamestate: connectfour.GameState, choice: str, col_num: str):
	"""If a valid move was made then the gamestate with the completed move will be returned"""

	if (checkMove(gamestate, choice, col_num)):
		if choice == "DROP":
			return connectfour.drop(gamestate, col_num-1)
		elif choice == "POP":
			return connectfour.pop(gamestate, col_num-1)
	else:
		return gamestate

def checkWin(gamestate: connectfour.GameState):
	"""Checks the current gamestate to see if anybody has won and accordingly return the boolean to
	state the current game situtation"""

	if (connectfour.winner(gamestate) == 0):
		return True
	return False

def printWinner(gamestate: connectfour.GameState):
	""" Prints out the winner or tie if the game comes to an end"""

	if (connectfour.winner(gamestate) == 1):
		print("WINNER: RED")
	elif (connectfour.winner(gamestate) == 2):
		print("WINNER: YELLOW")
	else:
		print("TIE")
	print("Thanks for playing!")
