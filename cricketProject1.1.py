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

		
def shot(p,d):
	length = p
	dir = d
	global score
	shot_sel = input(">>")
	#short length
	if p == 0:   
		if dir == 1:
			#write conditions
			if 'glide' in shot_sel or 'late cut' in shot_sel :
				print("Gets an outside edge that flies to the third man region for a boundary")
				score = score + 4
			elif 'upper' in shot_sel:
				print("It has gone over the rope for a SIX.. Fantastica..")
				score = score + 6
			elif 'third' in shot_sel or 'pull' in shot_sel:
				print("Easy Single")
				score = score + 1
			else:
				out("That's OUT!!! ")
		if dir == 0:
			#write condition
			if 'glide' in shot_sel :
				print("")
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
				print("")
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
	global target
	print(reason,"OUT!")
	print("Your score: ", str(score))
	if score < target-1:
		print("You LOSE!")
		input("\nPress Enter to exit")
		exit(0)
	if score == target-1:
		draw()
		
def won():
	print("Congratulation you won!")
	input("\nPress Enter to exit")
	exit(0)

def draw():
	print("It's a draw")
	input("\nPress Enter to exit")
	exit(0)
	
def status(target,ball):
	print()
	print("Runs to win".ljust(20) +": " + str(target-score))
	print("Balls remaining".ljust(20) +": " + str(6-ball))
	
def start():
	global score
	global target
	print("Enter difficulty level(easy ,medium ,hard) ")
	mode  = input(">>")
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
		if score >= target:
			won()
		p = random.randint(0,0)
		d = random.randint(1,1)
		length(p)
		line(d)
		shot(p,d)
		
	if score == target-1:
		draw()
	if score >= target:
		won()

		
		
score = 0
target= 0
print("WELCOME TO TEXT-CRICKET".center(55,"-"))
print()		
start()