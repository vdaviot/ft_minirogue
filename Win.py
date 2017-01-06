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
		curses.curs_set(0)
		curses.cbreak()
		# curses.flash()
		self.win = curses.newwin(col, row, 0, 0)
		self.win.keypad(1)
		self.run = True
		self.event = None

	def	__str__(self):
		return "Win:\n\t" + "row: {}\n\t".format(self.row) + "col: {}\n".format(self.col)
		
	def	_leave(self):
		curses.endwin()
		
	def	_nextTurn(self):
		return self.win.getch()

	def	_waitTurn(self):
		action = self.win.getch()
		return self.win.ungetch()
