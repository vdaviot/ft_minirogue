# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    player.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/15 17:06:03 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/15 17:06:04 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from curses import *
import random

class	Player():

	def __init__(self, Map):
		self.skin = "8"
		self.hp = 12
		self.alive = True
		self.in_level = 0
		self.strengh = 10
		self.armor = 5
		self.posX = Map.spawnX
		self.posY = Map.spawnY
		self.Map = Map
		self.status = ""
		self.inventory_open = False
		self.target = None

	def	move(self, event):
		if event == KEY_UP:
			self.check_case(self.posX, self.posY - 1)
		if event == KEY_DOWN:
			self.check_case(self.posX, self.posY + 1)
		if event == KEY_LEFT:
			self.check_case(self.posX - 1, self.posY)
		if event == KEY_RIGHT:
			self.check_case(self.posX + 1, self.posY)

	def actions(self, key, monster_table):
		if(key == 32):
			self.target = self.check_attack_case(monster_table)
			if self.target:
				proba = random.randrange(15)
				if proba < self.strengh:
					damages = max(self.strengh - self.target.armor, 0)
					self.target.hp -= damages
					if self.target.hp <= 0:
						self.target.status = "Monster type {} got hit for {} damages and died!".format(self.target.monster_type, damages)
					else:
						self.target.status = "Monster type {} got hit for {} damages!".format(self.target.monster_type, damages)
				proba = random.randrange(15)
				if proba < self.target.strengh:
					damages = self.target.strengh - self.armor
					self.hp -= damages
					self.status = "You've got hit for {}!".format(damages)
				else:
					self.status = "You've been missed!"


	def	check_attack_case(self, monster_table):
		for m in monster_table.table:
			if abs(m.posX - self.posX) + abs(m.posY - self.posY) == 1 and m.hp > 0:
				return m

	def check_case(self, x, y):
		if(x >= 0 and y >= 0 and x < len(self.Map.map[0]) and y < len(self.Map.map) and (self.Map.map[y][x] == '.' or self.Map.map[y][x] == '+')):
			self.posX = x
			self.posY = y
