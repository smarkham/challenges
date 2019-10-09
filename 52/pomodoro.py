""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

"""
At its simplest, create a timer for a set duration (eg 20 minutes) that "alarms" or notifies you at completion.

Go a step further and allow the user to specify the amount of time the Pomodoro Timer goes for.

Again, further develop the app by allowing it to loop. That is, Pomodoro Time > break time > Pomodoro Time > break time. Just like the pros!

Create a user interface if you have the time! PyGame or argparse perhaps? Maybe even make it web based with Flask 
or your other favourite web framework.
"""

from datetime import timedelta
import time

"""
When the timer reaches zero, ask the user if they are done, want to start the timer again, or take a
5 minute break.
"""

def welcome():
    header()
    user_input()

def header():
    print(f'~~~~~~~~~~********************~~~~~~~~~~')
    print(f'____Pomodoro Timer by Steven Markham____')
    print(f'~~~~~~~~~~********************~~~~~~~~~~')

def user_input():
    duration = input(f'Welcome to the Pomodoro Timer! Let me know when you want to be bothered (in minutes): ')
    pomodoro(int(duration))
    
def pomodoro(d):
    minutes_left = timedelta(minutes=d)
    
    while minutes_left:  
        print(f'Keep working! You have {str(minutes_left)} left.')
        time.sleep(1)
        minutes_left -= timedelta(seconds=1)
    
    next_input(d)
    
def next_input(d):
    print_d = 'minutes'
    
    if d == 1:
        print_d = 'minute.'
    
    selection = input(f'Your time is up! What would you like to do next:'
                      f'[1] Do another round of {str(d)} {print_d}'
                      f'[2] Take a 5 minute breather and start again.'
                      f'[3] No more! Get me out of here.'
                     )
    
    if selection == '1':
        pomodoro(d)
    elif selection == '2':
        breather()
    elif selection == '3':
        print(f'Thanks for stopping by! I will miss you...')
        exit()
    else:
        print(f'You cannot do that! Make another selection: ')

def breather():
    minutes_left = timedelta(minutes=5)
    
    while minutes_left:
        print(f'Fine! Leave! See if I care. I do not want to talk to you for another {minutes_left}!')
        time.sleep(1)
        minutes_left -= timedelta(seconds=1)
        
    user_input()
    
welcome()