#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: November 15
# This program generates two random values for Dice 1 and Dice 2.
# It continues generating random numbers until Dice 1 and Dice 2 match.

# imports random
import random

# import sleep
from time import sleep

# loadbar function that contains a starting load bar
# only displayed on the first run because
# it gets annoying when rolling many times
# extra function definition


def loadbar(iteration, total, prefix="",
            suffix="", decimals=1, length=100, fill="⚂ "):
    # the percentage of the bar, formatted string
    percent = ("{0:." + str(decimals) + "f}").format
    (100 * (iteration / float(total)))
    # determine how much of the bar is filled (cast to integer)
    # "//"  creates a floor (divisional),
    # removes the fraction aspect of a number
    filledLength = int(length * iteration // total)
    # the bar itself
    bar = fill * filledLength + "-" * (length - filledLength)
    # carriage return, brings cursor back to the beginning of the line "\r"
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end="\r")
    # end it if iteration is equal to total (prints out blank line)
    if iteration == total:
        print()


# list, display the code above in console (will print 40 dice symbols)
# I can't believe Mr. Coxall's linter states "l" is a bad variable name
items = list(range(0, 40))
items_variable = len(items)

# display the very first iteration
loadbar(
    0,
    items_variable,
    prefix="Rolling Dices...",
    suffix="Complete",
    length=items_variable,
)
for i, item in enumerate(items):
    # sleep function applied
    # manages the speed it is printed out to avoid seeing the display too fast
    sleep(0.1)
    loadbar(
        i + 1,
        items_variable,
        prefix="Rolling Dices...",
        suffix="Complete",
        length=items_variable,
    )


def main():

    # set the counter to 0, this is the value of the # of times the dice rolls
    counter = 0

    # using a do while loop to perform a
    # statement until a boolean expression is met.
    while True:
        # generate two random numbers
        secret_number = random.randint(0, 6)
        secret_number2 = random.randint(0, 6)
        # print both random numbers to the user
        print(f"Dice ⚀ = {secret_number} & Dice ⚁ = {secret_number2}")
        # increment the counter/# of dice rolls
        counter = counter + 1
        # if the two dice rolls are equal, break
        if secret_number == secret_number2:
            break

    # display to the user at what # of dice rolls, their pair of dices matched
    print(f"The dice matched at {counter} rolls")

    # calculate the percentage chance of rolling doubles
    percentage = 1 / counter
    final_percentage = percentage * 100

    print(f"The chance of this was {final_percentage}%")


if __name__ == "__main__":
    main()
    # ask the user for "y" or "n" to continue
    answer = input("Would you like to try again? (y/n): ")
    # use a while loop to loop back if user's input is "y"
    while answer == "y":
        main()
        answer = input("Would you like to try again? (y/n): ")

    # if user inputs n, thank them for playing
    if answer == "n":
        print("Thank you for playing.")

    # else, if none of the options above were inputted, output default message
    else:
        print("Program has ended.")
