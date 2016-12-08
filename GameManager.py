# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    GameManager.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/28 16:36:36 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/28 16:36:38 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Server import Server
from WaitRoom import WaitRoom
import socket, select, sys, types, struct, time

class		GameManager():

	def	__init__(self, name="Shayn's server", addr="localhost", port=4242):

		self.waitRoom = WaitRoom()
		self.server = Server(addr, port, self.waitRoom.map)
		# self.level = Level()
		self.nLevel = 1
		# self.main_player = PlayerCreation()
		self.player = []

	def	_NewPlayer(self):
		return PlayerCreation()

	def	_Return_Waitroom(self):
		return self.wait_room

	def	_run(self):
		while True:
			self.server._waitEvent()


game = GameManager()
game._run()