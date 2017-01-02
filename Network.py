# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Network.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/29 18:54:53 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/29 18:54:54 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, select, sys, types, struct

class	Network():

	callbacks = {}

	def __init__(self):
		Network.callbacks = {}

# def _generatePlayerPositions(self, id, datas):
# 		for s in self.connected_clients:
# 			if s.id == id:
# 				posX = int(datas.split(":")[0])
# 				posY = int(datas.split(":")[1])
# 				print posX, posY
# 				while self._collisionCheck(posX, posY) == True:
# 					if posX > posY:
# 						posX += 1
# 					else:
# 						posY += 1
# 				s.posX = posX
# 				s.posY = posY
# 				position = str(s.posX) + ":" + str(s.posY)
# 				Network.SendPlayerPosition(s.socket, s.id, position)
# 				break
	# Client to Server Callbacks

	@staticmethod
	def setPlayerAddedCallback(callback):
		Network.callbacks["NP"] = callback

	@staticmethod
	def	setPlayerIdCallback(callback):
		Network.callbacks["ID"] = callback

	@staticmethod
	def	setMapCallback(callback):
		Network.callbacks["MA"] = callback

	@staticmethod
	def	setNextTurn(callback):
		Network.callbacks["NT"] = callback

	@staticmethod
	def setPlayerLeavedCallback(callback):
		Network.callbacks["PL"] = callback

	@staticmethod
	def	setServerGiveClientPositions(callback):
		Network.callbacks["EP"] = callback

	@staticmethod
	def	setOtherPlayerName(callback):
		Network.callbacks["NA"] = callback

	@staticmethod
	def setPlayerPositionChangeCallback(callback):
		Network.callbacks["PP"] = callback

	@staticmethod # AP Ask for position (Client)
	def	AskServerIfPosition(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "AP", id, action)

	@staticmethod # LP Let's Play
	def	playerSendGoServer(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "LP", id, action)

	@staticmethod # SP Player spawning position
	def	sendPlayerSpawningPosition(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "SP", id, action)

	@staticmethod # PP Player position
	def SendPlayerPosition(targetSocket, id, position):
		Network.sendWrapper(targetSocket, "PP", id, str(position))

	@staticmethod # NA Player name
	def SendPlayerName(targetSocket, id, name):
		Network.sendWrapper(targetSocket, "NA", id, name)


	
	# Server to Client Callbacks

	@staticmethod
	def	setPlayerAskForPosition(callback):
		Network.callbacks["AP"] = callback

	@staticmethod
	def	setPlayerSpawningPositionCallback(callback):
		Network.callbacks["SP"] = callback

	# @staticmethod
	# def	setPlayerNewIdCallback(callback):
	# 	Network.callbacks["PL"] = callback
		
	@staticmethod
	def	setPlayerLetsPlay(callback):
		Network.callbacks["LP"] = callback

	@staticmethod
	def setPlayerNameCallback(callback):
		Network.callbacks["NA"] = callback

	@staticmethod # NT Player Next Turn
	def	sendNextTurnPlayer(targetSocket, id, message):
		Network.sendWrapper(targetSocket, "NT", id, message)
		
	@staticmethod # EP Entities positions
	def	sendClientPositionList(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "EP", id, action)

	@staticmethod  # AP Ask for position (Server)
	def sendPlayerAnswerPositon(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "AP", id, action)

	@staticmethod # LP Player can play
	def	sendPlayerLetsPlay(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "LP", id, action)


	@staticmethod # PL Player leaved
	def SendPlayerLeaved(targetSocket, id):
		Network.sendWrapper(targetSocket, "PL", id, "")

	@staticmethod # Multiple AP
	def SendAddPlayer(targetSocket, id, name):
		Network.SendMultipleAddPlayer(targetSocket, name + "," + struct.pack("i", id) + ";")

	@staticmethod # AP Added player
	def SendMultipleAddPlayer(targetSocket, players):
		Network.sendWrapper(targetSocket, "NP", -1, players)

	@staticmethod # ID Player id
	def SendPlayerID(targetSocket, id):
		Network.sendWrapper(targetSocket, "ID", id, "")

	@staticmethod
	def GetPlayerID(targetSocket):
		targetSocket.recv(2)
		ret = targetSocket.recv(4)
		return struct.unpack("i", ret)[0]

	@staticmethod # MA Map 
	def	SendMapPlayer(targetSocket, map):
		Network.sendWrapper(targetSocket, "MA", -1, map)



	# Unused at the moment

	# @staticmethod
	# def	setPlayerChoosedAction(callback):
	# 	Network.callbacks["CA"] = callback

	# @staticmethod # CA Player has choosed an action
	# def	sendPlayerChoosedAction(targetSocket, id, action): 
	# 	Network.sendWrapper(targetSocket, "CA", id, action)



	# Utility Method

	@staticmethod # Wrapper to send nicely formatted messages
	def sendWrapper(socket, cmd, id, message):
		socket.send(cmd + struct.pack("i", id) + message + "\x99")

	@staticmethod # Reading method for client and server to talk
	def Read(targetSocket):
		datas = targetSocket.recv(4096)
		if not datas:
			return False
		cmds = datas.split('\x99')
		# print cmds
		for cmd in cmds:
			key = cmd[:2]
			if not key:
				continue
			strid = cmd[2:6]
			id = struct.unpack("i", strid)[0]
			cmd = cmd[6:]
			if key == "NP":
				for players in cmd.split(';'):
					if players == "":
						continue
					playerName = players.split(',')[0]
					id = struct.unpack("i", players.split(',')[1])[0]
					Network.callbacks[key](id, playerName)
			else:
				Network.callbacks[key](id, cmd)
		return True
