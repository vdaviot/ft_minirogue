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
from Mapp import Map_generator
from faker import Factory
from Status import Status

BOSS_SUFFIX = [", the One Legged", ", the Mad Scientist", ", the Abobination", ", the Sinful", ", the Giant", ", the Lost", ", the Fallen", ", the Archangel", ", the Juggernaut", ", the Dreadful", ", the Ivory King", 
", the God of all Things", ", the Unstoppable", ", the Green", ", the Unborn", ", the Eternal", ", the Follower", ", the Corruptor", ", the Flesheater", ", the Maneater", ", the Bonehunter", ", Lord of the Lost Souls", ", Master of the Pit", ", the Tainted Soul", ", the Immaterial"]
BOSS_PREFIX = []

MONSTER_NAME = []
MONSTER_SUFIX = []
MONSTER_PREFIX = []
class	Monster():

	def	__init__(self, mapp, one=0):
		generator = Factory.create('nl_NL')
		self.map = mapp
		self.level = 1
		if one == 0:
			self.boss = True
			self.skin = "1"
			self.hp = random.randrange(10, 30 + self.level * 2)
			self.armor = random.randrange(4, 10 + round(self.level / 2))
			self.precision = random.randrange(40, 100 + (self.level * 15))
			self.max_precision = self.precision
			self.strength = random.randrange(7 + self.level, 13 + self.level)
			self.dexterity = random.randrange(6 + self.level, 12 + self.level)
			self.endurance = random.randrange(6 + self.level, 14 + self.level)
			self.movement_allowed = True
			self.monster_type = 10
			self.name = self.generate_bossname(generator)
		else:
			self.name = self.generate_monstername()
			self.init_random_monster()
			self.hp = random.randrange(4, 12 + self.level)
			self.boss = False
		self.state = "{} is looking for a target.".format(self.name)
		self.target = None
		self.status = Status()
		self.random_position_monster()
			

	def	generate_bossname(self, generator):
		name = generator.name().split()[0]
		suffix = random.choice([", the one legged", ", the mad scientist", ", the abobination", ", the sinful", ", the giant", ", the lost", ", the fallen", ", the archangel"])
		prefix = random.choice(["Old ", "Sadic ", "", "", "Father ", ])
		return prefix + name + suffix

	def	generate_monstername(self):
		name = random.choice(["Bat", "Zombie", "Rat", "Salamander", "Bear", "Ghoul", "Fdp"])
		suffix = random.choice(["blue ", "red ", "green ", "yellow ", "", "", "", "", "", "", "", "", ""])
		prefix = random.choice(["Angry ", "Hungry ", "Raging ", "Bad ass ", "Flying ", "Giant "])
		return prefix + suffix + name

	def	init_random_monster(self):
		self.monster_type = random.randrange(10)
		self.skin = random.choice('@%&^?')
		self.strength = random.randrange(11)
		self.armor = random.randrange(8)

	def	random_position_monster(self):
		self.posX = random.randrange(59)
		self.posY = random.randrange(14)
		while self.map.map[self.posY][self.posX] != '.':
			self.posX = random.randrange(59)
			self.posY = random.randrange(14)
