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

import socket, select, sys, types, struct, time
from Network import Network

class		Server():

	def	__init__(self, ip, port, map):
		Server.rawmap = map.generate_definitive_map()
		Server.map = map.__str__()
		Server.row = map.col
		self.turn = 0
		self.nextTurn = self.turn + 1
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((ip, port))
		self.server.listen(5)
		self.inputs = [self.server]
		self.outputs = []
		self.connected_clients = []
		self.disconnected_clients = []

		# CE QUE JE DOIT RECEVOIR DES CLIENTS
		Network.setPlayerNameCallback(self._PlayerNameChanged)
		Network.setPlayerAskForPosition(self._playerAskingForPosition)
		Network.setPlayerSpawningPositionCallback(self._playerSpawningPosition)
		Network.setPlayerLetsPlay(self._launchGame)
		# Network.setPlayerNewIdCallback(self._givePlayerNewID)

	def	_waitEvent(self):
		while self.inputs:
			print >>sys.stderr, '\nWaiting for next event.'
			try:
				readableClient, writableClient, exceptional = select.select(self.inputs, self.outputs, self.inputs)
			except KeyboardInterrupt, e:
				print >>sys.stderr, e, "\nServer disconnected by user. Closing..."
				time.sleep(1)
				sys.exit(0)

			for s in readableClient:
				if s is self.server:
					connection, client_address = s.accept()
					print >>sys.stderr, "New client on socket: {}, from {}.".format(connection.fileno(), client_address)
					self.inputs.append(connection)
					obj = ConnectedClient(connection)
					self.connected_clients.append(obj)
					Network.SendPlayerID(connection, obj.id)
					self.outputs.append(s)
					self._sendNewClient(connection, obj)
					self._sendClientList(connection)
					self._sendMapClient(connection)
				else:
					if Network.Read(s) == False:
						print >>sys.stderr, 'Player from', client_address, 'disconnected from the game.'
						self._removeConnectedClient(s)
			for s in exceptional:
				print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
				self._removeConnectedClient(s)
	



	# Unused at the moment

	def	_launchGame(self, id, action):
		for client in self.connected_clients:
			Network.sendPlayerLetsPlay(client.socket, client.id, "GO")










	# def	_givePlayerNewID(self, id, action):
	# 	for client in self.co

	def	_sendAllPlayerPositions(self):
		toSend = ""
		for client in self.connected_clients:
			toSend += str(client.id) + "=" + str(client.posX) + ":" + str(client.posY) + "\n"
		for client in self.connected_clients:
			Network.sendClientPositionList(client.socket, client.id, toSend)


	def	_playerHavePlayed(self, id, action):
		i = 0
		for client in self.connected_clients:
			if client.wait == True:
				i += 1
		if i == len(self.connected_clients):
			print "All player have played!"
			self.turn += 1
			for s in self.connected_clients:
				s.wait = False
				Network.sendNextTurnPlayer(s.socket, s.id, str(self.turn))
				self._sendMapClient(s.socket)
		for client in self.connected_clients:
			Network.sendPlayerLetsPlay(client.socket, client.id, str(self.turn))

	def	_removeConnectedClient(self, target):
		for p in self.connected_clients:
			if p.socket.fileno() == target.fileno():
				self.disconnected_clients.append(p)
				self.connected_clients.remove(p)
				self._sendClientLeaved(p.socket, p.id)
		if target in self.inputs:
			self.inputs.remove(target)
		if target in self.outputs:
			self.outputs.remove(target)
		target.close()

	def _PlayerNameChanged(self, id, name):
		for s in self.connected_clients:
			if s.id == id:
				socket = s.socket
		for ppl in self.disconnected_clients:
			if ppl.id == id:
				self.connected_clients.append(ConnectedClient(s.socket, ppl.id, ppl.name, ppl.posX, ppl.posY))
				print "Welcome back {}! ({})".format(ppl.name, ppl.id)
				self.disconnected_clients.remove(ppl)
				return
		for s in self.connected_clients:
			if s.id == id:
				s.name = name
				print "Player {} is now called {}! ".format(id, name)
				self._sendClientNameChanged(s.socket, s.id, name)

	def	_playerSpawningPosition(self, id, position):
		for s in self.connected_clients:
			if s.id == id:
				s.posX = int(position.split(":")[0])
				s.posY = int(position.split(":")[1])
				break

	def	_playerAskingForPosition(self, id, position):
		for s in self.connected_clients:
			if s.id == id and s.wait == False:
				s.wait = True
				posX = int(position.split(":")[0])
				posY = int(position.split(":")[1])
				if self._collisionCheck(posX, posY) == True:
					s.posX = posX
					s.posY = posY
					position = str(s.posX) + ":" + str(s.posY)
					Network.SendPlayerPosition(s.socket, s.id, position)
					break
		self._sendAllPlayerPositions()
		self._playerHavePlayed(None, None)
	
	def	_collisionCheck(self, posX, posY):
		collision = False
		if Server.rawmap[posX][posY] == 2:
			for s in self.connected_clients:
				if s.posX == posX and s.posY == posY:
					print "ANOTHER PLAYER ENCOUNTERED"
					collision = True
					# return False
				# else:
					# return True
		if collision == False:
			return True
		return False

	def	_sendMapClient(self, target):
		Network.SendMapPlayer(target, Server.map)

	def	_sendClientList(self, target):
		toSend = ""
		for s in self.connected_clients:
			if s.socket.fileno() != target.fileno():
				if s.name:
					toSend += s.name + "," + struct.pack("i", s.id) + ";"
		Network.SendMultipleAddPlayer(target, toSend)

	def _sendNewClient(self, target, obj):
		for s in self.connected_clients:
			if s.socket.fileno() != target.fileno():
				Network.SendAddPlayer(s.socket, obj.id, str(obj.id))

	def _sendClientLeaved(self, connection, id):
		for s in self.connected_clients:
			if s.socket.fileno() != connection.fileno():
				Network.SendPlayerLeaved(s.socket, id)
		
	def _sendClientNameChanged(self, connection, id, newName):
		for s in self.connected_clients:
			if s.socket.fileno() != connection.fileno():
				Network.SendPlayerName(s.socket, id, newName)

class	DisconnectedClient():

	def	__init__(self, sock, name, id, posX, posY):
		self.socket, self.name, self.id, self.posX, self.posY = sock, name, id, posX, posY


class	ConnectedClient():

	clientID = 0

	def	__init__(self, sock, id=None, name=None, posX=1, posY=1):
		if id != None:
			self.id = id
		else:
			self.id = ConnectedClient.clientID
			ConnectedClient.clientID += 1
		self.wait = False
		self.name = name
		self.posX = posX
		self.posY = posY
		self.socket = sock

	def __str__(self):
		msg = str(self.id) + " should wait?: {}".format(self.wait)
		return msg

	def	_setClientName(self, name):
		self.name = name
