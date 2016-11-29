# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/28 15:39:44 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/28 15:39:46 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, select, sys, types, struct
from Network import Network

class		Server():

	def	__init__(self, ip, port):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((ip, port))
		self.server.listen(5)
		self.inputs = [self.server]
		self.outputs = []
		self.connected_clients = []

		Network.setPlayerNameCallback(self._PlayerNameChanged)
		Network.setPlayerPositionChangeCallback(self._PlayerPositionChanged)

	def	_removeConnectedClient(self, target):
		for p in self.connected_clients:
			if p.socket.fileno() == target.fileno():
				print "deleted client from list"
				self.connected_clients.remove(p)
				self._sendLeavedClient(p.socket, p.id)
		if target in self.inputs:
			self.inputs.remove(target)
		if target in self.outputs:
			self.outputs.remove(target)
		target.close()

	def _PlayerNameChanged(self, id, name):
		print "name: " + name
		for s in self.connected_clients:
			if s.id == id:
				s.name = name
				self._sendClientNameChanged(s.socket, s.id, name)

	def _PlayerPositionChanged(self, socket, position):
		print "pos: " + position


	def	_waitEvent(self):
		while self.inputs:
			print >>sys.stderr, '\nWaiting for next event.'
			readableClient, writableClient, exceptional = select.select(self.inputs, self.outputs, self.inputs)
			for s in readableClient:
				if s is self.server:
					connection, client_address = s.accept()
					print "new client on socket: {}".format(connection.fileno())
					print >>sys.stderr, 'New player connected from', client_address
					self.inputs.append(connection)
					obj = ConnectedClient(connection)
					self.connected_clients.append(obj)
					Network.SendPlayerID(connection, obj.id)
					self.outputs.append(s)
					self._sendClientList(connection)
					self._sendNewClient(connection)
				else:
					if Network.Read(s) == False:
						print >>sys.stderr, 'Player from', client_address, 'disconnected from the game.'
						self._removeConnectedClient(s)
			for s in exceptional:
				print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
				self._removeConnectedClient(s)

	def	_sendClientList(self, target):
		toSend = ""
		for s in self.connected_clients:
			if s.socket.fileno() != target.fileno():
				toSend += s.name + "," + struct.pack("i", s.id) + ";"
		Network.SendMultipleAddPlayer(target, toSend)

	def _sendNewClient(self, connection):
		for s in self.connected_clients:
			if s.socket.fileno() != connection.fileno():
				Network.SendAddPlayer(s.socket, s.id, str(s))

	def _sendLeavedClient(self, connection, id):
		for s in self.connected_clients:
			if s.socket.fileno() != connection.fileno():
				Network.SendLeavedPlayer(s.socket, id)

	def _sendClientNameChanged(self, connection, id, newName):
		for s in self.connected_clients:
			if s.socket.fileno() != connection.fileno():
				Network.SendPlayerName(s.socket, id, newName)

class	ConnectedClient():

	clientID = 0

	def	__init__(self, sock):
		self.id = ConnectedClient.clientID
		ConnectedClient.clientID += 1
		self.name = None
		self.socket = sock

	def	_setClientName(self, name):
		self.name = name

	def __str__(self):
		if self.name == None:
			return str(self.clientID)
		else:
			return self.name

# try:
server = Server(sys.argv[1], int(sys.argv[2]))
server._waitEvent()
# except:
	# print "\nProgram closed."
