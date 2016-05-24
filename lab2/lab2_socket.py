#Ryan Yue 69858941
#Hubert Cheng 12885496

import socket
from collections import namedtuple

class ConnectFourError(Exception):
	"""A exception so that an error can be raised when something does not work"""
	pass

Connection = namedtuple("Connection", ["socket", "input", "output"])

def connect(host: str, port: int):
	"""Creates a connection with the server using a tuple of the host and port"""

	connect_socket = socket.socket()
	connect_socket.connect((host, port))
	input = connect_socket.makefile("r")
	output = connect_socket.makefile("w")
	return Connection(connect_socket, input, output)

def send_message(connection: Connection, message: str):
	"""A function to correctly send a message to the server with the end of line sequence and flushes"""

	connection.output.write(message + "\r\n")
	connection.output.flush()

def receive_message(connection: Connection):
	"""Function to receive the message and exclude the \n that is read"""

	return connection.input.readline()[:-1]

def close(connection: Connection):
	"""Correctly closes the connection with the server"""

	connection.input.close()
	connection.output.close()
	connection.socket.close()

def hello(connection: Connection, username: str):
	"""Follows the protocol to say "hello" to the server and checks if the user is sending back the correct welcome message
	Sends the message to the server to start a game and is notified that the server is ready"""

	_write_line(connection, "I32CFSP_HELLO {}".format(username))
	_expected_line(connection, "WELCOME {}".format(username))
	_write_line(connection, "AI_GAME")
	_expected_line(connection, "READY")

#Private functions
	
def _write_line(connection: Connection, line: str):
	"""Function to correctly write a line to the server with the end of line sequence and flush"""

	connection.output.write(line+"\r\n")
	connection.output.flush()

def _expected_line(connection: Connection, expected_line: str):
	"""Function to see if the line read from the sever is the expected/correct line"""

	line = _read_line(connection)
	if (line != expected_line):
		raise ConnectFourError()

def _read_line(connection: Connection):
	"""Read the line from the server"""
	
	return connection.input.readline()[:-1]
