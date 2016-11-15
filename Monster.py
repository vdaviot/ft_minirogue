# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Monster.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/15 17:06:26 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/15 17:06:27 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

class	Monster():

	def	__init__(self, mapp, one=0):
		self.map = mapp
		if one == 0:
			self.boss = True
			self.skin = "1"
			self.hp = 16
			self.armor = 9
			self.strengh = 12
			self.monster_type = 10
		else:
			self.init_random_monster()
			self.hp = random.randrange(8)
			self.boss = False
		self.status = "Monster type {} is looking for a target.".format(self.monster_type)
		self.random_position_monster()
			

	def	init_random_monster(self):
		self.monster_type = random.randrange(10)
		self.skin = random.choice('@%&^?')
		self.strengh = random.randrange(11)
		self.armor = random.randrange(8)

	def	random_position_monster(self):
		self.posX = random.randrange(59)
		self.posY = random.randrange(14)
		while self.map.map[self.posY][self.posX] != '.':
			self.posX = random.randrange(59)
			self.posY = random.randrange(14)