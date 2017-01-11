# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Save.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/01/11 09:32:29 by vdaviot           #+#    #+#              #
#    Updated: 2017/01/11 09:32:31 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os, time

class		Save():

	def	__init__(self):
		self.directory = "save/"
		if os.path.isdir("save") == False:
			os.mkdir(self.directory)

	def	_saveCaracter(self, profile):
		filename = self.directory + profile.name + str(time.time())
		file = open(filename, 'w+')
		toWrite = profile._saveFormatting()
		print toWrite
		file.write(profile._saveFormatting())
		file.close()
