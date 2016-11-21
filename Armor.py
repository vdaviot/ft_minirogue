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

class	Armor():
	def	__init__(self):
		fake = Factory.create(random.choice(['de_DE', 'fr_FR', 'sv_SE', 'el_GR', 'ru_RU']))
		self.old_user = fake.name().split()[0]
		self.durability = random.randrange(20, 100)
		self.armor_type = random.choice(["armor", "cap", "shirt", "plate", "chainmail", "leather", "brigandine", "scale armor", "lamellar armor", "laminar armor", "plated mail", "samurai armor", "ballistic vest", "vest", "interceptor armor"])
		self.armor_value = random.randrange(5, 20)
		self.elemental_resistance = self.random_element()
		self.rarity = random.randrange(1, 15)
		self.attribute = self.randomize_attribute()
		self.armor_prefix = self.get_rarity_prefixes(self.rarity)
		self.name = self.assemble_name()

	def	random_element(self):
		return random.choice(['poison', 'bleed', 'heavy'])

	def	randomize_attribute(self):
		return random.choice(["poison defense", "blindness protection", "blood resillience", "the crushed", "toxic resplenishment", "fire", "ice", "", "", "", "", "", "", "", "","", "", "", "", "light"])

	def	get_rarity_prefixes(self, rarity):
		prefixes = ["", "Legendary","Epic" , "Unique", "Mystic", "Rare", "Quality", "Good", "Common", "", "Used", "Old", "Rusted", "Shitty", "Broken", ""]
		if rarity > 0:
			return prefixes[rarity]

	def	assemble_name(self):
		wp = self.armor_prefix + " " + self.old_user + "'s " + self.armor_type
		if self.attribute != "":
			wp = wp + " of " + self.attribute 
		return wp
