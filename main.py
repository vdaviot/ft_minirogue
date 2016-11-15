#!/Users/vdaviot/homebrew/bin/python3.5
import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
import random
from mapp import Map_generator
from player import Player
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
			if self.event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
				self.player.move(self.event)
				self.action = True
			if self.event == 32:
				self.player.actions(self.event, self.monster_table)
			if self.action == True:
				Main_game.turn += 1
				self.action = False
			self.level.print_map(self.player, self.monster_table)
			self.event = win.getch()
			

if __name__ == '__main__':
	stdscr = curses.initscr()
	win = curses.newwin(400, 400, 0, 0)
	win.keypad(1)
	game = Main_game(win)
