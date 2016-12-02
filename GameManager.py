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

class		GameManager():

	def	__init__(self, name="Shayn's server", addr="localhost:4242"):

		self.server = Server(name, addr)
		self.wait_room = WaitRoom()
		self.level = Level()
		self.nlevel = 1
		self.main_player = PlayerCreation()
		self.player = []

	

	def	_NewPlayer(self):
		return PlayerCreation()

	def	_Return_Waitroom(self):
		return self.wait_room



