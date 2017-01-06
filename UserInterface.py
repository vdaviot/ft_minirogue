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
from Win import Win

class		UserInterface():

	def	__init__(self, win, map, lenx=400, leny=400, inventory=None, group=None):
		self.lenx = lenx
		self.leny = leny
		self.win = Win(lenx, leny)
		self.inventory = inventory
		self.map = map
		self.group = group
		# self._initColorDisplay()
		# self.groupDisplay()
		# self._initMapDisplay()
		# self._playerDisplay()
		# self._initStuffDisplay()
		# self._initInventoryDisplay()
		# self._initChatDisplay()

	def	_initColorDisplay(self):
		pass

	def	_generateBar(self, entity):
	# Stat bar generation
		maxSize = 30
		bar = "["
		n = float(entity.maxHp) / float(entity.hp) * maxSize
		for p in range(maxSize):
			if n - i >= 0:
				bar += "0"
			else:
				bar += " "
		bar += "]"
		return bar


	def	playerDisplay(self, player):
		healthbar = self._generateBar(player.hp, player.maxHp)
		self.win.win.addnstr(leny / 2, lenx / 2, player.name, len(player.name))
		self.win.win.addnstr(leny / 2 + 1, lenx / 2, healthbar, len(healtbar))


	def	groupDisplay(self, group):
	# Print each teammember like shayn: 10/10hp rdy: [√] or [x]
		i = 0
		for ppl in group:
			self.win.win.addnstr(40 + i, self.map.mapCol + 20, ppl.__str__(), len(ppl.__str__()))
			i += 1

	def	_initMapDisplay(self, map):
	 # Print each line of the map for screenlen / 2 
	 # This way the map will always center the main character
	 	i = 0
		for floor in self.rawmap:
			self.win.win.addnstr(2, 2 + i, floor, len(floor))
			i += 1
			

	def	_initStuffDisplay(self, stuff):
		#WHEN DONE
		pass

	def	_initInventoryDisplay(self, inventory):
		#WILL DO WHEN INVENTORY DONE
		pass

	def	_initChatDisplay(self):
		# Chat / combat log WILL DO LATELY
		pass









		##########################################################################
		#                                               #		Stuff
		#                                               #
		#                                               # Head:
		#                                               # Body:
		#                                               # Gloves:
		#                         GAME                  # Pants:
		#                                               # Boots:
		#                                               # rWeapon:
		#                                               # lWeapon:
		#                                               #
		#                                               #  press i for inventory  
		###########################################################################
		#                                #    Player    #		Group Display
		#                     CHAT       #              # 	
		#                      or        #              # shayn: 15/21hp
		#                  combat log    #              # jderlmar: 21/23hp
		#                                #              #
		#                                #              #
		###########################################################################