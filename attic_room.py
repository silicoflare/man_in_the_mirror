import _CORE_ as c
import os
from colorify import *
from time import sleep
import sys


def boxLeft():
  pencil.cls()
  pencil.readw(
    mitm.process +
    "The box is made of wood and can hold many things, but it is locked...",
    0.05)
  if c.flags["_smallKey"]:
    cho = pencil.read(mitm.question + "Want to try to unlock it using " +
                      mitm.item + "SMALL KEY" + mitm.question + "?(Y/N):" +
                      mitm.reset + " " + mitm.userChoice).upper()
    if cho == 'N':
      return
    elif cho != 'Y':
      print()
      pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
      return
    else:
      pencil.write(mitm.process)
      print()
      pencil.readw("You insert and turn the key in the box, and it opens...",
                   0.05)
      pencil.read("YOU FOUND " + mitm.item + "CLAY" + mitm.reset)
      c.flags["_clay"] = True


def boxRight():
  pencil.cls()
  pencil.readw(
    mitm.process +
    "The box is made of wood and can hold many things, but it is locked...",
    0.05)
  if c.flags["_smallKey"]:
    cho = pencil.read(mitm.question + "Want to try to unlock it using " +
                      mitm.item + "SMALL KEY?(Y/N):" + mitm.reset + " " +
                      mitm.userChoice).upper()
    if cho == 'N':
      return
    elif cho != 'Y':
      print()
      pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
      return
    else:
      pencil.write(mitm.process)
      print()
      pencil.readw(
        "You insert and try to turn the key in the box, but it doesn't open...",
        0.05)


def furnace():
  pencil.cls()
  if not c.flags[".copperMolten"]:
    pencil.readw(mitm.process + "You go to the machine and inspect it. It is a furnace which can even melt metal. This is what that has been heating the room...")

  if c.flags[".copperMolten"]:
    pencil.readw(mitm.process + "There is the molten copper in this furnace...")
    if c.flags["_clay"]:
      cho = pencil.read(mitm.question + "Want to use the " + mitm.item +
                        "CLAY" + mitm.question + "?(Y/N):" + mitm.reset + " " +
                        mitm.userChoice).upper()
      if cho == 'N':
        return
      elif cho != 'Y':
        print()
        pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
        return
      else:
        pencil.write(mitm.process)
        print()
        pencil.readw(
          "You make a cup out of clay and scoop the molten copper into it...",
          0.05)
        c.flags[".smelt"] = True
        return

  if c.flags["_copper"] and not c.flags[".copperMolten"]:
    cho = pencil.read(mitm.question + "Want to use it to melt the " +
                      mitm.item + "PIECE OF COPPER" + mitm.question +
                      "?(Y/N):" + mitm.reset + " " + mitm.userChoice).upper()
    if cho == 'N':
      return
    elif cho != 'Y':
      print()
      pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
      return
    else:
      pencil.write(mitm.process)
      print()
      pencil.readw(
        "You put the piece of copper and melt it. Only if there was something to hold it...",
        0.05)
      c.flags[".copperMolten"] = True
      if c.flags["_clay"]:
        cho = pencil.read(mitm.question + "Want to use the " + mitm.item +
                          "CLAY" + mitm.question + "?(Y/N):" + mitm.reset +
                          " " + mitm.userChoice).upper()
        if cho == 'N':
          return
        elif cho != 'Y':
          print()
          pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
          return
        else:
          pencil.write(mitm.process)
          print()
          pencil.readw(
            "You make a cup out of clay and scoop the molten copper into it...",
            0.05)
          c.flags[".smelt"] = True


def bed():
  pencil.cls()
  pencil.readw(
    mitm.process +
    "You look at the bed on which you were lying. It seems pretty old, and now you start inspecting it..."
  )
  pencil.readw("Nothing on it...")
  pencil.readw(
    "You then see under the bed and find a piece of copper. It might be useful later..."
  )
  pencil.read("YOU FOUND " + mitm.item + "COPPER" + mitm.reset)
  c.flags["_copper"] = True


def window():
  pencil.cls()
  pencil.writew(mitm.process + "You go to the window and push it.")
  sleep(0.5)
  pencil.writew(
    " It opens a little and closes shut, but drops a small key down.")
  sleep(0.5)
  pencil.readw(" You pick it up...")
  pencil.read("YOU FOUND " + mitm.item + "SMALL KEY" + mitm.reset)
  c.flags["_smallKey"] = True


def door():
  pencil.cls()
  pencil.readw(mitm.process +
               "You go to the door and try to open it, but it is locked...")
  if c.flags["_smallKey"]:
    cho = pencil.read(mitm.question + "Want to try to unlock it using " +
                      mitm.item + "SMALL KEY" + mitm.question + "?(Y/N):" +
                      mitm.reset + " " + mitm.userChoice).upper()
    if cho == 'N':
      return
    elif cho != 'Y':
      print()
      pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
      return
    else:
      pencil.write(mitm.process)
      print()
      pencil.readw("You try to fit the key but it's too small...", 0.05)
      if c.flags[".smelt"]:
        cho = pencil.read(mitm.question + "Want to mess with the " +
                          mitm.item + "MOLTEN COPPER" + mitm.question +
                          "?(Y/N):" + mitm.reset + " " +
                          mitm.userChoice).upper()
        if cho == 'N':
          return
        elif cho != 'Y':
          print()
          pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
          return
        else:
          pencil.write(mitm.reset)
          pencil.cls()
          pencil.writew(
            mitm.cutscene +
            "You dip the key in the molten copper and immediately put in into the keyhole.\n"
          )
          sleep(0.5)
          pencil.readw(
            "It solidifies and then you turn it, and the lock clicks open as you enter what feels like an attic..."
          )
          c.stackCommand = "ADD atticMain"
          return


def exe(firstTime):
  options = {}
  pencil.write(pencil.reset)
  pencil.cls()
  pencil.write(mitm.process)
  if firstTime:
    pencil.readw(
      "You wake up on a bed in a small room. The room has two boxes, a weird machine, a small window and a door...",
      0.05)
    pencil.readw(
      "You are profusely sweating due to the air being unnaturally hot...",
      0.05)
  else:
    pencil.write(
      "You wake up on a bed in a small room. The room has two boxes, a weird machine, a small window and a door.\n"
    )
    pencil.write(
      "You are profusely sweating due to the air being unnaturally hot.\n")

  pencil.write(mitm.reset)
  if not c.flags["_clay"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset +
                 " Inspect the box on the left\n")
    options[1] = boxLeft

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset +
                 " Inspect the box on the right\n")
    options[2] = boxRight

  if not c.flags[".smelt"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset +
                 " Inspect the machine\n")
    options[3] = furnace

  if not c.flags["_copper"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "4]" + mitm.reset +
                 " Inspect the bed\n")
    options[4] = bed

  if not c.flags["_smallKey"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "5]" + mitm.reset +
                 " Inspect the window\n")
    options[5] = window

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "6]" + mitm.reset +
                 " Inspect the door\n")
    options[6] = door

  sleep(0.5)
  choice = pencil.read("Enter your choice: " + mitm.userChoice)
  if choice.isdigit():
    choice = int(choice)
    pencil.write(mitm.reset)
    if choice in options:
      options[choice]()
    else:
      pencil.read("Invalid option!")
  else:
    pencil.read("Enter an integer")
