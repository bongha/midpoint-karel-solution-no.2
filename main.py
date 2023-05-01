from karel.stanfordkarel import *

def main():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()
    while no_beepers_present():
        fill_the_line()
    if facing_west():
        put_beeper()
    else:
        turn_around()
        move()
        put_beeper()
    while front_is_clear():
        move()
    turn_around()
    while front_is_clear():
        pick_beeper()
        move()
    pick_beeper()    
    turn_around()
    while no_beepers_present():
        move()
    turn_around()
    
def fill_the_line():
    while no_beepers_present():
        move()
    turn_around()
    move()
    put_beeper()
    move()
  
def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
