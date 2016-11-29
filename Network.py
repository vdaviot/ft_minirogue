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
	def SendPlayerPosition(targetSocket, id, position):
		targetSocket.send("PP" + struct.pack("i", id) + str(position))

	@staticmethod
	def setPlayerNameCallback(callback):
		Network.callbacks["NA"] = callback

	@staticmethod
	def SendPlayerName(targetSocket, id, name):
		targetSocket.send("NA" + struct.pack("i", id) + name)

	@staticmethod
	def setPlayerLeavedCallback(callback):
		Network.callbacks["LP"] = callback

	@staticmethod
	def SendLeavedPlayer(targetSocket, id):
		targetSocket.send("LP" + struct.pack("i", id))

	@staticmethod
	def setPlayerAddedCallback(callback):
		Network.callbacks["AP"] = callback

	@staticmethod
	def SendAddPlayer(targetSocket, id, name):
		Network.SendMultipleAddPlayer(targetSocket, name + "," + struct.pack("i", id) + ";")

	@staticmethod
	def SendMultipleAddPlayer(targetSocket, players):
		targetSocket.send("AP" + "BBBB" + players)

	@staticmethod
	def SendPlayerID(targetSocket, id):
		print "sended id: ", id
		targetSocket.send("ID" + struct.pack("i", int(id)))

	@staticmethod
	def GetPlayerID(targetSocket):
		targetSocket.recv(2)
		ret = targetSocket.recv(4)
		return struct.unpack("i", ret)[0]


	@staticmethod
	def Read(targetSocket):
		try:
			key = targetSocket.recv(2)
			if not key:
				return False
			print "key = " + key
			strid = targetSocket.recv(4)
			print "str id = " + strid
			id = struct.unpack("i", strid)[0]
			datas = targetSocket.recv(1024)
			if not datas:
				return False
			print >>sys.stderr, 'New message: "{}" from {}'.format(datas, targetSocket.getpeername())
			if key == "AP":
				for players in datas.split(';'):
					if players == "":
						continue
					playerName = players.split(',')[0]
					id = struct.unpack("i", players.split(',')[1])[0]
					Network.callbacks[key](id, playerName)
			else:
				Network.callbacks[key](id, datas)
			return True
		except:
			return False