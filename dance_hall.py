import _CORE_ as c
from colorify import pencil, mitm, bg, fg
from time import sleep
import sys

def gramaphone():
  pencil.cls()
  pencil.write(mitm.process)
  pencil.writew("You go to the gramaphone and inspect it. ")
  sleep(0.5)
  pencil.readw("It is pretty old. No chances of it working...")
  pencil.readw("You fiddle with the gramaphone and a contact card of a mattress delivery service falls down...")
  pencil.read("YOU FOUND " + mitm.item + "CONTACT CARD" + mitm.reset)
  c.flags["_deliveryCard"] = True

# --------------------------------------------------------------------------------------------------------------

def tableLeft():
  pencil.cls()
  pencil.readw("You go to the table on the left and inspect it. You find nothing...")

# --------------------------------------------------------------------------------------------------------------

def tableRight():
  pencil.cls()
  pencil.readw("You go to the table on the right and find a crowbar on it. It might be useful...")
  pencil.read("YOU FOUND " + mitm.item + "CROWBAR" + mitm.reset)
  c.flags["_crowbar"] = True

# --------------------------------------------------------------------------------------------------------------

def escapeWindow():
  pencil.cls()
  pencil.write(mitm.process)
  if not c.flags[".openedWindow"]:
    pencil.readw("The window is closed with a rope tied to the frame. Only if you had something to cut it off...")
    if c.flags["_knife"]:
      cho = pencil.read(mitm.question + "Want to try to cut it using " +
                        mitm.item + "KNIFE" + mitm.question + "?(Y/N):" +
                        mitm.reset + " " + mitm.userChoice).upper()
      if cho == 'N':
        return
      elif cho != 'Y':
        print()
        pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
        return
      else:
        pencil.write(mitm.process)
        pencil.readw(
          "You cut the rope with the knife, and the window falls open...")
        c.flags[".openedWindow"] = True

  if c.flags[".openedWindow"]:
    pencil.cls()
    pencil.writewb(
      mitm.cutscene + "You look through the window. ",
      "It is still dark outside, and you look down. ",
      "You are on the second floor, and there is one chance of escape: ",
      "A jump through the window. ")
    pencil.readw("But to survive you need something to break your fall...")

    if c.flags["_deliveryCard"] and not c.flags[".planned"]:
      pencil.writewb(
        "Oh yes! ", "The mattress delivery service exists! \n",
        "You need to somehow place a call to that service and order a good amount of them so that you will land safely.\n",
        "As you are lost in calculations and ideas, the gramophone in the corner of the room starts playing all of a sudden, which frightens you to death. ",
        "You go to the gramaphone to turn it off, and then look back at the window. "
      )
      pencil.readw(
        "To your horror, you find yourself standing face to face with the Man In The Mirror..."
      )
      pencil.writewb(
        "You close your eyes, and scream at the top of your voice. But when you open your eyes, he is gone.",
        " Now you are sure of one thing: ")
      pencil.readw("You must either escape fast or scream to death...")
      c.flags[".planned"] = True

  
  if c.flags[".callPlaced"]:
    pencil.cls()
    pencil.writew(mitm.cutscene)
    pencil.writewb(
      "You go to the window and wait desperately for the mattress truck to arrive. ",
      "After half an hour he finally arrives and parks the truck as you told him to do. ",
      "Without waiting for another second, you jump out of the window and fortunately land safely on the mattresses. ",
      "You then yell at the driver to speed away, which he does. ",
      "As you breath a sigh of relief and look at the building that held you prisoner for such a long time, "
    )
    pencil.readw("you see him again..", 0.1)
    pencil.readw("Those glaring eyes, from the window you took your leap of life...")
    pencil.writew("You wish to never see those eyes again, ")
    sleep(0.5)
    pencil.readw("but little did you know that those eyes will haunt you for the rest of your life...")

    pencil.cls()
    pencil.readw(mitm.title + "THE END", 0.1)
    pencil.writew("\n\nOr...? ", 0.1)
    pencil.readw("To be continued??")
    pencil.readw("\nOnly time will tell...", 0.1)
    sys.exit()
  
  if c.flags[".planned"]:
    pencil.readw(mitm.process + "You need to place a call to the mattress service before doing anything else...")

# --------------------------------------------------------------------------------------------------------------

def receptionDoor():
  pencil.cls()
  pencil.readw(mitm.process + "You open the door and enter the dance hall...")
  c.stackCommand = "ADD danceHall"
  return

# --------------------------------------------------------------------------------------------------------------

def goBack():
  pencil.cls()
  c.stackCommand = "POP"
  return

# --------------------------------------------------------------------------------------------------------------

def exe(firstTime):
  options = {}
  pencil.write(pencil.reset)
  pencil.cls()
  pencil.write(mitm.process)
  if firstTime:
    pencil.readw("You enter the dance floor from the banquet hall, breathing heavily and unsure where to proceed...")
    pencil.readw("You see two tables at each side of the hall, with a stage in the centre...")
    pencil.readw("You also see a gramaphone, a large window and a door that leads downstairs...")
  else:
    pencil.write("You enter the dance floor from the banquet hall, breathing heavily and unsure where to proceed.\n")
    pencil.write("You see two tables at each side of the hall, with a stage in the centre.\n")
    pencil.write("You also see a gramaphone, a large window and a door that leads downstairs.\n")

  pencil.write(mitm.reset)
  if not c.flags["_deliveryCard"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset +
                 " Inspect the gramaphone\n")
    options[1] = gramaphone

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset +
                 " Inspect the table on the left\n")
    options[2] = tableLeft

  if not c.flags["_crowbar"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset +
                 " Inspect the table on the right\n")
    options[3] = tableRight

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "4]" + mitm.reset +
                 " Inspect the window\n")
    options[4] = escapeWindow

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "5]" + mitm.reset +
                 " Inspect the door\n")
    options[5] = receptionDoor

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "6]" + mitm.reset +
                 " Go back to banquet hall\n")
    options[6] = goBack

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