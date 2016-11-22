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
from Status import Status
import sys

class	Player(Status):

	def __init__(self, Map):
		if sys.argv[1]:
			self.name = sys.argv[1]
		else:
			self.name = "Shayn"
		self.skin = "8"
		self.alive = True
		
		self.hp = 12
		self.level = 1
		self.gold = 0
		self.armor = 5
		self.strength = 11
		self.dexterity = 8
		self.precision = 80
		self.max_precision = 80
		self.endurance = 10
		self.vitality = 10

		self.posX = Map.spawnX
		self.posY = Map.spawnY
		self.Map = Map
		self.status = Status()
		self.state = ""
		self.target = None
		self.movement_allowed = True

	def	move(self, event):
		if self.movement_allowed == True:
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
				self.target.target = "player"
				proba = random.randrange(15)
				if proba < self.strength:
					damages = max(self.strength - self.target.armor, 0)
					damages = abs(damages)
					self.target.hp -= damages
					if self.target.hp <= 0:
						self.target.state = "{} got hit for {} damages and died!".format(self.target.name, damages)
					else:
						self.target.state = "{} got hit for {} damages!".format(self.target.name, damages)
				proba = random.randrange(15)
				if proba < self.target.strength:
					damages = self.target.strength - self.armor
					self.hp -= damages
					if self.hp < 1:
						self.state = "{} died!".format(self.name)
					else:
						self.state = "{} got hit for {} damages!".format(self.name, damages)
				else:
					self.state = "{} have been missed!".format(self.name)

	def	check_attack_case(self, monster_table):
		for m in monster_table.table:
			if abs(m.posX - self.posX) + abs(m.posY - self.posY) == 1 and m.hp > 0:
				return m

	def check_case(self, x, y):
		if(x >= 0 and y >= 0 and x < len(self.Map.map[0]) and y < len(self.Map.map) and (self.Map.map[y][x] in '.+-')):
			self.posX = x
			self.posY = y
