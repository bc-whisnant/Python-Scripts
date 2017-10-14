import random

#from Tkinter import *

passwordContents = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2",
                    "3", "4", "5", "6", "7", "8", "9"]

def generateAPassword():
    generated_eight_characters = random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents)

    print(generated_eight_characters)

    generated_twelve_characters = random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents)

    print(generated_twelve_characters)

    generated_sixteen_characters = random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents) + random.choice(passwordContents) + random.choice(
        passwordContents) + random.choice(
        passwordContents) + random.choice(passwordContents)

    print(generated_sixteen_characters)




generateAPassword()
