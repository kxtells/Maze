#
# Sound list
#
# FX:
# 0 - Death
# 1 - Checkpoint
# 2 - all Checkpoints
# 3..10: Player moves, random sound
# 11 - Player turn
# 12 - You Made it! synth
#
# Music: Total 7 songs

import pygame.mixer as MIXER
from random import randint

CURRSONG = -1
NSONGS = 9
FXON = True
MUSICON = True
MIXER.init()

#FX = [MIXER.Sound("fx/fx0.ogg")]
FX = []

for f in range(13):
	fx = MIXER.Sound("fx/fx"+str(f)+".ogg")
	FX.append(fx)


def toggle_fx():
	global FXON
	if FXON: FXON = False
	else: FXON = True
	return FXON

def toggle_music():
	global MUSICON
	if MUSICON: 
		MIXER.music.stop()
		MUSICON = False
	else: 
		MIXER.music.play()
		MUSICON = True
	return MUSICON

def play_fx(ids):
	"""
		Play a sound specified by id
		if the sound exists, else do nothing
	"""
	if not FXON: return
	try:
		FX[ids].play()
	except:
		pass

def play_fx_player_rand():
	"""
		FUCKING BAD IDEA, sounds like HELL
		Play a sound for the player when turning
		random sounds of a scale
	"""
	try:
		FX[randint(3,10)].play()
	except:
		pass

def play_music(index):
	if not MUSICON: return

	try:
		MIXER.music.load("music/m"+str(index)+".ogg")
	except:
		MIXER.music.load("music/m"+str(index)+".ogg")
		print "WARNING: unknow music index, loading default"	

	MIXER.music.play(-1)

def play_music_random():
	if not MUSICON: return
	index = -1
	while index==CURRSONG:index = randint(1,NSONGS)
	try:
		MIXER.music.load("music/m"+str(index)+".ogg")
	except:
		MIXER.music.load("music/m"+str(index)+".ogg")
		print "WARNING: unknow music index, loading default"	

	MIXER.music.play(-1)
