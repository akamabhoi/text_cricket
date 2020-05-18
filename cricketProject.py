import random

def length(p):
	length = ['short length','good length','yorker']
	print(length[p])
	
def line(d):
	dir = ['wide outside off stump','outside off stump','on off stump','to middle stump','to leg stump','outside legstump']
	print(dir[d])

'''
shots - 

paddled sweep/scoop
sweep, hook, leg glance, flick
hoick over mid wicket, pull shot
on drive
off drive, straight drive
cover drive, inside out 
square cut
late cut, glide to third man
'''	
		
def shot(p,d):
	length = p
	dir = d
	global score
	shot_sel = input(">")
	#lengthing short
	if p == 0:   
		if dir == 0:
			#write conditions
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 1:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 2:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 3:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 4:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 5:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
	
	#good length delivery
	if p == 1: 
		if dir == 0:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 1:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 2:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 3:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 4:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 5:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
	
	#yorker delivery
	if p == 2: 
		if dir == 0:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 1:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 2:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 3:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 4:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")
		if dir == 5:
			#write condition
			if 'glide' in shot_sel :
				print("comment on shot")
				score = score + 4
			elif 'upper' in shot_sel:
				print("comment on shot")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("comment")
				score = score + 1
			else:
				out("reason")

			
def out(reason):
	global score
	print(reason,"OUT!")
	print("Your score: ", str(score))
	print("You LOSE!")
	input("\nPress Enter to exit")
	exit(0)

def won():
	print("Congratulation you won!")
	input("\nPress Enter to exit")
	exit(0)

def status(target,ball):
	print("Runs to win: " + str(target-score))
	print("Balls remaining: " + str(6-ball))
	
def start():
	global score
	target = 0
	print("Enter difficulty level(easy ,medium ,hard) ")
	mode  = input(">")
	print()
	if mode == 'easy':
		target = 9
	elif mode == 'medium':
		target = 15
	else:
		target = 20
	for ball in range(0,6,1):
		if score < target:
			status(target,ball)
		else:
			won()
		p = random.randint(0,2)
		d = random.randint(0,5)
		length(p)
		line(d)
		shot(p,d)

score = 0		
start()
