import _CORE_ as c
from colorify import bg, fg, pencil, mitm
from time import sleep


def window():
  pencil.cls()
  pencil.writew(
    mitm.cutscene +
    "You look out of the window. It is very dark outside, but you can see the building you are in due to moonlight."
  )
  sleep(0.5)
  pencil.readw(" You see that it has 4 floors in total...")
  sleep(0.5)
  pencil.readw(
    "You feel the urge to get away from there as soon as possible...")
  c.flags["#heightFromWin"] = True


# -------------------------------------------------------------------------------------------------------------


def mirror():
  pencil.cls()
  pencil.writew(mitm.cutscene + "You look at yourself in the mirror. ")
  sleep(0.5)
  pencil.writew(
    "You look exhausted and disturbed, thanks to that sinister experience. ")
  sleep(0.5)
  pencil.readw(
    "As you go into thoughts of you wishing to be at home than being stuck in this place, you see something so frightening that you almost start crying..."
  )
  pencil.readw(
    "In one of the dark corners of the room, near the dance hall door, you see a dark silhouette of a man with glowing eyes glaring at you..."
  )
  pencil.writew(
    "You stare at that figure, aghast, and when you come back to your senses and turn back, there is no one but the door swings open and you here footsteps from inside. "
  )
  sleep(0.5)
  pencil.writew(
    "It is then you realise, you are not alone in that building. \n")
  sleep(0.5)
  pencil.readw(
    "There is someone sinister and frightening in that with eyes on you, always..."
  )
  pencil.writew("It is the Man In The Mirror, ")
  sleep(0.5)
  pencil.readw("and he is on the hunt for you...")
  pencil.read("You found " + mitm.item + "SAFE KEY" + mitm.reset)
  c.flags["_safeKey"] = True


# -------------------------------------------------------------------------------------------------------------


def desks():
  pencil.cls()
  pencil.readw(
    mitm.process +
    "You go to the desks and open them, but you don't find anything..." +
    mitm.reset)


# -------------------------------------------------------------------------------------------------------------


def banquetTable():
  pencil.cls()
  pencil.write(mitm.process)
  pencil.writewb(
    "You search on the table everywhere, up and down, right and left. ",
    "It is completely empty. ", "Save for a tablecloth. ",
    "\nAs you are about to leave, ",
    "you trip on the tablecloth and a knife tinkles down from it.")
  pencil.readw(" You pick the knife...")
  pencil.read("You found " + mitm.item + "KNIFE" + mitm.reset)
  c.flags["_knife"] = True


# -------------------------------------------------------------------------------------------------------------


def danceHall():
  pencil.cls()
  if not c.flags["_safeKey"]:
    pencil.readw(mitm.process +
                 "You try to open the door, but it is locked...")
  else:
    pencil.readw(mitm.process +
                 "You open the door and enter the dance hall...")
    c.stackCommand = "ADD danceHall"


# -------------------------------------------------------------------------------------------------------------


def goBack():
  c.stackCommand = "POP"
  return


# -------------------------------------------------------------------------------------------------------------


def exe(firstTime: bool):
  """
    Main execution of the room

    firstTime
        To specify whether the room is displayed for the first time or not
    """
  options = {}
  pencil.write(pencil.reset)
  pencil.cls()
  pencil.write(mitm.process)

  if firstTime:
    pencil.writew(
      "You enter an abandoned banquet hall. It has a small dining table in the centre, with five chairs each on the sides. "
    )
    pencil.writew(
      "\nThere is a closet on one side of the room and a set of desks on the other side."
    )
    pencil.writew(
      "\nThere is a also a door at the opposite side which appears to not have a handle."
    )
    pencil.readw("\nLastly, there is a large mirror on the wall...")
  else:
    pencil.write(
      "You enter an abandoned banquet hall. It has a small dining table in the centre, with five chairs each on the sides. "
    )
    pencil.write(
      "\nThere is a closet on one side of the room and a set of desks on the other side."
    )
    pencil.write(
      "\nThere is a also a door at the opposite side which appears to not have a handle."
    )
    pencil.write("\nLastly, there is a large mirror on the wall.\n")

  pencil.write(mitm.reset)

  if not c.flags["#heightFromWin"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset +
                 " Inspect the window\n")
    options[1] = window

  if not c.flags["_safeKey"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset +
                 " Inspect the mirror\n")
    options[2] = mirror

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset +
                 " Inspect the desks\n")
    options[3] = desks

  if not c.flags["_knife"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "4]" + mitm.reset +
                 " Inspect the banquet table\n")
    options[4] = banquetTable

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "5]" + mitm.reset +
                 " Inspect the dance hall door\n")
    options[5] = danceHall

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "6]" + mitm.reset +
                 " Go back to the attic\n")
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


# -------------------------------------------------------------------------------------------------------------
