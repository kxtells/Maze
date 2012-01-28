import pygame
import cMsg
import cPlayer
import cLevel
import sys
import sounds as SOUNDS
from cMenu import cMenu
from colors import *
from strings import *


pygame.init()
size = width, height = 800,600

FPS = 60
clock = pygame.time.Clock ()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Rects")

PLAYER = cPlayer.cPlayer(10,10,10,10)
LEVEL = cLevel.cLevel()

show_menu = True

SOUNDS.play_music_random()
MESSAGE = cMsg.cMsg("TEST",window)

#
# Menus
#

#Main Menu
main_menu_texts = 'Boring', 'Easy' , 'Normal' , 'Difficult' , 'Extreme', 'Insane'
main_menu = cMenu(main_menu_texts,"Difficulty",0,blue,red)
main_menu_img1 = pygame.image.load("img/arrkeys.png").convert_alpha()
esckey_img = pygame.image.load("img/esckey.png").convert_alpha()
mkey_img = pygame.image.load("img/mkey.png").convert_alpha()
pkey_img = pygame.image.load("img/pkey.png").convert_alpha()
skey_img = pygame.image.load("img/skey.png").convert_alpha()


def main_menu_selection():
	global show_menu
        PLAYER.set_speed(main_menu.current+1)
	show_menu = False

main_menu.action_function = main_menu_selection


def new_level():
	global LEVEL
	LEVEL = cLevel.cLevel()
	PLAYER.clear_pathlist()
	SOUNDS.play_music_random()

def reload_game():
	global show_menu
	show_menu = True
	new_level()
	PLAYER.set_to_start()
	PLAYER.clear_pathlist()

def draw_maze():
	for r in LEVEL.MAZERECTS:
		pygame.draw.rect(window, LEVEL.bgcolor, pygame.Rect(r).move(-1,-1))
		pygame.draw.rect(window, LEVEL.fgcolor, r)

def draw_checkpoints():
	for r in LEVEL.CHECKPOINTS:
		#pygame.draw.rect(window, yellow, pygame.Rect(r).move(-1,-1))
		pygame.draw.rect(window, red, r.inflate(-5,-5))

	for r in LEVEL.VISITED:
		pygame.draw.rect(window, green, pygame.Rect(r).move(-1,-1))
		pygame.draw.rect(window, green, r)
#
# Draws a menu on screen 
# - menu (the menu to draw)
#
def draw_menu(menu,sx=200,sy=165):
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Arial", 20)
        titlefont = pygame.font.SysFont("Arial", 25)
	titlefont.set_underline(True)
	ymov = 40        

	if menu.background != None:
		window.blit(menu.background,menu.background.get_rect())
	else:
		pygame.draw.rect(window, green, (sx-15,sy-25,150,len(menu.options)*ymov+50))
		pygame.draw.rect(window, white, (sx-10,sy-50,150,len(menu.options)*ymov + 50))
		        
	#title
        render_font = titlefont.render(menu.title, 1, black) 
        window.blit(render_font, (sx, sy-ymov))
	
	x = sx
        y = sy

        for index,me in enumerate(menu.options):
                if menu.current == index: color = menu.select_color
                else: color = menu.color

                render_font = myfont.render(me, 1, color) 
                window.blit(render_font, (x, y))
                y += ymov

def draw_explanation():
	"""
		How to play the game
	"""
        myfont = pygame.font.SysFont("Arial", 15)
        font = myfont.render("Connect all the Red squares", 1, blue) 
        font2 = myfont.render("And head to the exit!", 1, blue) 
        font3 = myfont.render("You only need these keys:", 1, blue) 
        
	sx = 0
	sy = 50
	ymov = 40
	ln=20

	pygame.draw.rect(window, green, (sx-10,sy+10,font.get_width()+15,210))
	pygame.draw.rect(window, white, (sx-5,sy-5,font.get_width()+15,210))

	window.blit(font, (sx, sy))
        window.blit(font2, (sx, sy+ln))
        window.blit(font3, (sx, sy+ln*3))
	window.blit(main_menu_img1,main_menu_img1.get_rect().move(sx,sy+ln*4))

def draw_cheatsheet():
	"""
		Some good keys to know
	"""
        titlefont = pygame.font.SysFont("Arial", 15)
	titlefont.set_underline(True)
        myfont = pygame.font.SysFont("Arial", 15)

	title = titlefont.render("CheatSheet",1,black)
        font = myfont.render("Return to this screen", 1, blue) 
        font2 = myfont.render("Un/Mute Player sounds", 1, blue) 
        font3 = myfont.render("Un/Mute General sounds", 1, blue) 
        font4 = myfont.render("Un/Mute Music", 1, blue) 
        
	sx = 500
	sy = 50
	ymov = 40
	ln=20

	
	pygame.draw.rect(window, green, (sx-10,sy-30,300,300))
	pygame.draw.rect(window, white, (sx-5,sy-40,300,300))

	window.blit(title, (sx, sy - 20 ))
	
	window.blit(font, (sx + esckey_img.get_width(), sy + esckey_img.get_height()/2))
	window.blit(esckey_img,esckey_img.get_rect().move(sx,sy))

	window.blit(font2, (sx + esckey_img.get_width(), sy*2 + esckey_img.get_height()/2))
	window.blit(pkey_img,esckey_img.get_rect().move(sx,sy*2))

	window.blit(font3, (sx + esckey_img.get_width(), sy*3 + esckey_img.get_height()/2))
	window.blit(skey_img,esckey_img.get_rect().move(sx,sy*3))

	window.blit(font4, (sx + esckey_img.get_width(), sy*4 + esckey_img.get_height()/2))
	window.blit(mkey_img,esckey_img.get_rect().move(sx,sy*4))

def update_scene():
	"""
		Update all the rectangles in scene
	"""
	window.fill(black)
	
	
	#for o in LEVEL.OBSTACLES:
	#	pygame.draw.rect(window, white, o)
	
	pygame.draw.rect(window, blue, LEVEL.START)
	
	if len(LEVEL.CHECKPOINTS) > 0:
		pygame.draw.rect(window, gray, LEVEL.END)
	else:
		pygame.draw.rect(window, red, LEVEL.END)
	
	draw_maze()
	draw_checkpoints()
	
	
	
	for path in PLAYER.pathlist:
		pygame.draw.lines(window, orange, False, path)
		pygame.draw.circle(window, orange, path[-1],3) 

	pygame.draw.lines(window, green, False, PLAYER.path+[PLAYER.rect.center])
	pygame.draw.rect(window, red, PLAYER.rect)



def maze_colision():
	collided = False

	for r in LEVEL.MAZERECTS:
		if PLAYER.rect.colliderect(r):
			collided = True

	if PLAYER.rect.x < 0 \
	or PLAYER.rect.y <0 \
	or PLAYER.rect.x > width\
	or PLAYER.rect.y > height:
		collided = True
	
	if collided:
		SOUNDS.play_fx(0)
		MESSAGE.set_text(get_death_string(len(LEVEL.VISITED)))
		PLAYER.set_to_start()
		LEVEL.reset()

def checkpoints_colision():
	for index,c in enumerate(LEVEL.CHECKPOINTS):
		if PLAYER.rect.colliderect(c):
			LEVEL.VISITED.append(LEVEL.CHECKPOINTS.pop(index))
			MESSAGE.set_text(get_checkpoint_string(len(LEVEL.VISITED)))
			if len(LEVEL.CHECKPOINTS) > 0:
				SOUNDS.play_fx(1)
			else:
				SOUNDS.play_fx(2)

def colision_handling():
	if PLAYER.rect.colliderect(LEVEL.END) and len(LEVEL.CHECKPOINTS)==0:
		MESSAGE.set_text(get_end_string())
		SOUNDS.play_fx(12)
		PLAYER.set_to_start()
		new_level()
	
	maze_colision()
	checkpoints_colision()

def update_logic():
	"""
		Update verything logic. Basically move the squares
	"""

	PLAYER.update_logic()
	MESSAGE.update_logic(window)
	#LEVEL.update_obstacles_logic(width,height)


#
# EVENTS
#

UP_K = [pygame.K_UP]
DWN_K = [pygame.K_DOWN]
LEFT_K = [pygame.K_LEFT]
RIGHT_K = [pygame.K_RIGHT]

def game_event_handler(event):
	if event.type == pygame.QUIT: pygame.quit();sys.exit()
 	if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_p: 
			PLAYER.toggle_sounds();
			MESSAGE.set_text("AAA")
        	if event.key == pygame.K_s: 
			SOUNDS.toggle_fx();
			MESSAGE.set_text("AAA")
        	if event.key == pygame.K_m: 
			SOUNDS.toggle_music();
			MESSAGE.set_text("Enjoying the Music?")
	
	
	if show_menu:
 		if event.type == pygame.KEYDOWN:
        	        if event.key == pygame.K_DOWN: main_menu.menu_down();
        	        elif event.key == pygame.K_UP: main_menu.menu_up();
        	        elif event.key == pygame.K_RETURN: main_menu.action_function()
			else:
				if main_menu.event_function != None: main_menu.event_function(event)
	else:
		if event.type == pygame.KEYDOWN:
               		if event.key in DWN_K: PLAYER.move_down();
                	elif event.key in UP_K: PLAYER.move_up();
                	elif event.key in LEFT_K: PLAYER.move_left();
                	elif event.key in RIGHT_K: PLAYER.move_right();
                	elif event.key == pygame.K_ESCAPE: reload_game()

		#Pause Button
                #elif event.key == pygame.K_ESCAPE or event.key == pygame.K_p: status.pause_game()
                
def main():
	while True:
        	for event in pygame.event.get(): game_event_handler(event)
	
		
		update_logic()
		update_scene()
		colision_handling()
		MESSAGE.draw(window)

		if show_menu:
			draw_menu(main_menu,sx=300)
			draw_explanation()	
			draw_cheatsheet()	
	
		clock.tick(FPS)
                pygame.display.update()


if __name__ == '__main__': main()  
