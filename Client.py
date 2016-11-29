# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Client.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/28 15:46:39 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/28 15:46:41 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, select, sys, Queue, struct
from Network import Network

class	Client():

	players		= {}

	def	__init__(self, name, host, port=4242):
		self.name = name
		self.host = host
		self.port = int(port)
		self.addr = host + ':' + str(port)
		self.id = 0
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((host, self.port))
			print "Connected to game server at %d" % self.port

			self.id = Network.GetPlayerID(self.sock)

			print "client id: ", self.id
			Network.SendPlayerName(self.sock, self.id, self.name)
		except socket.error, e:
			print "Could not connect to the game server at {} ({}).".format(self.port, e)
			sys.exit(1)
		self.inputs = [self.sock]
		self.outputs = []

		Network.setPlayerPositionChangeCallback(self._playerPositionChangeCallback)
		Network.setPlayerAddedCallback(self._playerAddedCallback)
		Network.setPlayerLeavedCallback(self._playerLeavedCallback)
		Network.setPlayerNameCallback(self._playerChangeNameCallback)

	def _playerPositionChangeCallback(self, id, datas):
		print "player moved to: ", id, datas
		pass

	def _playerAddedCallback(self, id, datas):
		print "player joined the game: ", id
		self.players[id].name = str(id)
		pass

	def _playerLeavedCallback(self, id, datas):
		print "player disconnected:", id
		del self.players[id]
		pass

	def _playerChangeNameCallback(self, id, datas):
		print "player ", id, "changed name", datas
		self.players[id].name = datas
		pass

	def	_waitEvent(self):
		while self.inputs:
			readable, writable, exceptionnal = select.select(self.inputs, self.outputs, self.inputs)
			if len(readable) != 0:
				Network.Read(self.sock)
					# print "Data received from game server: {}".format(data)
			# if len(writable) != 0:

			# 	self.sock.send("{} wrote something to the server.".format(self.name))


client = Client(sys.argv[1], "localhost", 4242)
client._waitEvent()

