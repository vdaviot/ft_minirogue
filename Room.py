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
from Cellar_automata import Cellar_automata
from Maze import Maze

class	Room():

	def	__init__(self):
		self.room_type = random.randrange(1, 3)
		self.row = random.randrange(10, 20)
		self.col = random.randrange(10, 40)
		self.area = self.row * self.col
		self.room = self.generate_room(self.room_type)

	def	__str__(self):
		return self.room.__str__()

	def	generate_room(self, type):
		if type == 1:
			self.algo = Cellar_automata(self.row, self.col, random.uniform(0.25, 0.70))
		elif type == 2:
			self.algo = Maze(self.row, self.col)
		return self.algo.map

for i in range(10):
	map = Room()
	print ("map {}:").format(i)
	print(map)