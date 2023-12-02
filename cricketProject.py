import random

def get_length_description(length_code):
    length_description = ['short length','good length','yorker']
    return length_description[length_code]

def get_direction_description(direction_code):
    direction_description = ['wide outside off stump','outside off stump','on off stump','to middle stump','to leg stump','outside legstump']
    return direction_description[direction_code]

def get_shot_range(shot_selection, available_shots):
    shots = [shot for shot in available_shots if shot in shot_selection]
    return shots

def play_shot(length_code, direction_code):
    length = get_length_description(length_code)
    direction = get_direction_description(direction_code)
    global score
    available_shots = ['glide','late cut','upper','third','pull']
    available_shots = get_shot_range(input("Enter available shots (space separated): ").lower(), available_shots)

    # Define shot outcomes based on length and direction
    if length_code == 0: 
        if direction_code == 1:
            outcomes = {
                'glide': ("Gets an outside edge that flies to the third man region for a boundary", 4),
                'late cut': ("Gets an outside edge that flies to the third man region for a boundary", 4),
                'upper': ("It has gone over the rope for a SIX.. Fantastica..", 6),
                'third': ("Easy Single", 1),
                'pull': ("Easy Single", 1)
            }
        random_shot = random.choice(available_shots)
        outcome_description, score_change = outcomes[random_shot]
        print(outcome_description)
        score += score_change

    # good length delivery
    elif length_code == 1: 
        if direction_code == 0:
            outcomes = {
                'glide': ("Elegant cover drive to the gully for a boundary", 4),
                'late cut': ("Elegant cover drive to the gully for a boundary", 4),
                'upper': ("Ferocious drive that smashes to the rope for a SIX!", 6),
                'third': ("Nicely placed straight drive to the fence for a single", 1),
                'pull': ("Nicely placed straight drive to the fence for a single", 1)
            }
        random_shot = random.choice(available_shots)
        outcome_description, score_change = outcomes[random_shot]
        print(outcome_description)
        score += score_change

    # yorker delivery
    elif length_code == 2: 
        if direction_code == 0:
            outcomes = {
                'glide': ("Thrust forward into the pad that the bowler should have been bowling to for a duck!", 4),
                'late cut': ("Thrust forward into the pad that the bowler should have been bowling to for a duck!", 4),
                'upper': ("Strikes a terrible ball from the bowler and smashes it over the fence for a boundary!", 6),
                'third': ("Lets out a loud and resounding 'ARRGH!' as the ball lands square on the pad and goes straight to the wicket-keeper for a catch!", 1),
                'pull': ("Lets out a loud and resounding 'ARRGH!' as the ball lands square on the pad and goes straight to the wicket-keeper for a catch!", 1)
            }
        random_shot = random.choice(available_shots)
        outcome_description, score_change = outcomes[random_shot]
        print(outcome_description)
        score += score_change

def get_input(prompt):
    print()
    print(prompt)
    print()
    return input(">> ").lower()

def end_game(result):
    print("Your score: ", str(score))
    print(result)
    input("\nPress Enter to exit")
    exit(0)

def start():
    global score
    global target
    difficulty = get_input("Enter difficulty level (easy, medium, hard): ")
    if difficulty == 'easy':
        target = 9
    elif difficulty == 'medium':
        target = 15
    else:
        target = 20
    for ball in range(0,6,1): 
        if score < target:            
            status(target,ball)           
        if score >= target:
            end_game("Congratulation you won!")
        length_code = random.randint(0,2)
        direction_code = random.randint(0,5)
        print(get_length_description(length_code), end=" ")
        print(get_direction_description(direction_code))

        available_shots_input = input("Enter available shots (space separated): ").lower()
        available_shots = available_shots_input.split()

        while len(available_shots) == 0:
            print("Invalid input. Please enter available shots (space separated): ")
            available_shots_input = input("Enter available shots (space separated): ").lower()
            available_shots = available_shots_input.split()

        play_shot(length_code, direction_code)

    if score == target-1:
        end_game("It's a draw")
    if score >= target:
        end_game("Congratulation you won!")

    input("\nPress Enter to exit")
    exit(0)

def status(target, ball):
    print()
    print("Runs to win".ljust(20) +": " + str(target-score))
    print("Balls remaining".ljust(20) +": " + str(6-ball))
    print()

score = 0
target = 0
print("WELCOME TO TEXT-CRICKET".center(55,"-"))
print() 
start()