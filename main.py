#!/usr/bin/python
import curses
import locale
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
import random
from Mapp import Map_generator
from Player import Player
from Monster import Monster
from Monster_table import Monster_table

class	Main_game():

	def	__init__(self, win):
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
				curses.endwin()

			if self.event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
				self.player.move(self.event)
				self.action = True

			if self.event == 32:
				self.player.actions(self.event, self.monster_table)
				self.action = True

			if self.action == True:
				Main_game.turn += 1
				self.action = False
				# self.player.refresh_statuses(self.run, win)
			self.level.print_map(self.player, self.monster_table, Main_game.turn)
			self.event = win.getch()

if __name__ == '__main__':
	locale.setlocale(locale.LC_ALL,'fr_FR.UTF-8')
	stdscr = curses.initscr()
	win = curses.newwin(400, 400, 0, 0)
	win.keypad(1)
	game = Main_game(win)
