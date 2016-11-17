# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Monster_table.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/15 17:06:35 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/15 17:06:36 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Mapp import Map_generator
from Monster import Monster
import random

class	Monster_table():

	def __init__(self, mapp):
		self.table = []
		self.map = mapp
		for i in range(10):
			if i == 9:
				self.table.append(Monster(self.map, 0))
			else:
				self.table.append(Monster(self.map, 1))

	def monster_movement(self):
		for i in range(len(self.table)):
			self.monster_pathfinder(self.table[i])

	def monster_pathfinder(self, monster):
		found = False
		while found == False and monster.target == None:
			px, py = monster.posX, monster.posY
			rand = random.randrange(7)
			if rand == 1:
				px += 1
			elif rand == 2:
				px -= 1
			elif rand == 3:
				py += 1
			elif rand == 4:
				py -= 1
			elif rand == 5:
				py = py
				px = px
			elif rand == 6:
				py = py
				px = px
			elif rand == 7:
				py = py
				px = px
			if self.map.map[py][px] == '.':
				monster.posX = px;
				monster.posY = py;
				found = True

