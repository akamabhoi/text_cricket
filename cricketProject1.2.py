import random

def length(p):
	length = ['short length','good length','yorker']
	print(length[p],end=" ")
	
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

def paddled_sweep(res):
	if res == 1:
		print("")
	else:
		print("")
		
def sweep(res):
	if res == 1:
		print("")
	else:
		print("")

def scoop(res):
	if res == 1:
		print("")
	else:
		print("")
		
def hook(res):
	if res == 1:
		print("")
	else:
		print("")
	
def leg_glance(res):
	if res == 1:
		print("")
	else:
		print("")
		
def flick(res):
	if res == 1:
		print("")
	else:
		print("")

def over_midwicket(res):
	if res == 1:
		print("")
	else:
		print("")
		
def pull(res):
	if res == 1:
		print("")
	else:
		print("")
		
def on_drive(res):
	if res == 1:
		print("")
	else:
		print("")
		
def off_drive(res):
	if res == 1:
		print("")
	else:
		print("")

def straight_drive(res):
	if res == 1:
		print("")
	else:
		print("")
		
def cover(res):
	if res == 1:
		print("")
	else:
		print("")

def inside_out(res):
	if res == 1:
		print("")
	else:
		print("")
		
def square_cut(res):
	if res == 1:
		print("")
	else:
		print("")

def late_cut(res):
	if res == 1:
		print("")
	else:
		print("")
		
def glide2thirdman(res):
	if res == 1:
		print("")
	else:
		print("")
		
def shot(p,d):
	length = p
	dir = d
	global score
	shot_sel = input(">")
	#short length
	if p == 0:   
		if dir == 0:
			#write conditions
			if 'glide' in shot_sel or 'late cut' in shot_sel :
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

def difficulty(mode):
	if mode == easy:
		opp = 9
	elif mode == medium:
		opp = 15
	elif mode == difficult:
		opp = 20
	else:
		opp = 35
	return opp
	
def out(reason,mode):
	global score
	print(reason,"OUT!")
	print("Your score: ", str(score))
	check_draw(mode)	
	print("You LOSE!")
	input("\nPress Enter to exit")
	exit(0)

def check_draw(mode):
	global score
	if mode == easy and score == difficulty(easy):
		print("It's a draw!")
		input("\Press Enter to exit")
		exit(0)
	if mode == medium and score == difficulty(medium):
		print("It's a draw!")
		input("\Press Enter to exit")
		exit(0)
	if mode == hard and score == difficulty(hard):
		print("It's a draw!")
		input("\Press Enter to exit")
		exit(0)
		
def won():
	print("Congratulation you won!")
	input("\nPress Enter to exit")
	exit(0)
	
def status(target,ball):
	print()
	print("Runs to win".ljust(20) +": " + str(target-score))
	print("Balls remaining".ljust(20) +": " + str(6-ball))
	
def start():
	global score
	target = 0
	print("Enter difficulty level(easy ,medium ,hard) ")
	mode  = input(">")
	print()
	target = difficulty(mode)
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
print("WELCOME TO TEXT-CRICKET".center(55,"-"))
print()		
start()