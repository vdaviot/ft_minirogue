# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/21 22:23:02 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/21 22:23:06 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python
import curses, locale, random, time, curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from Mapp import Map_generator
from Player import Player
from Monster import Monster
from Monster_table import Monster_table
from Status import Status
import sys

class	Main_game():

	def	__init__(self, win):
		self.win = win
		self.level = Map_generator(win)
		self.player = Player(self.level)
		self.monster_table = Monster_table(self.level)
		self.action = False
		self.event = 0
		Main_game.turn = 1
		self.run()

	def	run(self):
		self.run = True;
		while self.run == True:
			if self.event == 127:
				self.run = False
				self.win.addnstr(7, 20, "Game Closed!", len("Game Closed!"))
				self.win.refresh()
				time.sleep(3)
				curses.endwin()
				sys.exit()

			if self.event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
				self.player.move(self.event)
				self.action = True

			if self.event == 32:
				self.player.actions(self.event, self.monster_table)
				self.action = True

			if self.action == True:
				self.monster_table.monster_movement()
				Main_game.turn += 1
				self.action = False
				
			run = self.refresh(self.monster_table, self.player, self.run)
			if run == False:
				break
			self.level.print_map(self.player, self.monster_table, Main_game.turn)
			self.event = win.getch()
		self.win.clear()
		self.win.addnstr(7, 20, "You died!", len("You died!"))
		self.win.refresh()
		time.sleep(3)
		curses.endwin()

	def refresh(self, monster_table, player, run):
		for i in range(len(monster_table.table)):
			monster_table.table[i].status.refresh_status(monster_table.table[i], run)
		return player.status.refresh_status(player, run)

if __name__ == '__main__':
	locale.setlocale(locale.LC_ALL,'fr_FR.UTF-8')
	stdscr = curses.initscr()
	win = curses.newwin(400, 400, 0, 0)
	win.keypad(1)
	game = Main_game(win)
