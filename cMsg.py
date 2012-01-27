from pygame import font
from pygame import Rect
from pygame import draw
import colors as C
import time

class cMsg():
	HOLD_TIME = 2
	
	def __init__(self,string,window):
		font.init()
		self.text = string
        	self.myfont = font.SysFont("Arial", 20)
        	self.render_font = self.myfont.render(string, 1, C.black)
		w = self.render_font.get_width()
		h = self.render_font.get_height()
		self.winh = window.get_height()
		self.rect = Rect(0,self.winh,w,h)
		
		self.movein = False
		self.moveout = False
		self.hold = False
		self.hold_start = 0
	
	def draw(self,window):
		"""
			Draw the current message
		"""
		draw.rect(window, C.white, self.rect)
        	window.blit(self.render_font, (self.rect.x, self.rect.y))

	def update_logic(self,window):
		"""
			Movein and Moveout logic movement
		"""
		if self.movein:
			fh = self.render_font.get_height()
			self.rect.move_ip(0,-1)
			if self.rect.y <= window.get_height()-fh:
				self.move_hold()

		elif self.moveout:
			self.rect.move_ip(0,1)
			if self.rect.y > window.get_height():
				self.move_stop()
		elif self.hold:
			self.update_hold()

	def update_hold(self):
		"""
			Controls how much time the message must stay
			between movein state and moveout state
		"""
		ctime = time.time()
		if (ctime - self.hold_start) > self.HOLD_TIME:
			self.move_out()

	#
	# Flag control for movement
	#
	def move_in(self):
		self.movein = True
		self.moveout = False
		self.hold = False

	def move_out(self):
		self.movein = False
		self.moveout = True
		self.hold = False
	
	def move_hold(self):
		self.movein = False
		self.moveout = False
		self.hold = True
		self.hold_start = time.time()

	def move_stop(self):
		self.movein = False
		self.moveout = False
		self.hold = False

	def set_text(self,string,movein=True):
		"""
			Set a new text for the message.
			Additionally it shows the message. the flag movein controls that True=>Move in, False=> simply set text
		"""
		self.text = string
        	self.render_font = self.myfont.render(string, 1, C.black) 
		w = self.render_font.get_width()
		h = self.render_font.get_height()
		self.rect = Rect(0,self.winh,w,h)

		if movein: self.move_in()
