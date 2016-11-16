# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Weapon.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/16 14:10:07 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/16 14:10:08 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from faker import Factory

class Weapon():

	def __init__(self):
		fake = Factory.create('fr_FR')
		self.old_user = fake.name().split()[0]
		self.weapon_type = random.choice(["dagger", "sword", "greatsword", "ultra-greatsword", "slingshot", "axe", "great-axe", "cleaver", "hammer", "great-hammer", "knife"])
		self.damages = random.randrange(5, 20)
		self.maniability = random.randrange(40, 100)
		self.weight = self.randomize_weight(random.choice('1234'))
		self.durability = random.randrange(45, 100)
		self.rarity = random.randrange(1, 15)
		self.attribute = self.randomize_attribute()
		self.weapon_prefix = self.get_rarity_prefixes(self.rarity)
		self.name = self.assemble_name()

	def	assemble_name(self):
		wp = self.weapon_prefix + " " + self.old_user + "'s " + self.weapon_type
		if self.attribute != "":
			wp = wp + " of " + self.attribute 
		return wp


	def	randomize_attribute(self):
		return random.choice(["poison", "blindness", "blood", "the crushed", "toxic", "burning", "freezing", "", "", "", "", "", "", "", "","", "", "", "", "light"])

	def	get_rarity_prefixes(self, rarity):
		prefixes = ["", "Legendary","Epic" , "Unique", "Mystic", "Rare", "Quality", "Good", "Common", "", "Used", "Old", "Rusted", "Shitty", "Broken", ""]
		if rarity > 0:
			return prefixes[rarity]

	def	randomize_weight(self, wtype):
		if wtype == 1:
			random.randrange(5)
		if wtype == 2:
			random.randrange(8)
		if wtype == 3:
			random.randrange(10)
		if wtype == 4:
			random.randrange(20)