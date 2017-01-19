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

import curses, locale, sys, signal, os, readline
import curses.textpad

UP = 259
RIGHT = 261
DOWN = 258
LEFT = 260
DEL = 127

class	Win():

	def	__init__(self, row, col):

	# Main Window init
		os.environ['LINES'] = str(row)
		del os.environ['LINES']
		os.environ['COLUMNS'] = str(col)
		del os.environ['COLUMNS']
		self.row = row
		self.col = col
		self.mainScreen = curses.initscr()
		self.mainScreen.border('@', '@', '@', '@', '@', '@', '@', '@')
		self.mainScreen.addnstr(curses.LINES - 2, curses.COLS / 2 - len("Made by vdaviot with <3") / 2, "Made by vdaviot with <3", len("Made by vdaviot with <3"))
		self.maxY, self.maxX = self.mainScreen.getmaxyx()[0], self.mainScreen.getmaxyx()[1]
		curses.curs_set(0)
		curses.cbreak()
		curses.putp("li")
		curses.putp("co")
	# Color init

		if curses.has_colors():
			curses.start_color()
			curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
			curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
			curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

	# Map Subwindow init

		self.mapSpot = self.mainScreen.subwin(curses.LINES / 3 * 2, curses.COLS / 4 * 3, 0, 0)
		self.mapSpot.border('#', '#', '#', '#', '#', '#', '#', '#')		# Map display spot
		self.mapSpot.addnstr(5, 5, "MAP", len("MAP"))
		self.mapSpot.refresh()

		self.chatWindow = self.mainScreen.subwin(curses.LINES / 3 - 1, curses.COLS / 4 * 3, curses.LINES / 3 * 2, 0)
		self.chatWindow.border('#', '#', '#', '#', '#', '#', '#', '#')		# Chat display spot
		self.chatWindow.addnstr(5, 5, "CHAT", len("CHAT"))
		self.chatWindow.refresh()

		self.groupDisplay = self.mainScreen.subwin(curses.LINES / 3 + 1, (curses.COLS / 4), 0, (curses.COLS / 4) * 3 + 1)
		self.groupDisplay.border('#', '#', '#', '#', '#', '#', '#', '#')		#Group Display spot
		self.groupDisplay.addnstr(5, 5, "GROUP", len("GROUP"))
		self.groupDisplay.refresh()

		self.selfDisplay = self.mainScreen.subwin(curses.LINES / 3 + 1, (curses.COLS / 4), curses.LINES / 3, (curses.COLS / 4) * 3 + 1)
		self.selfDisplay.border('#', '#', '#', '#', '#', '#', '#', '#')			#Self character display
		self.selfDisplay.addnstr(5, 5, "ME", len("ME"))
		self.selfDisplay.refresh()

		self.stuffDisplay = self.mainScreen.subwin(curses.LINES / 3 - 1, (curses.COLS / 4), curses.LINES / 3 * 2, (curses.COLS / 4) * 3 + 1)
		self.stuffDisplay.border('#', '#', '#', '#', '#', '#', '#', '#')		# Display your stuff
		self.stuffDisplay.addnstr(5, 5, "STUFF", len("STUFF"))
		self.stuffDisplay.refresh()

		self.run = True
		self.event = None
		i =0
		while True:
			try:
				# coord = "Coord:\n\tx: " + str(self.maxX) + "\n\ty: " + str(self.maxY)
				# self.chatWindow.addnstr(7 ,7 , coord, len(coord))
				# signal.signal(signal.SIGWINCH, self._resizeTerm)
				self.maxX = int(os.popen('tput cols', 'r').readline())
				self.maxY = int(os.popen('tput lines', 'r').readline())
				coord = "x: " + str(self.maxY) + " :" + " y:" + str(self.maxX)
				self.mainScreen.refresh()
				self.mapSpot.refresh()
				self.chatWindow.refresh()
				self.groupDisplay.refresh()
				self.stuffDisplay.refresh()
				self.selfDisplay.refresh()
				self.selfDisplay.addnstr(3, 3, str(coord), len(str(coord)))
				i += 1
				# action = self.mainScreen.getch(0)
				# if action is curses.KEY_RESIZE:
					# self.selfDisplay.addnstr(0, 0, str(action), len(str(action)))
			except KeyboardInterrupt:
				curses.endwin()




	def	__str__(self):
		return "Win:\n\t" + "row: {}\n\t".format(self.row) + "col: {}\n".format(self.col)

	def	_resizeTerm(self, signal, frame):
		# self.maxY, self.maxX = os.environ['LINES'], os.environ['COLUMNS']
		self.selfDisplay.addnstr(3, 3, coord, len(coord))
		if curses.is_term_resized(self.maxY, self.maxX) == True:
			curses.resize_term(self.maxY, self.maxX)


	def	_leave(self):
		curses.endwin()
		
	def	_nextTurn(self):
		return self.mainScreen.getch()

	def	_waitTurn(self):
		action = self.mainScreen.getch()
		return self.mainScreen.ungetch()
