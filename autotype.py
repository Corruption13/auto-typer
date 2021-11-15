# Made to apologize to bess fren.
import keyboard
import time



keyboard.wait(' ')

file1 = open("lyrics.txt", 'r')

lyrics = file1.readlines()

while True:
    for line in lyrics:
        keyboard.write(line)
        keyboard.press_and_release('enter')
        time.sleep(2.5)


