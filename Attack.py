# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Attack.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/16 12:51:14 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/16 12:51:16 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Attack():

	def __init__(self, entity, weapon):
		self.entity = entity
		self.weapon = weapon
		self.damages = self.potential_damages()
		self.precision = self.potential_precision()
		self.attack_counter = round(self.precision / 100) if > 1 else 1

	def	potential_damages(self):
		return int(self.weapon.damages * (self.entity.strength / 3))

	def	potential_precision(self):
		return int((0.8 / (self.entity.strength / self.entity.dexterity)) / ((1 / (self.weapon.maniability ** 2 / 4)) / (self.entity.dexterity / 40)) * (self.entity.strength / (self.weapon.weight * 4)))
