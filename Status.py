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

class	Status():

	def __init__(self, win, status=None):
		if status != None:
			self.status = status
			self.duration = self.get_duration(status)
			self.damages = self.get_damages(status)
		else:
			self.status = None
			self.duration = 0
			self.damages = 0

	def	new_status(self, status, entity):
		entity.status = status
		entity.status.duration = self.get_duration(status)
		entity.status.damages = self.get_damages(status)

	def refresh_status(self, entity):
		if entity.status == "poisonned":
			return self.poison(entity)
		if entity.status == "bleeding":
			return self.bleed(entity)
		if entity.status == "broken_arm":
			return self.broken_arm(entity)
		if entity.status == "broken_leg":
			return self.broken_leg(entity)
		if entity.status == "blind":
			return self.blind(entity)

	def get_duration(self, status):
		if status == "poisonned":
			return 5
		elif status == "bleeding":
			return 3
		elif status == "broken leg":
			return 10
		elif status == "broken arm":
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

	def	poison(self, entity):
		if entity.status == "poisonned":
			if entity.status.duration > 0:
				entity.status.duration -= 1
				entity.hp -= self.damages
			else:
				entity.status = None
		return entity.status

	def bleed(self, entity):
		if entity.status == "bleeding":
			if entity.status.duration > 0:
				entity.status.duration -= 1
				entity.hp -= self.damages
			else:
				entity.status = None
		return entity.status

	def	broken_leg(self, entity):
		if entity.status == "broken_leg":
			if entity.status.duration > 0:
				entity.status.duration -= 1
				entity.move = !entity.move
			else:
				entity.status = None
				entity.move = True
		return entity.status


	def	blind(self, entity):
		if entity.status == "blind":
			if entity.status.duration > 0:
				entity.status.duration -= 1
				entity.precision = entity.max_precision - 50
			else:
				entity.status = None
				entity.precision = entity.max_precision


	def	broken_arm(self, entity):
		if entity.status == "broken_arm":
			if entity.status.duration > 0:
				entity.status.duration -= 1
				entity.attack = !entity.attack
			else:
				entity.status = None
				entity.attack = True
		return entity.status
