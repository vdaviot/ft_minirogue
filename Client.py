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

import socket, select, sys, Queue, struct, time, random
from Network import Network
from Win import Win

UP = 259
RIGHT = 261
DOWN = 258
LEFT = 260
DEL = 127

class	Client():

	players	= {}
	posX = 1
	posY = 1

	def	__init__(self, name, host, port=4242):
		self.name = name
		self.win = Win(400, 400)
		self.posY = random.randrange(1, 8)
		self.posX = random.randrange(1, 8)
		self.host = host
		self.port = int(port)
		self.addr = host + ':' + str(port)
		self.turn = 0
		self.wait = False
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
		self.inputs = [self.sock]
		self.outputs = []

		# CE QUE JE DOIT RECEVOIR DU SERVEUR
		Network.setPlayerAddedCallback(self._playerAddedCallback)
		Network.setPlayerLeavedCallback(self._playerLeavedCallback)
		Network.setPlayerNameCallback(self._playerChangeNameCallback)
		Network.setMapCallback(self._playerAskMap)
		Network.setNextTurn(self._playerGetNextTurn)
		Network.setPlayerLetsPlay(self._playerLetsPlay)
		Network.setPlayerPositionChangeCallback(self._playerPositionChangeCallback)	

	def	_playerGetNextTurn(self, id, datas):
		self.turn = int(datas)
		# self.win.win.addnstr(21, 40, "Next turn incomming! ({})".format(self.turn), len("Next turn incomming! ({})".format(self.turn)))
		self.win.win.refresh()

	def	_playerLetsPlay(self, id, datas):
		self.turn = int(datas)
		self.wait = False
		# self.win.win.addnstr(22, 40, "It's your TURN! ({})".format(self.turn), len("It's your TURN! ({})".format(self.turn)))
		self.win.win.refresh()

	def _playerAskMap(self, id, datas):
		self.win.win.clear()
		if datas != None:
			self.map = datas
		self.win.win.addnstr(0, 0, self.map, len(self.map))
		self.win.win.addnstr(self.posX, self.posY, str(self.id), len(str(self.id)))
		# for ppl in self.player:

		self.win.win.refresh()

	def _playerPositionChangeCallback(self, id, datas):
		if id == self.id:
			self.posX = int(datas.split(":")[0])
			self.posY = int(datas.split(":")[1])
			self.wait = True
		else:
			self.player[id]["pos"] = datas
		self._playerAskMap(None, None)

	def _playerAddedCallback(self, id, datas):
		msg = "player joined the game: " + str(id)
		self.win.win.addnstr(20, 40, msg, len(msg))
		self.players[id] = {"name":""}
		self.players[id]["name"] = str(id)
		self.win.win.refresh()

	def _playerLeavedCallback(self, id, datas):
		msg = "Player {} disconnected.".format(id)
		self.win.win.addnstr(22, 40, msg, len(msg))
		self.win.win.refresh()
		del self.players[id]

	def _playerChangeNameCallback(self, id, datas):
		self.players[id]["name"] = datas

	def	_waitEvent(self):
		try:
			while True:
				try:
					readable, writable, exceptionnal = select.select(self.inputs, self.outputs, self.inputs, 0.1)
					if len(readable) != 0:
						if Network.Read(self.sock) == False:
							print >>sys.stderr, "Server Disconnected, exiting.."
							sys.exit(0)
					self._executeWinActions(self.win._nextTurn())
				except select.error, e:
					print >>sys.stderr, e
					time.sleep(1)
					sys.exit(0)
		except KeyboardInterrupt, e:
			print >>sys.stderr, e
			sys.exit(0)

	def	_executeWinActions(self, action):
		# self.win.win.addnstr(20, 40, str(self.wait), len(str(self.wait)))
		if self.wait == True:
			return False
		else:
			posY = self.posY
			posX = self.posX
			if action == LEFT:
				posY -= 1
			elif action == DOWN:
				posX += 1
			elif action == RIGHT:
				posY += 1
			elif action == UP:
				posX -= 1
			elif action == 127:
				sys.exit(0)
		self.wait = True
		Network.SendPlayerPosition(self.sock, self.id, str(posX) + ":" + str(posY))
		self.win.win.refresh()

client = Client(sys.argv[1], sys.argv[2], 4242)
client._waitEvent()

