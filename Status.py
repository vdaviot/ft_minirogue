# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Status.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/16 12:51:01 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/16 12:51:03 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class	Status():

	def __init__(self, status=None):
		if status != None:
			self.name = status
			self.duration = self.get_duration(status)
			self.damages = self.get_damages(status)
		else:
			self.name = None
			self.duration = 0
			self.damages = 0

	def	new_status(self, status, entity):
		entity.status = status
		entity.status.duration = self.get_duration(status)
		entity.status.damages = self.get_damages(status)

	def refresh_status(self, entity, run):
		if entity.status == "poisonned":
			entity.status = self.poison(entity)
		elif entity.status == "bleeding":
			entity.status = self.bleed(entity)
		elif entity.status == "broken_arm":
			entity.status = self.broken_arm(entity)
		elif entity.status == "broken_leg":
			entity.status = self.broken_leg(entity)
		elif entity.status == "blind":
			entity.status = self.blind(entity)
		if entity.hp < 1:
			return self.death(entity, run)
		return ""

	def get_duration(self, status):
		if status == "poisonned":
			return 5
		elif status == "bleeding":
			return 3
		elif status == "broken leg" or "broken arm":
			return 10
		elif status == "blind":
			return 12
		else:
			return 0

	def	get_damages(self, status):
		if status == "poisonned":
			return 1
		elif status == "bleeding":
			return 1
		else:
			return 0

	def	death(self, entity, run):
		if entity.name == sys.argv[1]:
			return False
		else:
			entity.state = "{} has died.".format(entity.name)
			return True

	def	poison(self, entity):
		if entity.status.duration > 0:
			entity.status.duration -= 1
			entity.hp -= self.damages
		else:
			entity.status = ""
		return entity.status

	def bleed(self, entity):
		if entity.status.duration > 0:
			entity.status.duration -= 1
			entity.hp -= self.damages
		else:
			entity.status = ""
		return entity.status

	def	broken_leg(self, entity):
		if entity.status.duration > 0:
			entity.status.duration -= 1
			entity.move = -entity.move
		else:
			entity.status = ""
			entity.move = True
		return entity.status


	def	blind(self, entity):
		if entity.status.duration > 0:
			entity.status.duration -= 1
			entity.precision = entity.max_precision - 50
		else:
			entity.status = ""
			entity.precision = entity.max_precision


	def	broken_arm(self, entity):
		if entity.status.duration > 0:
			entity.status.duration -= 1
			entity.attack = -entity.attack
		else:
			entity.status = ""
			entity.attack = True
		return entity.status
