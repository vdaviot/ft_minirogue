# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    IA_movement.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/17 19:41:57 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/17 19:41:58 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

class	Ai_movement():

	def	__init__(self, entity, mapp):
		self.map = mapp
		self.attitude = "idle"
		self.los = False
		self.movement_list = []
		self.impaired_movement = False
		self.posX = entity.posX
		self.posY = entity.posY

	def	handle_movement(self):
		if self.attitude == "idle":
			self.idleBehavior()
		elif self.attitude == "attack" or self.los == True:
			self.attackBehavior()
		elif self.attitude == "escape"
			self.escapeBehavior()

	def idleBehavior(self):
		found = False
		while found == False and self.target == None:
			px, py = self.posX, self.posY
			rand = random.randrange(8)
			if rand == 1:
				px += 1
			elif rand == 2:
				px -= 1
			elif rand == 3:
				py += 1
			elif rand == 4:
				py -= 1
			elif rand in '5678':
				py = py
				px = px
			if self.map.map[py][px] == '.':
				self.posX = px;
				self.posY = py;
				found = True


	def attackBehavior(self, player_x, player_y):
		pass

	def escapeBehavior(self, player_x, player_y):
		pass

	def	check_case(self, x, y):
		if(x >= 0 and y >= 0 and x < len(self.Map.map[0]) and y < len(self.Map.map) and (self.Map.map[y][x] in '.+-')):
			self.posX = x
			self.posy = y
