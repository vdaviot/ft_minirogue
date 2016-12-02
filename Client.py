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

import socket, select, sys, Queue, struct, time
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
			print "Your client id is", self.id
			Network.SendPlayerName(self.sock, self.id, self.name)
		except socket.error, e:
			print "Could not connect to the game server at {} ({}).".format(self.port, e)
			sys.exit(1)
		self.inputs = [self.sock]
		self.outputs = []

		# CE QUE JE DOIT RECEVOIR DU SERVEUR
		Network.setPlayerPositionChangeCallback(self._playerPositionChangeCallback)
		Network.setPlayerAddedCallback(self._playerAddedCallback)
		Network.setPlayerLeavedCallback(self._playerLeavedCallback)
		Network.setPlayerNameCallback(self._playerChangeNameCallback)
		Network.setMapCallback(self._playerAskMap)

	def _playerAskMap(self, id, datas):
		print "Level map: \n", datas
		pass

	def _playerPositionChangeCallback(self, id, datas):
		print "player moved to: ", id, datas
		pass

	def _playerAddedCallback(self, id, datas):
		print "player joined the game: ", id
		self.players[id] = {"name":""}
		self.players[id]["name"] = str(id)
		pass

	def _playerLeavedCallback(self, id, datas):
		print "player disconnected:", id
		del self.players[id]
		pass

	def _playerChangeNameCallback(self, id, datas):
		self.players[id]["name"] = datas
		pass

	def	_waitEvent(self):
		try:
			while True:
				try:
					readable, writable, exceptionnal = select.select(self.inputs, self.outputs, self.inputs, 1)
					if len(readable) != 0:
						Network.Read(self.sock)
				except select.error, e:
					print >>sys.stderr, e
					time.sleep(1)
					sys.exit(0)
		except KeyboardInterrupt, e:
			print >>sys.stderr, e
			sys.exit(0)


client = Client(sys.argv[1], sys.argv[2], 4242)
client._waitEvent()

