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

import socket, select, sys, Queue, struct, time, random, os
from Network import Network
from Win import Win

UP = 259
RIGHT = 261
DOWN = 258
LEFT = 260
DEL = 127
ENTER = 10

class	Client():

	players	= {}
	posX = 1
	posY = 1

	def	__init__(self, name, host, port = 4242):
		self.win = Win(400, 400)
		# if self._checkIfPlayerExist(name) == False:
		self.name = name
		self.posY = 1
		self.posX = 1
		# else:
		# 	self._getSavedPlayer(name)
		self.host = host
		self.port = int(port)
		self.turn = 0
		self.wait = False
		self.map = ""
		self.peers = []
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((host, self.port))
			print "Connected to game server at %d" % self.port
			self.id = Network.GetPlayerID(self.sock)
			Network.SendPlayerName(self.sock, self.id, self.name)
			Network.sendPlayerSpawningPosition(self.sock, self.id, str(self.posX) + ":" + str(self.posY))
		except socket.error, e:
			print "Could not connect to the game server at {} ({}).".format(self.port, e)
			sys.exit(1)
		self.inputs = [self.sock, 0]
		self.outputs = []

		# CE QUE JE DOIT RECEVOIR DU SERVEUR
		Network.setPlayerAddedCallback(self._playerAddedCallback)
		Network.setPlayerIdCallback(self._playerHaveNewId)
		Network.setPlayerLeavedCallback(self._playerLeavedCallback)
		# Network.setPlayerNameCallback(self._playerChangeNameCallback)
		Network.setMapCallback(self._playerAskMap)
		Network.setNextTurn(self._playerGetNextTurn)
		Network.setPlayerLetsPlay(self._playerLetsPlay)
		Network.setServerGiveClientPositions(self._getOtherPlayerPosition)
		Network.setPlayerPositionChangeCallback(self._playerPositionChangeCallback)
		Network.setOtherPlayerName(self._getOtherPlayerName)

	def	_checkIfPlayerExist(self, name):
		try:
			directory = os.listdir("save/")
		except:
			return False
		for files in directory:
			if name in files:
				self._loadProfile(name)
				return True

	def	_loadProfile(self, name):
		# id:name = posX:posY [stuff]
		profile = os.open("save/" + name).read()
		infos, pos = profile.split('=')[0], profile.split('=')[1]
		self.id, self.name = infos.split(':')[0], infos.split(':')[1]
		self.posX, self.posY = pos.split(':')[0], pos.split(':')[1]
		profile.close()


	def	_getOtherPlayerName(self, id, datas):
		for s in self.peers:
			if s.id == id:
				s.name = datas

	def	_playerHaveNewId(self, id, datas):
		self.id = datas
		self.win.win.refresh()

	def	_getOtherPlayerPosition(self, id, datas):
		for client in datas.split('\n'):
			if client != "":
				if '@' in client:
					id, tmp = client.split('@')[0], client.split('@')[1]
					name, coord = tmp.split('=')[0], tmp.split('=')[1]
				else:
					id, coord = client.split('=')[0], client.split("=")[1]
				posX, posY = int(coord.split(':')[0]), int(coord.split(':')[1])
				nb = 0
				for ppl in self.peers:
					if ppl.id == id and self.id != id:
						ppl.posX, ppl.posY = posX, posY
						if name:
							ppl.name = name
					else:
						nb += 1
				if nb == len(self.peers):
					if name:
						self.peers.append(Peers(id, posX, posY, name))
					else:
						self.peers.append(Peers(id, posX, posY))
			
	def	_playerGetNextTurn(self, id, datas):
		self.turn = int(datas)

	def	_playerLetsPlay(self, id, datas):
		self.wait = False
		self._playerAskMap(None, None)

	def	_getMapData(self, datas):
		self.map = datas
		self.mapRow = self.map.count("\n")
		self.mapCol = int(len(self.map)  / self.mapRow) - 1

	def _playerAskMap(self, id, datas):
		if datas != None:
			self._getMapData(datas)
			self.win.win.addnstr(0, 0, self.map, len(self.map))
		else:
			self.win.win.addnstr(0, 0, self.map, len(self.map))
		i = 0
		for player in self.peers:
			if player.posX == self.posX and player.posY == self.posY or player.id == -1:
				continue
			elif player.connected == True:
				self.win.win.addnstr(player.posX, player.posY, str(player.id), len(str(player.id)))
				self.win.win.addnstr(0 + i, self.mapCol + 2, player.__str__(), len(player.__str__()))
				i += 1
		self.win.win.addnstr(self.posX, self.posY, str(self.id), len(str(self.id)))

	def _playerPositionChangeCallback(self, id, datas):
		if id == self.id:
			self.posX = int(datas.split(":")[0])
			self.posY = int(datas.split(":")[1])
		self._playerAskMap(None, None)

	def _playerAddedCallback(self, id, datas):
		msg = "player joined the game: " + str(id)
		self.win.win.addnstr(20, 40, msg, len(msg))
		self.win.win.refresh()

	def _playerLeavedCallback(self, id, datas):
		for s in self.peers:
			if s.id == id:
				s.connected = False
		msg = "Player {} disconnected.".format(id)
		self.win.win.addnstr(22, 40, msg, len(msg))
		self.win.win.refresh()

	def _playerChangeNameCallback(self, id, datas):
		for s in self.peers:
			if id == s.id:
				s.name = datas

	def	_waitEvent(self):
		try:
			while True:
				try:
					self.win.win.refresh()
					readable, writable, exceptionnal = select.select(self.inputs, self.outputs, self.inputs)
					for s in readable:
						if s == 0:
							if self.wait == False:
								action = self.win._nextTurn()
								# self.win.win.addnstr(30, 40, str(action), len(str(action)))
								if self._executeWinActions(action) != False:
									self.win.win.clear()
							# else:
							# 	self.win._nextTurn()
								# pass
								continue
						elif Network.Read(s) == False:
							print >>sys.stderr, "Server Disconnected, exiting.."
							sys.exit(0)
				except select.error, e:
					print >>sys.stderr, e
					time.sleep(1)
					sys.exit(0)
		except KeyboardInterrupt, e:
			print >>sys.stderr, e
			sys.exit(0)

	def	_executeWinActions(self, action):
		if action in [LEFT, RIGHT, DOWN, UP]:
			self.wait = True
			posY = self.posY
			posX = self.posX
			if action == LEFT and posY - 1 >= 0:
				posY -= 1
			elif action == DOWN and posX + 1 < self.mapRow:
				posX += 1
			elif action == RIGHT and posY + 1 < self.mapCol:
				posY += 1
			elif action == UP and posX - 1 >= 0:
				posX -= 1
			else:
				self.wait = False
				return False
			Network.AskServerIfPosition(self.sock, self.id, str(posX) + ":" + str(posY))
			return True
		elif action == 127:
			self.win._leave()
		else:
			return False

class Peers():

	def __init__(self, id, posX, posY, name=None):
		self.id = id
		self.name = None
		self.posX = int(posX)
		self.posY = int(posY)
		self.connected = True

	def	__str__(self):
		if self.name != None:
			return "{} is at x:{} y:{}.".format(self.name, self.posX, self.posY)
		else:
			return "Peers n{} is at x:{} y:{}.".format(self.id, self.posX, self.posY)


client = Client(sys.argv[1], sys.argv[2], 4242)
client._waitEvent()

