#Ryan Yue 69858941
#Hubert Cheng 12885496

import lab2_connectfourgame
import connectfour

def playGame(gamestate: connectfour.GameState):
	'''Calls functions from lab2_connectfourgame.py to play a console version of connectfour'''

	lab2_connectfourgame.printBoard(gamestate)
	while(lab2_connectfourgame.checkWin(gamestate)):
		user_action, col_num = lab2_connectfourgame.getUserInput()
		if (lab2_connectfourgame.checkMove(gamestate, user_action, col_num)):
			gamestate = lab2_connectfourgame.makeMove(gamestate, user_action, col_num)
			lab2_connectfourgame.printBoard(gamestate)
		else:
			print("Please enter a valid move")
	lab2_connectfourgame.printWinner(gamestate)

if __name__ == '__main__':
	playGame(connectfour.new_game())


