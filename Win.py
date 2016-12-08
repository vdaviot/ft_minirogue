# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Win.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/12/08 17:33:22 by vdaviot           #+#    #+#              #
#    Updated: 2016/12/08 17:33:24 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import curses, locale, sys

UP = 259
RIGHT = 261
DOWN = 258
LEFT = 260
DEL = 127

class	Win():

	def	__init__(self, row, col):
		self.row = row
		self.col = col
		stdscr = curses.initscr()
		self.win = curses.newwin(col, row, 0, 0)
		self.win.keypad(1)
		self.run = True
		self.event = None

	def	_run(self):
		self.event = self.win.getch()
		if self.event == DEL:
			self.run == False
			self.win.endwin()
			sys.exit(0)
		elif self.event == UP:
			return UP
		elif self.event == DOWN:
			return DOWN
		elif self.event == LEFT:
			return LEFT
		elif self.event == RIGHT:
			return RIGHT
		self.win.clear()
		self.win.refresh()

