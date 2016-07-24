# Ryan Yue
# 69858941

import othello_logic
import tkinter
from tkinter import messagebox

class LaunchScreen:
	'''This class represents the settings screen of the application. The settings screen allows the user to manipulate the
	game board - change number of rows, columns, choose who goes first, control the setup of the board, and choose the win
	condition. After the user clicks begin, it will return to the main game application.'''
	def __init__(self):
		'''sets up the initial conditions of the tkinter toplevel.'''
		self._detail_window = tkinter.Toplevel()
		self._font = ('Helvetica', 16)
		self._num_rows = 1
		self._num_col = 1
		self._first_move = ""
		self._left_corner_color = ""
		self._win_condition = ""

		# Creates and grids all LABELS
		game_label = tkinter.Label(
			master = self._detail_window,
			text = "Othello FULL GAME",
			font = self._font
		)
		game_label.grid(
			row = 0,
			column = 0,
			padx = 10,
			pady = 10,
			columnspan = 2
		)
		row_label = tkinter.Label(
			master = self._detail_window,
			text = "Number of rows: ",
			font = self._font
		)
		row_label.grid(
			row = 1,
			column = 0,
			padx = 10,
			pady = 10,
			sticky = tkinter.W
		)
		col_label = tkinter.Label(
			master = self._detail_window,
			text = "Number of columns: ",
			font = self._font
		)
		col_label.grid(
			row = 2,
			column = 0,
			padx = 10,
			pady = 10,
			sticky = tkinter.W
		)
		first_move = tkinter.Label(
			master = self._detail_window,
			text = "First move: ",
			font = self._font
		)
		first_move.grid(
			row = 3,
			column = 0,
			padx = 10,
			pady = 10,
			sticky = tkinter.W
		)
		color_setup = tkinter.Label(
			master = self._detail_window,
			text = "Color for top left corner: ",
			font = self._font
		)
		color_setup.grid(
			row = 4,
			column = 0,
			padx = 10,
			pady = 10,
			sticky = tkinter.W
		)
		win_condition = tkinter.Label(
			master = self._detail_window,
			text = "Win condition: ",
			font = self._font
		)
		win_condition.grid(
			row = 5,
			column = 0,
			padx = 10,
			pady = 10,
			sticky = tkinter.W
		)
		# Creates and grids all Input Widgets
		self._row_entry = tkinter.Spinbox(
			master = self._detail_window,
			from_ = 4,
			to = 16,
			increment = 2,
			justify = "right"
		)
		self._row_entry.grid(
			row = 1,
			column = 1,
			padx = 10,
			pady = 10,
			sticky = tkinter.E
		)
		self._col_entry = tkinter.Spinbox(
			master = self._detail_window,
			from_ = 4,
			to = 16,
			increment = 2,
			justify = "right"
		)
		self._col_entry.grid(
			row = 2,
			column = 1,
			padx = 10,
			pady = 10,
			sticky = tkinter.E
		)
		self._first_move_entry = tkinter.Entry(
			master = self._detail_window,
			font = self._font,
			justify = "right"
		)
		self._first_move_entry.grid(
			row = 3,
			column = 1,
			padx = 10,
			pady = 10,
			sticky = tkinter.E
		)
		self._left_corner = tkinter.Entry(
			master = self._detail_window,
			font = self._font,
			justify = "right"
		)
		self._left_corner.grid(
			row = 4,
			column = 1,
			padx = 10,
			pady = 10,
			sticky = tkinter.E
		)
		self._win_condition_entry = tkinter.Entry(
			master = self._detail_window,
			font = self._font,
			justify = "right"
		)
		self._win_condition_entry.grid(
			row = 5,
			column = 1,
			padx = 10,
			pady = 10,
			sticky = tkinter.E
		)

		# Creates and grids all Buttons
		cancel_button = tkinter.Button(
			master = self._detail_window,
			text = "CANCEL",
			font = self._font,
			bg = "#000000",
			command = self.quit
		)
		cancel_button.grid(
			row = 6,
			column = 1,
			padx = 10,
			pady = 10,
			sticky = tkinter.E + tkinter.N
		)
		submit_button = tkinter.Button(
			master = self._detail_window,
			text = "BEGIN",
			font = self._font,
			bg = '#000000',
			command = self.start_click
		)
		submit_button.grid(
			row =  6,
			column = 0,
			padx = 10,
			pady = 10,
			sticky = tkinter.N + tkinter.W
		)
		# Configure rows and columns so that resizing the canvas adds to each row and column proportionally
		self._detail_window.rowconfigure(0, weight = 1)
		self._detail_window.rowconfigure(1, weight = 1)
		self._detail_window.rowconfigure(2, weight = 1)
		self._detail_window.rowconfigure(3, weight = 1)
		self._detail_window.rowconfigure(4, weight = 1)
		self._detail_window.rowconfigure(5, weight = 1)
		self._detail_window.rowconfigure(6, weight = 1)
		self._detail_window.columnconfigure(0, weight = 1)
		self._detail_window.columnconfigure(1, weight = 1)

	def show(self) -> None:
		'''Shows the toplevel window and waits until the toplevel is dismissed'''
		self._detail_window.grab_set()
		self._detail_window.wait_window()

	def start_click(self) -> None:
		'''If the begin button is clicked, gather all the inputs from the input fields'''
		self._started = True
		self._num_rows = self._row_entry.get()
		self._num_col = self._col_entry.get()
		self._first_move = self._first_move_entry.get()
		self._left_corner_color = self._left_corner.get()
		self._win_condition = self._win_condition_entry.get()
		if (self.check_inputs()):
			self._detail_window.destroy()
		else:
			# Error produces a message box to tell the user to check their inputs
			tkinter.messagebox.showinfo("Error", "Please check your inputs")

	def check_inputs(self) -> bool:
		'''This function makes sure the inputs acceptable for the othello game'''
		accepted_colors = ["B", "W"]
		accepted_win_conditions = [">", "<"]
		if (self._first_move in accepted_colors):
			if (self._win_condition in accepted_win_conditions):
				return True
		return False

	def started(self) -> bool:
		return self._started

	def num_rows(self) -> int:
		return int(self._num_rows)

	def num_col(self) -> int:
		return int(self._num_col)

	def first_move(self) -> str:
		return self._first_move

	def left_corner(self) -> str:
		return self._left_corner_color

	def win_condition(self) -> str:
		return self._win_condition

	def quit(self) -> None:
		'''Destroys the settings window'''
		self._started = False
		self._detail_window.destroy()

class OthelloApplication:
	'''This class represents the othello game application. This is where the game board will be drawn and where the users
	will click to interact with the game'''
	def __init__(self):
		'''Sets up the initial state of the game. If the user does not choose to alter the game settings, the board defautls to
		a 4 x 4 gameboard'''
		self._game = othello_logic.OthelloGamestate(4, 4, "B", "B", ">")
		self._num_rows = self._game.get_num_row()
		self._num_col = self._game.get_num_col()

		self._root_window = tkinter.Tk()
		# Create and grid all the LABELS for the game
		game_label = tkinter.Label(
			master = self._root_window,
			text = "Othello Game Full",
			font = ("Helvetica", 24)
		)
		game_label.grid(
			row = 0,
			column = 0,
			padx = 10,
			pady = 10,
			columnspan = 4,
		)
		self._win_label = tkinter.Label(
			master = self._root_window,
			text = "Win condition: color with the most pieces wins",
			font = ("Helvetica", 16)
		)
		self._win_label.grid(
			row = 1,
			column = 0,
			padx = 10,
			pady = 10,
			columnspan = 4,
		)
		self._score_label = tkinter.Label(
			master = self._root_window,
			text = "Black: 2 White: 2",
			font = ("Helvetica", 16)
		)
		self._score_label.grid(
			row = 2,
			column = 0,
			padx = 10,
			pady = 10
		)
		self._turn_label = tkinter.Label(
			master = self._root_window,
			text = "Turn: {}".format(self._game.get_current_color()),
			font = ("Helvetica", 16)
		)
		self._turn_label.grid(
			row = 2,
			column = 1,
			padx = 10,
			pady = 10
		)
		# Create and grid the settings and clear board buttons
		setup_button = tkinter.Button(
			master = self._root_window,
			text = "Settings",
			font = ("Helvetica", 16),
			command = self._setup_game,
		)
		setup_button.grid(
			row = 2,
			column = 2,
			padx = 10,
			pady = 10
		)
		new_game_button = tkinter.Button(
			master = self._root_window,
			text = "Clear Board",
			font = ("Helvetica", 16),
			command = self._new_game,
		)
		new_game_button.grid(
			row = 2,
			column = 3,
			padx = 10,
			pady = 10
		)
		# creates and grids the canvas, which draws the game board
		self._canvas = tkinter.Canvas(
			master = self._root_window,
			width = 600,
			height = 600,
			background = "#FFFFFF"
		)
		self._canvas.grid(
			row = 3,
			column = 0,
			columnspan = 4,
			padx = 10,
			pady = 10,
			sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W
		)
		# configures the rows and columns to resize accordingly.
		self._root_window.rowconfigure(3, weight = 1)
		self._root_window.columnconfigure(0, weight = 1)
		self._root_window.columnconfigure(1, weight = 1)
		self._root_window.columnconfigure(2, weight = 1)
		self._root_window.columnconfigure(3, weight = 1)
		self._canvas.bind('<Configure>', self._canvas_resized)
		self._canvas.bind('<Button-1>', self._canvas_clicked)
		self._root_window.update()
		self._draw_board()


	def start(self) -> None:
		self._root_window.mainloop()

	def _canvas_resized(self, e: tkinter.Event) -> None:
		'''When the canvas is resized, delete everything that is on the canvas and redraw it proportionally to the new size'''
		try:
			self._canvas.delete(tkinter.ALL)
			self._draw_board()
		except:
			pass

	def _canvas_clicked(self, e: tkinter.Event) -> None:
		'''Determine where the user clicked on the board and translate the pixel point to a row and column in the game board. Check to
		see if that move is valid, then draw pieces accordingly'''
		row = int((e.x/self._canvas.winfo_width())*self._num_rows)
		col = int((e.y/self._canvas.winfo_height())*self._num_col)
		if (self._game.check_move(row, col)):
			self._game.make_move(row,col)
			self._draw_board()
			self._game.check_board_conditions()
			self._game.check_board_conditions()
			self._score_label.config(text = "Black: {} White: {}".format(self._game.num_black, self._game.num_white))
			self._turn_label.config(text = "Turn: {}".format(self._game.get_current_color()))
			if (self._game.continue_playing() == False):
				self._win_label.config(text = "Winner: {}".format(self._game.end_game()))

	def _draw_board(self) -> None:
		'''Draws the gameboard on the canvas'''
		cell_width = self._canvas.winfo_width()/self._num_rows
		cell_height = self._canvas.winfo_height()/self._num_col
		for i in range(self._num_rows):
			for j in range(self._num_col):
				self._draw_cell(i,j,cell_width, cell_height)
				if (self._game.gameboard[i][j] == "B"):
					self._draw_oval(i, j, cell_width, cell_height, "black")
				elif (self._game.gameboard[i][j] == "W"):
					self._draw_oval(i, j, cell_width, cell_height, "white")

	def _draw_cell(self, row, col, cell_width, cell_height) -> None:
		'''Draws each cell, representing one position on the gameboard'''
		start_x = row * cell_width
		start_y = col * cell_height
		end_x = start_x + cell_width
		end_y = start_y + cell_height
		self._canvas.create_rectangle(start_x, start_y, end_x, end_y, fill = "grey")

	def _draw_oval(self, row, col, cell_width, cell_height, color) -> None:
		'''Draws a black or white oval in the cell depending on the piece'''
		start_x = row * cell_width
		start_y = col * cell_height
		end_x = start_x + cell_width
		end_y = start_y + cell_height
		self._canvas.create_oval(start_x + 1, start_y + 1, end_x - 1, end_y - 1, fill = color)

	def _new_game(self) -> None:
		'''Creates a new board and resets all the labels to the original state'''
		self._game.new_gameboard()
		self._draw_board()
		self._score_label.config(text = "Black: 2 White: 2")
		self._turn_label.config(text = "Turn: {}".format(self._game.get_current_color()))
		if (self._game.win_condition == ">"):
			self._win_label.config(text = "Win condition: color with the most pieces wins")
		else:
			self._win_label.config(text = "Win condition: color with the least pieces wins")

	def _setup_game(self) -> None:
		'''shows the launch screen when the settings button is clicked. Creates a new othello game with the inputs that
		the user entered'''
		launcher = LaunchScreen()
		launcher.show()
		if launcher._started:
			self._game = othello_logic.OthelloGamestate(
				launcher.num_rows(),
				launcher.num_col(),
				launcher.first_move(),
				launcher.left_corner(),
				launcher.win_condition()
			)
			self._num_rows = self._game.get_num_row()
			self._num_col = self._game.get_num_col()
			self._new_game()
			if (self._game.win_condition == ">"):
				self._win_label.config(text = "Win condition: color with the most pieces wins")
			else:
				self._win_label.config(text = "Win condition: color with the least pieces wins")
			self._draw_board()