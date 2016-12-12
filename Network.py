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

	@staticmethod
	def setPlayerPositionChangeCallback(callback):
		Network.callbacks["PP"] = callback

	@staticmethod
	def	setPlayerLetsPlay(callback):
		Network.callbacks["LP"] = callback

	@staticmethod
	def	setPlayerSpawningPositionCallback(callback):
		Network.callbacks["SP"] = callback

	@staticmethod
	def	setNextTurn(callback):
		Network.callbacks["NT"] = callback

	@staticmethod
	def setPlayerNameCallback(callback):
		Network.callbacks["NA"] = callback

	@staticmethod
	def	setPlayerChoosedAction(callback):
		Network.callbacks["CA"] = callback

	@staticmethod
	def setPlayerLeavedCallback(callback):
		Network.callbacks["PL"] = callback

	@staticmethod
	def setPlayerAddedCallback(callback):
		Network.callbacks["AP"] = callback

	@staticmethod
	def	setPlayerIdCallback(callback):
		Network.callbacks["ID"] = callback

	@staticmethod
	def	setMapCallback(callback):
		Network.callbacks["MA"] = callback

	@staticmethod
	def	setPlayerIdCallback(callback):
		Network.callbacks["ID"] = callback

	@staticmethod # SP Player spawning position
	def	sendPlayerSpawningPosition(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "SP", id, action)

	@staticmethod # LP Player can play
	def	sendPlayerLetsPlay(targetSocket, id, action):
		Network.sendWrapper(targetSocket, "LP", id, action)

	@staticmethod # CA Player has choosed an action
	def	sendPlayerChoosedAction(targetSocket, id, action): 
		Network.sendWrapper(targetSocket, "CA", id, action)

	@staticmethod # NT Player Next Turn
	def	sendNextTurnPlayer(targetSocket, id, message):
		Network.sendWrapper(targetSocket, "NT", id, message)

	@staticmethod # Wrapper to send nicely formatted messages
	def sendWrapper(socket, cmd, id, message):
		socket.send(cmd + struct.pack("i", id) + message + "\x99")

	@staticmethod # PP Player position
	def SendPlayerPosition(targetSocket, id, position):
		Network.sendWrapper(targetSocket, "PP", id, str(position))

	@staticmethod # NA Player name
	def SendPlayerName(targetSocket, id, name):
		Network.sendWrapper(targetSocket, "NA", id, name)

	@staticmethod # PL Player leaved
	def SendPlayerLeaved(targetSocket, id):
		try:
			Network.sendWrapper(targetSocket, "PL", id, "")
		except socket.error as e:
			print >>sys.stderr, e

	@staticmethod
	def SendAddPlayer(targetSocket, id, name):
		Network.SendMultipleAddPlayer(targetSocket, name + "," + struct.pack("i", id) + ";")

	@staticmethod # AP Added player
	def SendMultipleAddPlayer(targetSocket, players):
		Network.sendWrapper(targetSocket, "AP", -1, players)

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

	@staticmethod
	def Read(targetSocket):
		datas = targetSocket.recv(4096)
		if not datas:
			return False
		cmds = datas.split('\x99')
		print cmds
		for cmd in cmds:
			key = cmd[:2]
			if not key:
				continue
			strid = cmd[2:6]
			id = struct.unpack("i", strid)[0]
			cmd = cmd[6:]
			if key == "AP":
				for players in cmd.split(';'):
					if players == "":
						continue
					playerName = players.split(',')[0]
					id = struct.unpack("i", players.split(',')[1])[0]
					Network.callbacks[key](id, playerName)
			else:
				Network.callbacks[key](id, cmd)
		return True
