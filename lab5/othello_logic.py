#Ryan Yue
#69858941

class OthelloGamestate:
	"""This class represents one othello game."""
	def __init__(self, row: int, col: int, first_move: str, position: str, win_condition: str) -> None:
		"""This method initializes an othello game. It takes in the parameters of board size, first move, starting positions,
		and win conditions and sets up the game board accordingly"""
		self.row = row
		self.col = col
		self.move = first_move
		self.position = position
		self.win_condition = win_condition
		self.num_black = 2
		self.num_white = 2
		self.continue_game = True
		self.black_can_move = True
		self.white_can_move = True
		self.original_move = first_move
		self.gameboard = self._setup_gameboard()
		self._setup_initial_piece_position()

	def new_gameboard(self):xq
		self.gameboard = self._setup_gameboard()
		self._setup_initial_piece_position()
		self.move = self.original_move
		self.num_black = 2
		self.num_white = 2

	def _setup_gameboard(self) -> None:
		"""This method initializes the game board array with the correct number of rows and columns"""
		gameboard = []
		for i in range(self.get_num_row()):
			array = []
			for i in range(self.get_num_col()):
				array.append(".")
			gameboard.append(array)
		return gameboard

	def _setup_initial_piece_position(self) -> None:
		"""This method sets up the initial positioning of the 2 black and 2 white pieces in the center of the board"""
		initial_row = self.get_num_row()//2
		initial_col = self.get_num_col()//2
		if (self.position == "W"):
			opposite = "B"
		else:
			opposite = "W"
		self.gameboard[initial_row-1][initial_col-1] = self.position
		self.gameboard[initial_row][initial_col] = self.position
		self.gameboard[initial_row][initial_col-1] = opposite
		self.gameboard[initial_row-1][initial_col] = opposite

	def get_game_board(self) -> [[]]:
		"""This method returns the current game board"""
		return self.gameboard

	def print_game_board(self) -> None:
		"""This methood prints out the number of each piece (black and white) and the game board itself"""
		print("B: {}  W: {}".format(self.num_black, self.num_white))
		for i in self.gameboard:
			for j in i:
				print(j, end=" ")
			print("\n")

	def print_turn(self) -> None:
		"""This method prints out the current turn"""
		print("TURN: {}".format(self.get_current_color()))

	def convert_to_coordinates(self, row, col) -> (int, int):
		"""This method converts the numbers that the user entered into indices of the list. Since lists start at index 0 instead of 1,
		we subtract 1 from both row and col"""
		return row-1, col-1

	def get_num_row(self) -> int:
		"""This method returns the number of rows in the board"""
		return self.row

	def get_num_col(self) -> int:
		"""This method returns the number of colunns in the board"""
		return self.col

	def get_current_color(self) -> str:
		"""This method returns the current move (black or white)"""
		return self.move

	def get_opposite_color(self) -> str:
		"""This method returns the opposite move (black or white)"""
		if (self.move == "B"):
			return "W"
		else:
			return "B"

	def continue_playing(self) -> bool:
		"""This method checks if there are any moves that can be made on the board"""
		if (self.black_can_move or self.white_can_move):
			return True
		return False

	def check_board_conditions(self):
		"""This method checks if one color still has moves left on the board"""
		for i in range(self.get_num_row()):
			for j in range(self.get_num_col()):
				if self.gameboard[i][j] == ".":
					if (len(self.check_pieces_to_flip(i,j)) != 0):
						return
		if (self.get_current_color() == "B"):
			self.black_can_move = False
			self.move = self.get_opposite_color()
		else:
			self.white_can_move = False
			self.move = self.get_opposite_color()

	def check_move(self, row, col) -> bool:
		"""This method checks if the move that the user entered is valid. It checks if it is within the game board bounds,
		if the cell that the user is empty, and if that cell is valid to flip other pieces"""
		if (row > self.get_num_row() or col > self.get_num_col() or row < 0 or col < 0):
			return False
		elif (self.gameboard[row][col] != "."):
			return False
		elif (len(self.check_pieces_to_flip(row, col)) == 0):
			return False
		else:
			return True

	def check_pieces_to_flip(self,row: int,col: int) -> []:
		"""This method returns the cells to flip in all 8 directions of the cell the user entered. For each of the directions, it iterates through
		the cells in that direction. If the order of the cells in that direction, match the order that is needed to flip the pieces, then it will
		append those cells to a list."""
		check_directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
		pieces_to_flip = []
		for i in check_directions:
			next_x = row
			next_y = col
			pieces = []
			while True:
				next_x += i[0]
				next_y += i[1]
				if ((next_x >= self.get_num_row()) or (next_x < 0) or (next_y >= self.get_num_col()) or (next_y < 0)):
					break
				elif (self.gameboard[next_x][next_y] == "."):
					break
				elif (self.gameboard[next_x][next_y] == self.get_current_color()):
					pieces.append([next_x, next_y])
				elif (self.gameboard[next_x][next_y] == self.get_opposite_color()):
					pieces.append([next_x, next_y])
					next_piece_x = next_x + i[0]
					next_piece_y = next_y + i[1]
					if ((next_piece_x >= self.get_num_row()) or (next_piece_x < 0) or (next_piece_y >= self.get_num_col()) or (next_piece_y < 0)):
						break
					else:
						if (self.gameboard[next_piece_x][next_piece_y] == self.get_current_color()):
							pieces_to_flip.extend(pieces)
							break
		return pieces_to_flip

	def flip_pieces(self, places_to_flip: []) -> None:
		"""This method takes an array of the cells that need to be flipped and change it to the current color. It also adds and subtracts
		to the count of black and white pieces on the board"""
		added = 0
		for i in places_to_flip:
			if (self.gameboard[i[0]][i[1]] != self.get_current_color()):
				self.gameboard[i[0]][i[1]] = self.get_current_color()
				added += 1
		if (self.get_current_color() == "B"):
			self.num_black += added
			self.num_white -= added
		else:
			self.num_white += added
			self.num_black -= added


	def make_move(self, row: int, col: int) -> None:
		"""This method gets the array of pieces to flip and calls the flip function to flip it. It also places down the piece at the location
		the user specified and adds 1 to either black or white, depending on the turn"""
		pieces_to_flip = self.check_pieces_to_flip(row, col)
		self.get_game_board()[row][col] = self.get_current_color()
		self.flip_pieces(pieces_to_flip)
		if (self.get_current_color() == "B"):
			self.num_black += 1
		else:
			self.num_white += 1
		self.move = self.get_opposite_color()

	def end_game(self) -> str:
		"""This method prints out the ending statements of the game and shows the winner"""
		if (self.num_black > self.num_white):
			if (self.win_condition == ">"):
				return "B"
			else:
				return "W"
		elif (self.num_white > self.num_black):
			if (self.win_condition == ">"):
				return "W"
			else:
				return "B"
		else:
			return "NONE"