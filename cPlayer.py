from pygame import Rect
import random
import sounds as SOUNDS

class cPlayer():
	mx = 0
	my = 0
	speed = 4
	sounds = True

	def __init__(self,left,top,width,height):
		self.startx = left
		self.starty = top
		self.width = width
		self.height = height
		self.rect = Rect(left, top, width, height)

		self.path = [self.rect.center]
		self.pathlist = []

	def update_logic(self):
		self.rect.move_ip(self.mx,self.my)

        def move_down(self):
		self.my = self.speed
		self.mx = 0
		self.add_point_to_path(self.rect.center)
		if self.sounds: SOUNDS.play_fx(11)
 
        def move_up(self):
 		self.my = -self.speed
		self.mx = 0               
		self.add_point_to_path(self.rect.center)
		if self.sounds: SOUNDS.play_fx(11)
	
	def move_left(self):
 		self.my = 0
		self.mx = -self.speed               
		self.add_point_to_path(self.rect.center)
		if self.sounds: SOUNDS.play_fx(11)

	def move_right(self):
 		self.my = 0
		self.mx = self.speed 
		self.add_point_to_path(self.rect.center)
		if self.sounds: SOUNDS.play_fx(11)

	def stop_moving(self):
		self.my = 0
		self.mx = 0
	
	def set_to_start(self):
		self.stop_moving()
		
		self.path.append(self.rect.center)
		
		self.rect = Rect(self.startx,self.starty,self.width,self.height)

		self.move_path_to_pathlist()

	def add_point_to_path(self,point):
		self.path.append(point)

	def move_path_to_pathlist(self):
		self.pathlist.append(self.path)
		self.path = [self.rect.center]

	def clear_pathlist(self):
		self.pathlist = []

	def random_speed(self):
		self.speed = random.uniform(2,5)

	def set_speed(self,speed):
		self.speed = speed

	def toggle_sounds(self):
		if self.sounds: self.sounds = False
		else: self.sounds == True
