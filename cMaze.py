import random

class cMaze():
	"""
		This class exclusively generates a python matrix (array of arrays) representing
		a maze
	"""

	rows = 0
	cols = 0
	start = (0,0)

	def __init__(self,mr,mc):
		self.rows = mr
		self.cols = mc
		self.visited= [ [ 0 for i in range(self.rows) ] for j in range(self.cols) ]
		self.maze= [ [ 1 for i in range(self.rows) ] for j in range(self.cols) ]
		self.cellstack = []
		
		self.visit_cell((0,0))
	

	def __str__(self):
		res = "maze:\n"
		for r in self.maze:
			res += str(r)+"\n"		

		res += "\nvisited:\n"
		for r in self.visited:
			res += str(r)+"\n"	


		return res

	def visit_cell(self,cell):
		if self.outofbounds(cell): return
		self.mark_as_visited(cell)
		
		#Find neighbours with intact walls
		neighbours = self.get_nonvisited_neighbours(cell)
		possibles = []
		for n in neighbours:
			if self.is_intact_cell(n): possibles.append(n)

		#at least one neighbour to visit
		if len(possibles) > 0:
			#choose one at random
			random.shuffle(possibles)
			c = possibles.pop()
			
			#remove the wall
			self.remove_wall(c)
			self.cellstack.append(cell) # currentcell to stack
			self.visit_cell(c)
		else:
			if len(self.cellstack) >0:
				self.visit_cell(self.cellstack.pop())
			else:
				return

	def mark_as_visited(self,cell):
		x = cell[0]
		y = cell[1]
		self.visited[x][y] = 1
	
	def remove_wall(self,cell):
		x = cell[0]
		y = cell[1]
		self.maze[x][y] = 0
	
	def get_nonvisited_neighbours(self,cell):
		x = cell[0]
		y = cell[1]
		nl = []
		
		tocheck = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		for c in tocheck:
			if not self.outofbounds(c) and not self.visited[c[0]][c[1]]: 
				nl.append(c)

		return nl

	def is_intact_cell(self,cell):
		x = cell[0]
		y = cell[1]
		nl = []
		
		tocheck = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		walls = 0

		for c in tocheck:
			if self.outofbounds(c) or self.maze[c[0]][c[1]]: 
				walls += 1
	
		return walls>=3 #three walls around


	
	def outofbounds(self,cell):
		x = cell[0]
		y = cell[1]

		if x<0 or y < 0: return True
	
		if x > self.cols-1 or y > self.rows-1: return True

		return False
