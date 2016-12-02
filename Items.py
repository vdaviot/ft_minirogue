# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Items.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/12/01 00:32:32 by vdaviot           #+#    #+#              #
#    Updated: 2016/12/01 00:32:34 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
from Currency import Currency
from Armor import Armor
from Weapon import Weapon
from Consummable import Consummable

class	Items():

	def	__init__(self, name, price):
		self.price = price
		self.name = name


# 	self.itemType = random.randrange(0, 4)
# 	if self.itemType == 1:
# 		self._initWeapon()
# 	elif self.itemType == 2:
# 		self._initArmor()
# 	elif self.itemType == 3:
# 		self._initCurrency()
# 	else:
# 		self._initConsummable()
# 	self.itemWeight = self.item.weight
# 	self.itemNumber = self.item.number

# def	__str__(self):
# 	return self.name

# def	_initWeapon(self):
# 	return self.item = Weapon()

# def	_initArmor(self):
# 	return self.item = Armor()

# def	_initCurrency(self):
# 	return self.item = Currency()

# def	_initConsummable(self):
# 	return self.item = Consummable()