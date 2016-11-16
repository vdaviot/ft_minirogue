# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Monster_table.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/15 17:06:35 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/15 17:06:36 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Mapp import Map_generator
from Monster import Monster

class	Monster_table():

	def __init__(self, mapp):
		self.table = []
		self.map = mapp
		for i in range(10):
			if i == 9:
				self.table.append(Monster(self.map, 0))
			else:
				self.table.append(Monster(self.map, 1))

