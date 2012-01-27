from random import randint

STRINGS = [ "Aloha", \
"CONGRATS"]

ENDSTRINGS = ["Congrats!","Ok, Next one"]

CP1 = ["First One!","Only 4 to go","Beh, only one","That was easy right?"]
CP2 = ["Second One!","Two is better than one","Like my number of balls","Tweenies"]
CP3 = ["Third One!","Only 2 to go","Almost done"]
CP4 = ["Fourth!","One More to Go baby!","You are making a nice performance","Already tired?"]
CP5 = ["Fifth!", "Go for it!","The GOAL is waiting","Warm Goal waiting","Go Go Go!"]
CHPSTRINGS = [CP1,CP2,CP3,CP4,CP5]

D0 = ["Early Death!","You don't even tried","Not a Checkpoint eh..","Dude, so bad"]
D1 = ["At least you tried","Well, is no that bad","You learnt something?","What a pity"]
D2 = ["Death in the middle","Two and dead","Dead and two checkpoints","...","Don't no that again"]
D3 = ["Not Bad","Start again","Death with 3 is better than death with 5","Well, not close to win"]
D4 = ["Almost","So Close","not now..","Cmon!"]
D5 = ["Oh Shit!","I hate you","Oh no! not again","Having Fun?","And here we go again"]
DEATHSTRINGS = [D0,D1,D2,D3,D4,D5]

def get_checkpoint_string(ncheckpoints):
	"""
		Returns a string depending on the number of checkpoints
		achieved
	"""
	arridx = ncheckpoints - 1
	idx = randint(0,len(CHPSTRINGS[arridx])-1)
	return CHPSTRINGS[arridx][idx]

def get_death_string(ncheckpoints):
	"""
		Returns a string depending on the number of checkpoints
		achieved
	"""
	arridx = ncheckpoints
	idx = randint(0,len(DEATHSTRINGS[arridx])-1)
	return DEATHSTRINGS[arridx][idx]

def get_end_string():
	"""
		Get a random end string
	"""
	idx = randint(0,len(ENDSTRINGS)-1)
	return ENDSTRINGS[idx]


