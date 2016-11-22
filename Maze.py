# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Maze.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/21 16:59:43 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/21 16:59:45 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random, sys

BOTTOMWALL = 0
RIGHTWALL = 1
VISITED = 2
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Maze():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.maze = [[[True, True, False] for j in range(col)] for i in range(row)]

        self.start_row = random.randrange(row)
        self.start_col = random.randrange(col)

        self.end_row = random.randrange(row)
        self.end_col = random.randrange(col)

        current_row = self.start_row
        current_col = self.start_col

        self.gen_maze(current_row, current_col)
        self.numtable = [[-1 for j in range(col)] for i in range(row)]
        self.map = self.__str__()
        self.solution_path = []

    def __str__(self):
        # return self.maze
        out_table = '.' + self.col * '_.' + '\n'
        for i in range(self.row):
            out_table += '|'
            for j in range(self.col):
                if self.maze[i][j][BOTTOMWALL]:
                    out_table += '_'
                else:
                    out_table += ' '
                if self.maze[i][j][RIGHTWALL]:
                    out_table += '#'
                else:
                    out_table += '.'
            out_table += '\n'
        return out_table

    def get_dir(self, row, col):
        dirlist = []
        if row - 1 >= 0:
            dirlist.append(UP)
        if row + 1 <= self.row - 1:
            dirlist.append(DOWN)
        if col - 1 >= 0:
            dirlist.append(LEFT)
        if col + 1 <= self.col - 1:
            dirlist.append(RIGHT)
        return dirlist

    def gen_maze(self, row, col, dir=None):
        maze = self.maze
        maze[row][col][VISITED] = True
        if dir == UP:
            maze[row][col][BOTTOMWALL] = False
        elif dir == DOWN:
            maze[row - 1][col][BOTTOMWALL] = False
        elif dir == RIGHT:
            maze[row][col - 1][RIGHTWALL] = False
        elif dir == LEFT:
            maze[row][col][RIGHTWALL] = False
        dir = self.get_dir(row, col)
        for i in range(len(dir)):
            j = random.randrange(len(dir))
            dir[i],dir[j] = dir[j], dir[i]

        for d in dir:
            if d == UP:
                if not maze[row - 1][col][VISITED]:
                    self.gen_maze(row - 1, col, UP)
            elif d == DOWN:
                if not maze[row + 1][col][VISITED]:
                    self.gen_maze(row + 1, col, DOWN)
            elif d == RIGHT:
                if not maze[row][col + 1][VISITED]:
                    self.gen_maze(row, col + 1, RIGHT)
            elif d == LEFT:
                if not maze[row][col - 1][VISITED]:
                    self.gen_maze(row, col - 1, LEFT)


    def solve_maze_aux(self, row, col, n):
        maze = self.maze
        numtable = self.numtable
        numtable[row][col] = n
        if (row, col) != (self.end_row, self.end_col):
            directions = self.get_dir(row, col)
            for d in directions:
                if d == UP and not maze[row - 1][col][BOTTOMWALL] and numtable[row - 1][col] == -1:
                    self.solve_maze_aux(row - 1, col, n + 1)
                if d == DOWN and not maze[row][col][BOTTOMWALL] and numtable[row + 1][col] == -1:
                    self.solve_maze_aux(row + 1, col, n + 1)
                if d == RIGHT and not maze[row][col][RIGHTWALL] and numtable[row][col + 1] == -1:
                    self.solve_maze_aux(row, col + 1, n + 1)
                if d == LEFT and not maze[row][col - 1][RIGHTWALL] and numtable[row][col - 1] == -1:
                    self.solve_maze_aux(row, col - 1, n + 1)

    def get_solution_path(self):
        actrow = self.end_row
        actcol = self.end_col
        start_row = self.start_row
        start_col = self.start_col
        path = []
        numtable = self.numtable
        path = self.solution_path

        while (actrow, actcol) != (start_row, start_col):
            path.append((actrow, actcol))
            directions = self.get_dir(actrow, actcol)
            for d in directions:
                if d == UP:
                    if numtable[actrow][actcol] - 1 == numtable[actrow - 1][actcol]:
                        actrow -= 1
                        break
                elif d == DOWN:
                    if numtable[actrow][actcol] - 1 == numtable[actrow + 1][actcol]:
                        actrow += 1
                        break
                elif d == LEFT:
                    if numtable[actrow][actcol] - 1 == numtable[actrow][actcol - 1]:
                        actcol -= 1
                        break
                elif d == RIGHT:
                    if numtable[actrow][actcol] - 1 == numtable[actrow][actcol + 1]:
                        actcol += 1
                        break
        path.append((actrow, actcol))
        path.reverse()

    def solve_maze(self):
        self.solve_maze_aux(self.start_row, self.startcol, 0)
        self.get_solution_path()





