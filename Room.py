# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Room.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/21 14:51:38 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/21 14:51:40 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
from Cellar_Automata import Cellar_Automata

class	Room():

	def	__init__(self):
		self.room_type = random.randrange(1, 2)
		self.row = random.randrange(10, 40)
		self.col = random.randrange(10, 40)
		self.area = self.row * self.col
		self.room = self.generate_room(self.room_type)

	def	generate_room(self, type):
		if type == 1:
			self.algo = Cellar_Automata(self.row, self.col, random.uniform(0.42, 0.56))
		if type == 2:
			self.algo = Maze(self.row, self.col)
		return self.algo.map
		