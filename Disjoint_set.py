# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Disjoint_set.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/22 11:33:12 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/22 11:33:14 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Disjoint_set():

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