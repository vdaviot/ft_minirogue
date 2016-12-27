# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    UserInterface.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/12/27 12:58:37 by vdaviot           #+#    #+#              #
#    Updated: 2016/12/27 12:58:42 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import curses, time, sys, locale

class		UserInterface():

	def	__init__(self, win, inventory, map, group):
		self.win = win
		self.inventory = inventory
		self.map = map
		self.group = group
		self._initColorDisplay()
		self._initGroupDisplay()
		self._initMapDisplay()
		self._initStuffDisplay()
		self._initInventoryDisplay()
		self._initChatDisplay()

	def	_initColorDisplay(self):
		pass

	def	_initGroupDisplay(self, group):
		pass

	def	_initMapDisplay(self, map):
		pass

	def	_initStuffDisplay(self, stuff):
		pass

	def	_initInventoryDisplay(self, inventory):
		pass

	def	_initChatDisplay(self):
		pass