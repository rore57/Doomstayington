from random import randrange

''' idk some text based adventure game with monsters '''

#----------------------------------------------------------------start--------------------------------------------------------------

print('press q to quit at anytime')
name = input('\nYou are a survivor, what is your name: ')
print(name + ' get ready for a dangerous adventure')

#----------------------------------------------------------------game body------------------------------------------------------------

def the_start():
    print('\nAs you open the hatch a bright light hits you')
    print('Your friend down in the bunker is injured, you need to find supplies or help')
    print('The path ahead will likely be fierce and unforgiving')
    print('But with equipped with your knife and revolver with 3 bullets you are determined')
    print('Ahead lies a forest, you see smoke coming from deep within the trees')
    print('To your left is a town, with a hospital a gun store')
    print('To your right are tall mountains that are completely unclimbable')

    while True:
        print('\nHead into the forrest press 1')
        print('\nHead towards the town press 2')

        ithestart = input('\nEnter Here: ')

        while True:
            if ithestart == '1':
                forward()
            elif ithestart == '2':
                left()
                ''' option 3 was took out of the game '''
            #elif ithestart == '3':
            #    right()
            #elif ithestart == 'q': 
                quitgame()
            else:
                print('This input is invalid try again')
                break
# through the forest

def forward():
    print('\nYou choose go into the forest')
    print('As you get deeper into the forest you hear the groans ahead of you')
    print('A gootenburger jumps out in front of you, you dont know if you can handle it')

    while True:
        print('\nWhat will you do?')
        print('Fire your gun at it in attempt to kill it press 1')
        print('Attempt to stab it to death to save your ammo press 2')
        iencounter = input('\nEnter Here: ')

        while True:
            if iencounter == '1':
                shoot_gootenburger()
            elif iencounter == '2':
                knife_gootenburger()
                '''
            elif iencounter == '3':
                run_gootenburger()
                '''
            elif iencounter == 'q':
                quitgame()
            else:
                print('\nInvalid input try again!')
                break

def shoot_gootenburger():
    per = str(randrange(1, 11, 1))
    iper = int(per)
    if iper <= 6:
        gootenburger_killed()
    elif iper >= 7:
        gootenburger_death()
    else:
        error_quit()


def knife_gootenburger():
    per = str(randrange(1, 11, 1))
    iper = int(per)
    if iper <= 4:
        gootenburger_killed()
    elif iper >= 5:
        gootenburger_death()
    else:
        error_quit()
        
'''
def run_gootenburger():
    per = str(randrange(1, 11, 1))
    iper = int(per)
    if iper <= 2:
        gootenburger_escape()
    elif iper >= 3:
        gootenburger_death()
    else:
        error_quit()
'''

def further_forest():
    print('\nyou go further and further into the forest, these dense deep woods make it impossible to see anything coming at you')
    print('you head to a clearing and see something quite interesting')
    print('there is a downed airplane, and as you go up to examine it people start to come out of it')
    print('"hello my name is Noah" one of the people exclaimed, what brings you into these woods?')
    print('realizing that these people could be the help you needed, you tell them that you and your friend are looking for food and medicine')
    print('skeptical of helping, the group claims that they do not have enough supplies to help outsiders, but if you join up with them they would have no problem helping you')

    while True:
        print('\nTo join up with this sketchy group of plane people press 1')
        print('To turn around and head back press 2')
        guyzz = input('Enter here: ')

        while True:
            if guyzz == '1':
                cannibalized()
            elif guyzz == '2':
                town_teim()
            else:
                print('\nInvalid input please try again')
                break


def cannibalized():
    print('\nThis crew is sketchy but you figure there is strenghth in numbers, you decide to join up with them')
    print('Noah motions for you to enter the plane "ok we should get ready to go back and help your friend" he says, you agree but something doesn\'t feel right')
    print('as Noah heads towards the back of the plane you start to look around, there are various blood soacked tools lying around the plane and everything is filthy')
    print('you slowly walk towards the cockpit and then you see it, out of the exit door you see the rest of the group eating something, a person')
    print('you turn around but are too late, Noah is standing in front of you, you bring up your gun but he is too fast and bashes you on the head')
    print('"I wish I could of at least found out where your friend was" he says as he drives as he stabs you')
    print('they then eat you because and it was very yucky thank god this is only a text based adventure game because the graphics would be nasty')
    game_over()

def town_teim():
    print('\nThere is something up with these people, better to not join up with them and turn around to head towards the town instead')
    print('as you head towards the town you find a dead body that has pieces torn out of it')
    print('it doesn\'t look like a creature did this, it almost looks surgically done, you pick up the pace as you head for a clearing that leads to the town')
    left()


def left():
    print('\nYou enter the town, it is quiet and you see a store and a hospital')
    print('\nDo you loot the hospital or loot the store?')

    while True:
        print('\nTo loot the hospital press 1')
        print('\nTo loot the store press 2')
        iloot = input('\nEnter here: ')

        while True:
            if iloot == '1':
                loot_hospital()
            elif iloot == '2':
                loot_store()
            else:
                print('\nInvalid input try again')
                break

def loot_hospital():
    print('\nAs you reach the hospitals glass doors you smash through them and head in')
    print('you head into the pharmacy section and find painkillers and antibiotics')
    print('this would be perfect for your friend back in the bunker, as you turn aroud you hear something slam the doors to the operating room open')
    print('it is a wantingbontingbollybop, they are extemely dangerous, and it is blocking the exit, do you fight it or hide?')

    while True:
        print('\nPress 1 to fight')
        print('\nPress 2 to hide')
        ithing = input('\nEnter here: ')

        while True:
            if ithing == '1':
                fight_wantingbontingbollybop()
            elif ithing == '2':
                hide_wantingbontingbollybop()
            else:
                print('\nInvalid input try again')
                break
 
def fight_wantingbontingbollybop():
    per = str(randrange(1, 11, 1))
    iper = int(per)
    if iper <= 6:
        wantingbontingbollybop_killed()
    elif iper >= 7:
        wantingbontingbollybop_death()
    else:
        error_quit()


def loot_store():
    print('\nyou enter the store and head through the aisles searching for something useful')
    print('you end up coming across some canned food and see a hunting section in the back of the store')
    print('interested, you head there, and you were able to find a shotgun and its dead owner')
    print('"he won\'t need this anymore" you think as you take it off of him, it could be useful for later')
    print('with some food you could hold out in the bunker for longer, should you return home or head to the hospital?')

    while True:
        print('\nPress 1 to head back home')
        print('\nPress 2 to head to the hospital')
        bingbo = input('Enter here: ')

        while True:
            if bingbo == '1':
                home_with_shotgun()
            elif bingbo == '2':
                secondary_hospital_loot()
            else:
                print('\nInvalid input please try again')
                break



def secondary_store_loot():
    print('\nyou head to the store to search for any leftover canned food')
    print('you search the aisles looking for anything useful, after awhile you find some canned food, you throw as much as you can carry in your backpack')
    print('as you round a corner you see a hunting section, interested you moce towards it, instantly regretting it as a foul stench hits you')
    print('you see a dead man clutching a shotgun, "he won\'t need this anymore" you think as you take it off him, it sure would\'ve been useful earlier')
    print('satisfied with what you have got, you decide to return home')
    home_with_shotgun()

def return_home():
    print('\ninjured and tired, you decide to return home')
    print('you limp out of the hospital, and head back to the hatch')
    print('as you round the corner to the hatch you see something that makes your heart drop')
    print('you see a heinzbraften scratching on the hatch trying to get in')
    print('in your current state and with no ammo you have no chance in killing it')
    print('you may have a chance to save your friend and not allow it to get into the hatch though')

    while True: 
        print('\nPress 1 to yell and lure the creature away from the hatch')
        print('\nPress 2 to leave your friend behind and start a new life because living in a hatch sucked anyways')

        bollybop = input('Enter here: ')
        while True: 
            if bollybop == '1':
                heinzbraften_death()
            if bollybop == '2':
                run_away_pansy()


def secondary_hospital_loot():
    print('\nyou enter the hospital and head towards the pharmacy')
    print('in the pharmacy you grab some painkillers and antibiotics for your friend, you then hear something outside')
    print('you exit the pharmacy and see a wantingbontingbollybop, you aim the shotgun at it and blow it away')
    print('you think "thank god I found this shotgun, these things won\'t stand a chance against me"')
    print('you decide to head home now, stocked up with all you need to help your friend')
    home_with_shotgun()

def home_with_shotgun():
    print('\nyou head back home with the spoils of your journey')
    print('as you round the corner to the hatch you see a heinzbraften')
    print('your heart drops, as you realize it is trying to open the hatch where your friend is')
    print('you scream at it as it turns and runs at you, putting your shotgun up and shoot it down')
    print('you breath a sigh of relif, and turn the hatch as you decend back into darkness, knowing it is all over for now')
    winner_yay()

#----------------------------------------------------------------deaths/kills-------------------------------------------------------------
def gootenburger_death():
    print('the gootenburger was too strong and fast, your attempts were futile against the beast and it has eaten you alive')
    game_over()

def gootenburger_killed():
    print('you took out the gootenburger, injured from the battle you think if you should head back to the town and loot the hospital')
    print('or to continue on into the forest, in hopes of finding others that could help you and your injured friends')

    while True:
        print('if you want to continue into the forest press 1')
        print('if you want to head to the town and loot the hospital press 2')
        baklava = input('\nEnter here: ')

        while True:
            if baklava == '1':
                further_forest()
            elif baklava == '2':
                loot_hospital()
            else:
                print('\nInvalid input please try again')
                break
        
def gootenburger_escape():
    print('escape')


def hide_wantingbontingbollybop():
    print('what are you trying to hide from a wantingbontingbollybop for? they have an insane sense of smell')
    print('you got brutally murdered it was very sad to see')
    game_over()


def wantingbontingbollybop_killed():
    print('\nyou survived this encounter, using all of your ammo on the wantingbontingbollybop')
    print('defensless and injured, it seems as if you should go back to the bunker with what meds you have gathered, do you attempt to loot the gun store?')

    while True:
        print('\nPress 1 to loot the store')
        print('\nPress 2 to go back to the bunker')
        ipks = input('\nEnter here: ')

        while True:
            if ipks == '1':
                secondary_store_loot()
            elif ipks == '2':
                return_home()
            else:
                print('\nInvalid input please try again')
                break

def wantingbontingbollybop_death():
    print('your attempts were valient')
    print('but it was too strong, you were overpowered and killed')
    game_over()

def heinzbraften_death():
    print('\nyou yell at the heinzbraften and it turns at see you')
    print('in an instant it runs towards you and turns you into dead and it eats you')
    print('satisfied and not hungry anymore, it scales the mountain by the hatch, ignoring the hatch it was once focused on')
    print('hearing the commotion, your friend exits the bunker and sees what happened, you saved their life, and they vow to continue to live in this harsh world for your sake')
    game_over()

def run_away_pansy():
    print('you turn your back and head back to the town, as you hear the heinzbraften rip open the hatch and enter the bunker')
    print('you don\'t turn back, you can\'t, the guilt overwhealms you but you keep pushing forward, hoping to survive by yourself in this lonely world')
    bad_ending()
#----------------------------------------------------------------game over/win-------------------------------------------------------------

def game_over():
    print('you died, game over')
    print('would you like to play again?')
    answer = input('press 1 to play again! press q to quit')
    if answer == '1':
        the_start()
    elif answer == 'q':
        quit_game()
    else:
        print('thanks for playing!')

def bad_ending():
    print('game over')
    print('would you like to play again?')
    answer = input('press 1 to play again! press q to quit')
    if answer == '1':
        the_start()
    elif answer == 'q':
        quit_game()
    else:
        print('you left your friend behind if you see this you should replay and not leave them meanie')

def winner_yay():
    print('thank you for playing! I hope you enjoyed!')
    answer = input('press 1 to play again! press q to quit')
    if answer == '1':
        the_start()
    elif answer == 'q':
        quit_game()
    else:
        print('good job surviving!')


    
#----------------------------------------------------------------idek I think quit outcomes-------------------------------------------------------------
def quit_game():
    print('>.>')
    break

def quitgame():
    print('^w^')
    break
#----------------------------------------------------------------technically impossible outcome-------------------------------------------------------------
def error_quit():
    print('how did you get here?')
    print('congrats you broke the game lol, you must kill the program and re-run sorry >.>')
    
the_start()
    
#credits:
#rory - me!
#whoever made randrange that/s cool
#thanks tony for teaching me python!
#I couldn't have done it without you
