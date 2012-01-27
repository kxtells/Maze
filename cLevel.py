from pygame import Rect
import random
import cMaze
import colors as COLOR

class cLevel():

	def __init__(self):
		sqw = 32
		sqh = 32
		nobstacles = 5
		ow = 25
		oh = 25		
		self.MAZERECTS = []

		self.START = Rect(0,0,sqw,sqh) 
		self.END = Rect(800-sqw*3,600-sqh*3,sqw*3,sqh*3)
		#self.OBSTACLES = self.generate_obstacles(nobstacles,ow,oh)
		

		maze = cMaze.cMaze(19,25)
		#self.MAZE = maze.maze
		maze.maze[0][0] = 0
		self.MAZERECTS = self.maze_to_rects(maze.maze,1)
		
		self.VISITED = []
		self.CHECKPOINTS = self.generate_checkpoints(maze.maze,5)
		
		self.fgcolor = COLOR.white
		self.bgcolor = COLOR.random_color() 
		
		self.right = True

	def get_start(self):
		return self.START
	
	def get_start(self):
		return self.END

	def generate_obstacles(self,num,ow,oh):
		obstacles = []		

		for o in range(num):
			px = random.randint(0+ow,800-ow*2)
			py = random.randint(50,600)
			rect = Rect(px,py,ow,oh)
			obstacles.append(rect)

		return obstacles

	def maze_to_rects(self,MAZE,val):
		w = 32
		h = 32
		result = []
		for x,r in enumerate(MAZE):
			for y,c in enumerate(r):
				if MAZE[x][y] == val:
					result.append(Rect(x*w,y*h,w,h))
		return result

	def update_obstacles_logic(self,width,height):
		for o in self.OBSTACLES:
			if self.right:
				o.move_ip(1,0)
			else:
				o.move_ip(-1,0)
	
	def update_logic():
		"""
			Update General logic of the level
		"""	
		if len(self.CHECKPOINTS) == 0:
			print "Now you can go to the ending"


	def generate_checkpoints(self,maze,num):
		"""
			Generates a random list of places to visit
		"""
		possibles = self.maze_to_rects(maze,0) #possible visitable places
		result = []		

		while len(result) < num:
			random.shuffle(possibles)
			result.append(possibles.pop())

		return result

	def reset(self):
		"""
			Just reset the checkpoints
		"""
		while len(self.VISITED) > 0:
			self.CHECKPOINTS.append(self.VISITED.pop())
