import _CORE_ as c
import os
from colorify import *
from time import sleep
import sys

def table():
    pencil.cls()
    pencil.readw(mitm.process + "You go to the table and find a paper on it. You pick it up and see that there is a chemical reaction written on it: ")
    pencil.write(mitm.reset + "NaOH + conc. H\u2082SO\u2084 → Na\u2082SO\u2084 + H\u2082O")
    if c.flags['#acidFound']:
        pencil.readw("\n" + mitm.process + "You now know exactly which chemicals to use so that you can neutralise the acid on the stairs...")
        c.flags[".learnReaction"] = True
    else:
        pencil.readw("\n" + mitm.process + "The equation doesn't really make sense, but you remember it anyway...")
        c.flags[".seeReaction"] = True

# --------------------------------------------------------------------------------------------------------------

def shelf():
    pencil.cls()
    pencil.readw(mitm.process + "You search through the shelves. No useful chemicals at all...")
    if c.flags[".learnReaction"]:
        pencil.writew("Finally you find a bottle of sodium.")
        pencil.readw(" You keep it for the reaction...")
        pencil.read("You found " + mitm.item + "SODIUM" + mitm.reset)
        c.flags["_sodium"] = True

# --------------------------------------------------------------------------------------------------------------

def exitRoom():
    c.stackCommand = "POP"
    return

# --------------------------------------------------------------------------------------------------------------

def exe(firstTime):
    options = {}
    pencil.write(pencil.reset)
    pencil.cls()
    pencil.write(mitm.process)

    if firstTime:
        pencil.readw("You enter the grey door. It looks like an abandoned chemistry lab, but no apparatus at all...")
        pencil.readw("There is a shelf on the wall with bottles of chemicals and a table in a corner...")
    else:
        pencil.write("You enter the grey door. It looks like an abandoned chemistry lab, but no apparatus at all.")
        pencil.write("\nThere is a huge closet leaned on the wall.\n")

    pencil.write(pencil.reset)
    if not c.flags[".learnReaction"]:
        sleep(0.5)
        pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset + " Inspect the table\n")
        options[1] = table

    if not c.flags["_sodium"]:
        sleep(0.5)
        pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset + " Inspect the shelf\n")
        options[2] = shelf

    if not False:
        sleep(0.5)
        pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset + " Exit the room\n")
        options[3] = exitRoom

    sleep(0.5)
    choice = pencil.read("Enter your choice: " + mitm.userChoice)
    if choice.isdigit():
        choice = int(choice)
        pencil.write(mitm.reset)
        if choice in options:
            options[choice]()
        else:
            pencil.read(mitm.error + "Invalid option!")
    else:
        pencil.read(mitm.error + "Enter an integer")

# --------------------------------------------------------------------------------------------------------------
