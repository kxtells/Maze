import pygame
import cMsg
import cPlayer
import cLevel
import sys , traceback
import sounds as SOUNDS
from cMenu import cMenu
from colors import *
from strings import *
from attributions import *

pygame.init()
size = width, height = 800,600

FPS = 60
clock = pygame.time.Clock ()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Rects")

PLAYER = cPlayer.cPlayer(10,10,10,10)
LEVEL = cLevel.cLevel()

show_menu = True
show_credits = False
endgame = False
fullscreen = False

SOUNDS.play_music(9)
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
ckey_img = pygame.image.load("img/ckey.png").convert_alpha()
fkey_img = pygame.image.load("img/fkey.png").convert_alpha()
logo_img = pygame.image.load("img/borinotlogo.png").convert_alpha()


def main_menu_selection():
	"""
		What to do on menu selection
	"""
	global show_menu
        PLAYER.set_speed(main_menu.current+1)
	show_menu = False

main_menu.action_function = main_menu_selection


def new_level():
	"""
		Create a new level
		Clear player pathlist
		Select another random music
	"""
	global LEVEL
	LEVEL = cLevel.cLevel()
	PLAYER.clear_pathlist()
	SOUNDS.play_music_random()

def go_to_menu():
	"""
		Return to game menu.
	"""
	global show_menu
	show_menu = True
	#new_level()
	#PLAYER.set_to_start()
	#PLAYER.clear_pathlist()

def toggle_fullscreen():
	"""
		Change between fullscreen and windowed
	"""
	global fullscreen
	if not fullscreen:
		pygame.display.set_mode((801,601),pygame.FULLSCREEN) #801,601 to force a square around the game
		fullscreen = True
	else:
		pygame.display.set_mode(size)
		fullscreen = False

def toggle_credits():
	"""
		Go to Credits Page
	"""
	global show_credits
	if show_credits: show_credits = False
	else: show_credits = True

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

def update_scene():
	"""
		Update all the rectangles in scene
	"""
	window.fill(black)
	
	
	#for o in LEVEL.OBSTACLES:
	#	pygame.draw.rect(window, white, o)
	
	pygame.draw.rect(window, blue, LEVEL.START)
	pygame.draw.lines(window, white,True, [(0,0),(800,0),(800,600),(0,600),])
	
	if len(LEVEL.CHECKPOINTS) > 0:
		pygame.draw.rect(window, gray, LEVEL.END)
	else:
		for i in xrange(5):
			pygame.draw.rect(window, random_color(), LEVEL.END.inflate(-i*2,-i*2))
		
		pygame.draw.rect(window, red, LEVEL.END.inflate(-6*2,-6*2))
	
	draw_maze()
	draw_checkpoints()
	
	
	
	for path in PLAYER.pathlist:
		pygame.draw.lines(window, orange, False, path)
		pygame.draw.circle(window, orange, path[-1],3) 

	pygame.draw.lines(window, green, False, PLAYER.path+[PLAYER.rect.center])
	pygame.draw.rect(window, red, PLAYER.rect)



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
        	
def draw_credits():
	"""
		Game and Music credits:
	"""
	#
	# Beware! Dragons ahead
	# highly bad and unreusable code ahead!
	# 
        myfont = pygame.font.SysFont("Arial", 15)
        titlefont = pygame.font.SysFont("Arial", 25)
	titlefont.set_underline(True)
        title = titlefont.render("BorinotGames Is:", 1, black) 
        titlethanks = titlefont.render("Special Thanks to:", 1, black) 
        font2 = myfont.render("Jordi Castells", 1, blue) 
        font3 = myfont.render("Music from ccMixter.org and freesound.org", 1, blue) 
        referal_font = myfont.render("Direct links to the songs can be found on BorinotGames.com", 1, blue) 
	title2 = titlefont.render("Music:", 1, black) 
	
	sx = 100 
	sy = 15
	sqw = 400
	sqh = 560
	ln=30 #line separation
	ln_music = ln*4 #where the music attributions
	
	#background
	pygame.draw.rect(window, green, (sx-10,sy+10,sqw,sqh))
	pygame.draw.rect(window, white, (sx-5,sy-5,sqw+15,sqh))

	#titles and subtitles
	window.blit(title, (sx, sy))
        window.blit(font2, (sx, sy+ln))
	window.blit(title2, (sx, sy+ln*2))
        window.blit(font3, (sx, sy+ln*3))

	#Music
	total_offset = 0
	for i,artist in enumerate(ATTRIBUTION_ARTISTS):
        	ay = sy+ln_music+(i*ln)+(total_offset*ln)
		total_offset += 1
		artist_font = myfont.render(artist, 1, blue) 
		window.blit(artist_font, (sx, ay))
        	
		for j,song in enumerate(ATTRIBUTION_SONGS[i]):
			csy = ay+(j+1)*ln
        		song_font = myfont.render(song, 1, blue) 
			window.blit(song_font, (sx+15, csy))
		
		total_offset += j
	
	total_offset = sy+ln_music+total_offset*ln+len(ATTRIBUTION_ARTISTS)*ln
        
	window.blit(referal_font, (sx, total_offset))
        total_offset += ln

	#Special Thanks
        window.blit(titlethanks, (sx, total_offset))
	for i,st in enumerate(SPECIAL_THANKS):
        	ay = sy+total_offset+20+(i*ln)
		sp_font = myfont.render(st, 1, blue) 
		window.blit(sp_font, (sx, ay))

def draw_logo():
	lw = logo_img.get_width()
	lh = logo_img.get_height()
	window.blit(logo_img,logo_img.get_rect().move(width-lw,height-lh))

def draw_exit_game():
	"""
		What to draw on exiting the game
	"""
	window.fill(black)
	lw = logo_img.get_width()
	lh = logo_img.get_height()
	window.blit(logo_img,logo_img.get_rect().move(0,200))
	
	myfont = pygame.font.SysFont("Arial", 50)
	myfont2 = pygame.font.SysFont("Arial", 25)
	title = myfont.render("Thanks for Playing!",1,white)
	text = myfont2.render("www.borinotgames.com",1,white)
	window.blit(title,(200,250))
	window.blit(text,(200,300))


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
        font2 = myfont.render("Exit Game", 1, blue) 
        font3 = myfont.render("Un/Mute General sounds", 1, blue) 
        font4 = myfont.render("Un/Mute Music", 1, blue) 
        font5 = myfont.render("Credits", 1, blue) 
        font6 = myfont.render("Toggle Fullscreen", 1, blue) 
        
	sx = 500
	sy = 50
	ymov = 40
	ln=20

	
	pygame.draw.rect(window, green, (sx-10,sy-30,300,350))
	pygame.draw.rect(window, white, (sx-5,sy-40,300,350))

	window.blit(title, (sx, sy - 20 ))
	
	window.blit(font, (sx + esckey_img.get_width(), sy + esckey_img.get_height()/2))
	window.blit(esckey_img,esckey_img.get_rect().move(sx,sy))

	window.blit(font2, (sx + esckey_img.get_width()*2, sy*2 + esckey_img.get_height()/2))
	window.blit(esckey_img,esckey_img.get_rect().move(sx,sy*2))
	window.blit(esckey_img,esckey_img.get_rect().move(sx+esckey_img.get_width(),sy*2))

	window.blit(font3, (sx + esckey_img.get_width(), sy*3 + esckey_img.get_height()/2))
	window.blit(skey_img,esckey_img.get_rect().move(sx,sy*3))

	window.blit(font4, (sx + esckey_img.get_width(), sy*4 + esckey_img.get_height()/2))
	window.blit(mkey_img,esckey_img.get_rect().move(sx,sy*4))

	window.blit(font6, (sx + esckey_img.get_width(), sy*5 + esckey_img.get_height()/2))
	window.blit(fkey_img,esckey_img.get_rect().move(sx,sy*5))
	
	window.blit(font5, (sx + esckey_img.get_width(), sy*6 + esckey_img.get_height()/2))
	window.blit(ckey_img,esckey_img.get_rect().move(sx,sy*6))


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
	#LEVEL.update_obstacles_logic(width,height)


#
# EVENTS
#

UP_K = [pygame.K_UP]
DWN_K = [pygame.K_DOWN]
LEFT_K = [pygame.K_LEFT]
RIGHT_K = [pygame.K_RIGHT]

def game_event_handler(event):
	global window
	if event.type == pygame.QUIT: pygame.quit();sys.exit()
 	#Changing sounds configuration and credits page
	if event.type == pygame.KEYDOWN:
        	#if event.key == pygame.K_p: 
		#	b = PLAYER.toggle_sounds();
		#	if b: MESSAGE.set_text("Player Sounds ON")
		#	else: MESSAGE.set_text("Muted Player, is it annoying?")
        	if event.key == pygame.K_s: 
			b = SOUNDS.toggle_fx();
			if b: MESSAGE.set_text("FX on ")
			else: MESSAGE.set_text("FX off")
        	if event.key == pygame.K_m: 
			b = SOUNDS.toggle_music();
			if b: MESSAGE.set_text("Enjoy the Music and the loops!")
			else: MESSAGE.set_text("Music off! is getting on your nerves?")
	
        	if event.key == pygame.K_c: 
			toggle_credits();
        	if event.key == pygame.K_f: 
			toggle_fullscreen()

	if show_credits: return #do nothing on credits

	if show_menu:
 		if event.type == pygame.KEYDOWN:
        	        if event.key == pygame.K_DOWN: main_menu.menu_down();
        	        elif event.key == pygame.K_UP: main_menu.menu_up();
        	        elif event.key == pygame.K_RETURN: main_menu.action_function()
                	elif event.key == pygame.K_ESCAPE: exit_game()
			else:
				if main_menu.event_function != None: main_menu.event_function(event)
	else:
		if event.type == pygame.KEYDOWN:
               		if event.key in DWN_K: PLAYER.move_down();
                	elif event.key in UP_K: PLAYER.move_up();
                	elif event.key in LEFT_K: PLAYER.move_left();
                	elif event.key in RIGHT_K: PLAYER.move_right();
                	elif event.key == pygame.K_ESCAPE: go_to_menu()

		#Pause Button
                #elif event.key == pygame.K_ESCAPE or event.key == pygame.K_p: status.pause_game()

def exit_game():
	global endgame
	endgame = True

               
def main():
	try:
		while not endgame:
        		for event in pygame.event.get(): game_event_handler(event)
		
			
			if not show_menu and not show_credits: update_logic()
			MESSAGE.update_logic(window)
			update_scene()
			colision_handling()
			MESSAGE.draw(window)
	
			if show_menu and not show_credits:
				draw_menu(main_menu,sx=300)
				draw_explanation()	
				draw_cheatsheet()
				draw_logo()	
		
			if show_credits:
				draw_credits()
				draw_logo()
	
			clock.tick(FPS)
	                pygame.display.update()
	
		#when game finished
		st_time = pygame.time.get_ticks()
		waittime = 0
		while waittime < 5000: #5 seconds
			waittime = pygame.time.get_ticks() - st_time
			draw_exit_game()
			clock.tick(FPS)
	                pygame.display.update()
	except :
		print "something bad happened"
		print "Logged into errlog.log"
	        traceback.print_exc(file=open("errlog.log","a"))

if __name__ == '__main__': main()  
