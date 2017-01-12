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
		if os.path.isdir(self.directory) == False:
			os.mkdir(self.directory)

	def	_saveCaracter(self, profile):
		filename = self.directory + profile.name
		file = open(filename, 'w+')
		toWrite = profile._saveFormatting()
		file.write(profile._saveFormatting())
		file.close()

	def	_EraseAllSave(self):
		for file in os.listdir(self.directory):
			os.remove(self.directory + file)
		os.rmdir(self.directory)
