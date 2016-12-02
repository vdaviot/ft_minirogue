# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    LootTable.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/12/01 21:22:57 by vdaviot           #+#    #+#              #
#    Updated: 2016/12/01 21:23:00 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

NONE = 60
WHITE = 20
GREEN = 10
BLUE = 6
PURPLE = 3
ORANGE = 1

class	LootTable(Items):

	def	__init__(self, number = 100, level = 1):
		self._initMainTable(number)

	def	_initMainTable(self, number):
		self.mainTable = []
		white = round((number / 100) * WHITE)
		green = round((number / 100) * GREEN)
		blue = round((number / 100) * BLUE)
		purple = round((number / 100) * PURPLE)
		orange = round((number / 100) * ORANGE)
		for i in range(number):
			if i in range(0, white):
				self.mainTable.append()
			if i in range(0, green):
				self.mainTable.append()
			if i in range(0, blue):
				self.mainTable.append()
			if i in range(0, purple):
				self.mainTable.append()
			if i in range(0, orange):
				self.mainTable.append()




