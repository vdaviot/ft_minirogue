# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Armor.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/21 22:22:09 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/21 22:22:15 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from faker import Factory
import random

ARMOR_PREFIX = ["Legendary","Epic" , "Unique", "Mystic", "Rare", "Quality", "Good", "Common", "", "Used", "Old", "Rusted", "Shitty", "Broken"]
ARMOR_TYPE = ["armor", "cap", "shirt", "plate", "chainmail", "leather", "brigandine", "scale armor", "lamellar armor", "laminar armor", "plated mail", "samurai armor", "ballistic vest", "vest", "interceptor armor"]
ARMOR_ATTRIBUTE = ["poison defense", "blindness protection", "blood resillience", "the crushed", "toxic resplenishment", "fire", "ice", "", "", "", "", "", "", "", "","", "", "", "", "light"]

class	Armor(Items):

	def	__init__(self):
		self.item = Items.__init__(self)
		fake = Factory.create(random.choice(['de_DE', 'fr_FR', 'nl_NL']))
		self.old_user = fake.name().split()[0]
		self.durability = random.randrange(20, 100)
		self.armor_type = random.choice(ARMOR_TYPE)
		self.armor_value = random.randrange(5, 20)
		self.rarity = random.randrange(1, 15)
		self.attribute = random.choice(ARMOR_ATTRIBUTE)
		self.armor_prefix = ARMOR_PREFIX[self.rarity]
		self.name = self.assemble_name().encode('utf-8')
		del self.fake

	def	__str__(self):
		return self.name

	def	randomize_attribute(self):
		return random.choice(ARMOR_ATTRIBUTE)

	def	get_rarity_prefixes(self, rarity):
		return ARMOR_PREFIX[rarity]

	def	assemble_name(self):
		if self.armor_prefix:
			armor = self.armor_prefix + " " + self.old_user + "'s " + self.armor_type
		else:
			armor = self.old_user + "'s " + self.armor_type
		if self.attribute != "":
			armor += " of " + self.attribute 
		return armor
