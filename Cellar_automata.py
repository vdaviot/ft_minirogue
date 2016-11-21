# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Map_generator.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/17 22:35:40 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/17 22:35:42 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import profile
import random
import sys

class Decouple():

	def	__init__(self):
		self.items = {}

	def union(self, root1, root2):
		if self.items[root2] < self.items[root1]:
			self.items[root1] = root2
		else:
			if self.items[root1] == self.items[root2]:
				self.items[root1] -= 1
			self.items[root2] = root1

	def	find(self, x):
		try:
			while self.items[x] > 0:
				x = self.items[x]
		except KeyError: 
			self.items[x] = -1
		return x

	def	split_sets(self):
		sets = {}
		j = 0
		for j in self.items.keys():
			root = self.find(j)
			if root > 0:
				if sets.has_key(root):
					list = sets[root]
					list.append(j)
					sets[root] = list
				else:
					sets[root] = [j]
		return sets

	def	dump(self):
		print self.items

class Cellar_automata():

	def	__init__(self, length, width, density=0.40):
		self.length = length
		self.width = width
		self.area = length * width
		self.map = []
		self.ds = Decouple()
		self.up_loc = 0
		self.center = (int(self.length / 2) , int(self.width / 2))
		self.generate_initial_map(density)

	def	print_map(self):
		x = 0
		row = ""
		for row in range(0, self.length):
			for col in range(0, self.width):
				if self.map[row][col] in (WALL, PERM_WALL):
					print('#'),
				else:
					print('.'),
			print

	def	generate_definitive_map(self):
		for row in range(1, self.length - 1):
			for col in range(1, self.width - 1):
				wall_count = self.adjust_wall_count(row, col)
				if self.map[row][col] == FLOOR:
					if wall_count > 5:
						self.map[row][col] = WALL
				elif wall_count < 4:
						self.map[row][col] = FLOOR
		self.join_room()
		return self.map

	def	set_border(self):
		for row in range(0, self.length):
			self.map[row][0] = PERM_WALL
			self.map[row][self.width - 1] = PERM_WALL

		for col in range(0, self.width):
			self.map[0][col] = PERM_WALL
			self.map[self.length - 1][col] = PERM_WALL

	def	generate_initial_map(self, density):
		for row in range(0, self.length):
			r = []
			for col in range(0, self.width):
				r.append(WALL)
			self.map.append(r)

		open_count = int(self.area * density)
		self.set_border()
		while open_count > 0:
			rand_row = random.randrange(1, self.length - 1)
			rand_col = random.randrange(1, self.width - 1)
			if self.map[rand_row][rand_col] == WALL:
				self.map[rand_row][rand_col] = FLOOR
				open_count -= 1

	def	adjust_wall_count(self, row, col):
		count = 0
		for r in (-1, 0, 1):
			for c in (-1, 0, 1):
				if self.map[(row + r)][(col + c)] != FLOOR and not (r == 0 and c == 0):
					count += 1
		return count

	def	join_room(self):
		for r in range(1, self.length - 1):
			for c in range(1, self.width - 1):
				if self.map[r][c] == FLOOR:
					self.union_adj_sqr(r, c)
		all_caves = self.ds.split_sets()
		for cave in all_caves.keys():
			self.join_point(all_caves[cave][0])


	def	join_point(self, point):
		next_point = point
		while 1:
			dir = self.get_tunnel_dir(point, self.center)
			move = random.randrange(0, 3)
			if move == 0:
				next_point = (point[0] + dir[0], point[1])
			elif move == 1:
				next_point = (point[0], point[1] + dir[1])
			else:
				next_point = (point[0], dir[0], point[0] + dir[1])
			if self.stop_drawing(point, next_point, self.center):
				return
			root1 = self.ds.find(next_point)
			root2 = self.ds.find(point)
			if root1 != root2:
				self.ds.union(root1, root2)
			self.map[next_point[0]][next_point[1]] = FLOOR
			point = next_point

	def	stop_drawing(self, point, next_point, center):
		if self.ds.find(next_point) == self.ds.find(center):
			return 1
		if self.ds.find(point) != self.ds.find(next_point) and self.map[next_point[0]][next_point[1]] == FLOOR:
			return 1
		else:
			return 0

	def	get_tunnel_dir(self, point1, point2):
		if point1[0] < point2[0]:
			h_dir = +1
		elif point1[0] > point2[0]:
			h_dir = -1
		else:
			h_dir = 0

		if point1[1] < point2[1]:
			v_dir = +1
		elif point1[1] > point2[1]:
			v_dir = -1
		else:
			v_dir = 0
		return (h_dir, v_dir)

	def	union_adj_sqr(self, srow, scol):
		loc = (srow, scol)
		for r in (-1, 0):
			for c in (-1, 0):
				newloc = (srow + r, scol + c)
				if self.map[newloc[0]][newloc[1]] == FLOOR:
					root1 = self.ds.find(loc)
					root2 = self.ds.find(newloc)
					if root1 != root2:
						self.ds.union(root1, root2)


PERM_WALL = 0
WALL = 1
FLOOR = 2

for i in range(9):
	print
	print("map {}:").format(i + 1)
	ca = Cellar_automata(random.randrange(10, 40), random.randrange(10, 40), random.uniform(0.40, 0.50))
	ca.generate_definitive_map()
	ca.print_map()

















