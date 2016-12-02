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
	def sendWrapper(socket, cmd, id, message):
		socket.send(cmd + struct.pack("i", id) + message + "\x99")

	@staticmethod
	def setPlayerPositionChangeCallback(callback):
		Network.callbacks["PP"] = callback

	@staticmethod
	def SendPlayerPosition(targetSocket, id, position):
		Network.sendWrapper(targetSocket, "PP", id, str(position))

	@staticmethod
	def setPlayerNameCallback(callback):
		Network.callbacks["NA"] = callback

	@staticmethod
	def SendPlayerName(targetSocket, id, name):
		Network.sendWrapper(targetSocket, "NA", id, name)

	@staticmethod
	def setPlayerLeavedCallback(callback):
		Network.callbacks["PL"] = callback

	@staticmethod
	def SendPlayerLeaved(targetSocket, id):
		try:
			Network.sendWrapper(targetSocket, "PL", id, "")
		except socket.error as e:
			print >>sys.stderr, e

	@staticmethod
	def setPlayerAddedCallback(callback):
		Network.callbacks["AP"] = callback

	@staticmethod
	def SendAddPlayer(targetSocket, id, name):
		Network.SendMultipleAddPlayer(targetSocket, name + "," + struct.pack("i", id) + ";")

	@staticmethod
	def SendMultipleAddPlayer(targetSocket, players):
		Network.sendWrapper(targetSocket, "AP", -1, players)

	@staticmethod
	def SendPlayerID(targetSocket, id):
		Network.sendWrapper(targetSocket, "ID", id, "")

	@staticmethod
	def GetPlayerID(targetSocket):
		targetSocket.recv(2)
		ret = targetSocket.recv(4)
		return struct.unpack("i", ret)[0]

	@staticmethod
	def	setMapCallback(callback):
		Network.callbacks["MA"] = callback

	@staticmethod
	def	SendMapPlayer(targetSocket, map):
		Network.sendWrapper(targetSocket, "MA", -1, map)

	@staticmethod
	def Read(targetSocket):
		try:
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
		except:
			return False