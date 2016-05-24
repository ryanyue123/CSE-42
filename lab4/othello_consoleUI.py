#Ryan Yue
#69858941

import othello_logic

def promptUserForSetup() -> othello_logic.OthelloGamestate:
	"""This method prompts the user to enter the board size, the piece that moves first, the position of the starting pieces,
	and the win condition of the game"""
	print("FULL")
	row = int(input(""))
	col = int(input(""))
	first_move = input("")
	position = input("")
	win_condition = input("")
	oth = othello_logic.OthelloGamestate(row, col, first_move, position, win_condition)
	return oth

def promptUserForMove() -> (int, int):
	"""This method prompts the user to enter a row and a column to make their move"""
	usr_input = input("")
	row = int(usr_input[0])
	col = int(usr_input[2])
	return row, col

def playGame(oth: othello_logic.OthelloGamestate) -> None:
	"""This method runs the game.
		First it prints the intial board,
		It checks to see if there are still moves available and prompts the user to make a move.
		If the move that the user entered is valid, the move will be made and the game board will be updated.
		If there are no more moves available, it will end the game and print the results"""
	oth.print_game_board()
	while (oth.continue_playing()):
		if (oth.check_board_conditions()):
			oth.print_turn()
			row, col = promptUserForMove()
			row, col = oth.convert_to_coordinates(row, col)
			if (oth.check_move(row, col)):
				print("VALID")
				oth.make_move(row, col)
				oth.print_game_board()
			else:
				print("INVALID")
	oth.end_game()

if __name__ == '__main__':
	oth = promptUserForSetup()
	playGame(oth)
