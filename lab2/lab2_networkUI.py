#Ryan Yue 69858941
#Hubert Cheng 12885496


import lab2_socket
import lab2_connectfourgame
import connectfour

def _prompt_For_Host():
	'''Prompts the user for the host and it returns a str that represents the host'''

	while True:
		host = input("Host: ").strip()
		if (len(host) == 0):
			print("Please specify a host (either a name or an IP address)")
		else:
			return host

def _prompt_For_Port():
	'''Prompts the user for a port and checks if the port is correct'''

	while True:
		try:
			port = int(input("Port: ").strip())
			if (port < 0 or port > 65535):
				print("Ports must be an integer between 0 and 65535")
			else:
				return port
		except ValueError:
			print("Ports must be an integer between 0 and 65535")

def _prompt_For_Username():
	'''Prompts the user for a username and makes sure that the username does not contain any spaces or have no characters'''

	while True:
		username = input("Username: ").strip()
		if (len(username) == 0 or (' ' in username) or ('\t' in username)):
			print("Please specify a valid username")
		else:
			return username

def _user_Turn(gamestate: connectfour.GameState, connection: lab2_socket.Connection):
	'''Gets the move and column number from the User and sends the move to the server.
	The gamestate is updated if the user makes a valid move'''

	action, col = lab2_connectfourgame.getUserInput()
	lab2_socket.send_message(connection, action + " " + str(col))
	if (lab2_connectfourgame.checkMove(gamestate, action, col)):
		updated_gamestate = lab2_connectfourgame.makeMove(gamestate, action, col)
		return updated_gamestate
	else:
		print("Please enter a valid move")
		return gamestate

def _process_Server_Move(connection: lab2_socket.Connection, gamestate: connectfour.GameState):
	'''Processes the server move and converts it to a string to get the action and column number
	Takes in the next server message to see if the server is ready of if a player has won. Then it updates the gamestate'''

	server_turn = lab2_socket.receive_message(connection)
	action, col = lab2_connectfourgame.stringToAction(server_turn)
	ready_message = lab2_socket.receive_message(connection)
	if (lab2_connectfourgame.checkMove(gamestate, action, col)):
		if (ready_message == 'READY' or ready_message == 'WINNER_YELLOW' or ready_message == 'WINNER_RED'):
			updated_gamestate = lab2_connectfourgame.makeMove(gamestate, action, col)
			return updated_gamestate, True
	return gamestate, False

def _server_Turn(connection: lab2_socket.Connection, gamestate: connectfour.GameState):
	'''Processes the server turn to see if the game should be continued and it returns a gamestate and boolean'''

	state = lab2_socket.receive_message(connection)
	if (state == 'OKAY'):
		gamestate, continue_playing = _process_Server_Move(connection, gamestate)
	elif (state == 'INVALID'):
		if(lab2_socket.receive_message(connection) == 'READY'):
			continue_playing = True
	elif (state == 'WINNER_RED' or state == 'WINNER_YELLOW'):
		continue_playing = False
	else:
		continue_playing = False
	lab2_connectfourgame.printBoard(gamestate)
	return gamestate, continue_playing

def _end_Game(connection: lab2_socket.Connection, gamestate: connectfour.GameState):
	'''Closes the connection to the server and prints out the winner of the game'''

	lab2_socket.close(connection)
	lab2_connectfourgame.printWinner(gamestate)

def playGame(connection: lab2_socket.Connection, gamestate: connectfour.GameState):
	'''Calls the functions to play the game and prints the board after each turn'''

	continue_playing = True
	lab2_connectfourgame.printBoard(gamestate)
	while(lab2_connectfourgame.checkWin(gamestate) and continue_playing):
		gamestate = _user_Turn(gamestate, connection)
		gamestate, continue_playing = _server_Turn(connection, gamestate)
	if (not lab2_connectfourgame.checkWin(gamestate)):
		_end_Game(connection, gamestate)
	else:
		print("The game crashed due to an error with the server.")

def initializeGame():
	'''Begins the game by asking for the host,port, and username and finally creates a new GameState with the new connection'''

	while True:
		host = _prompt_For_Host()
		port = _prompt_For_Port()
		try:
			connection = lab2_socket.connect(host, port)
			break
		except:
			print("The connection could not be made. Please try again.")
	lab2_socket.hello(connection, _prompt_For_Username())
	playGame(connection, connectfour.new_game())

if __name__ == '__main__':
	initializeGame()
