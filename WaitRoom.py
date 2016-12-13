# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    WaitRoom.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/28 16:51:05 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/28 16:51:07 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class WaitRoom():

	def __init__(self):
		self.room = []
		self.room.append("##########\n")
		self.row = len(self.room[0]) - 1
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("#........#\n")
		self.room.append("##########\n")
		self.col = len(self.room)
	
	def	__str__(self):
		map = ""
		for line in self.room:
			map += line
		return map