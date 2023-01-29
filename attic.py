import _CORE_ as c
from colorify import pencil, mitm, bg, fg
from time import sleep


def table():
  pencil.cls()
  pencil.writew(mitm.process + "You go to the table and find a hammer on it.")
  pencil.readw(' It might be useful...')
  pencil.read("YOU FOUND " + mitm.item + "HAMMER" + mitm.reset)
  c.flags["_hammer"] = True


# --------------------------------------------------------------------------------------------------------------


def whiteDoor():
  pencil.cls()
  pencil.writew(mitm.process + "You go to the white door and open it.")
  pencil.readw(" There is a room inside...")
  c.stackCommand = "ADD waterRoom"
  return


# --------------------------------------------------------------------------------------------------------------


def greyDoor():
  pencil.cls()
  pencil.write(mitm.process)
  if not c.flags[".brokeLock"]:
    pencil.writew("You go to the grey door and inspect the padlock.")
    sleep(0.5)
    pencil.writew(" It is old.")
    pencil.readw(" Only if you had something to break it open...")
    if c.flags["_hammer"]:
      cho = pencil.read(mitm.question + "Want to try to unlock it using " +
                        mitm.item + "HAMMER" + mitm.question + "?(Y/N):" +
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
        pencil.readw(
          "You break open the lock and open the door. It leads into a room...",
          0.05)
        c.flags[".brokeLock"] = True
        c.stackCommand = 'ADD chemicalRoom'
        return
  else:
    c.stackCommand = 'ADD chemicalRoom'
    return


# --------------------------------------------------------------------------------------------------------------


def stairs():
  pencil.cls()
  if not c.flags["#acidFound"]:
    pencil.readw(
      mitm.cutscene +
      '''You go to the stairs and notice a liquid on the stairs. While you were wondering what it is, you sneeze because of the dust and a piece of blue litmus paper stuck to you falls onto the liquid. It instantly turns red and corrodes to dust. You understand it is an acid not to be messed with. Only if there was something to neutralize it...'''
    )
    if c.flags[".seeReaction"]:
      pencil.readw(mitm.process + 'Now you understood what the reaction was for...')
      c.flags[".learnReaction"] = True
    c.flags["#acidFound"] = True
  else:
    pencil.readw(mitm.process +
                 "There is the strong acid on the stairs. You cannot pass...")

  if c.flags["#neutralized"]:
    pencil.cls()
    pencil.readw(mitm.process + "You go down the stairs...")
    c.stackCommand = "ADD banquetHall"
    return

  if c.flags[".waterReacted"]:
    stuff = mitm.question + "Want to use the " + mitm.item + "NaOH" + mitm.question + "?(Y/N):" + mitm.reset + " " + mitm.userChoice
    cho = pencil.read(stuff).upper()
    if cho == 'N':
      return
    elif cho != 'Y':
      print()
      pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
      return
    else:
      pencil.write(mitm.reset)
      pencil.cls()
      pencil.write(mitm.cutscene)
      print()
      pencil.writew(
        "You pour the chemical on to the acid, and it neutralises with a sizzling sound. You go down the stairs and find a door."
      )
      sleep(0.5)
      pencil.writew(
        " As you are about to open it, you come across a sinister realization: "
      )
      sleep(0.5)
      pencil.writew("\nConcentrated acids evaporate fast.", 0.1)
      sleep(0.25)
      pencil.writew(" Really fast.", 0.1)
      sleep(0.5)
      pencil.writew("\nThen why was acid on the stairs at the first place")
      pencil.writew("...?", 0.5)
      sleep(0.5)
      pencil.readw(
        "\nSuddenly you hear creaking sounds from the attic as you open the door into an abandoned banquet hall..."
      )
      c.stackCommand = "ADD banquetHall"
      c.flags["#neutralized"] = True
      return

  


# --------------------------------------------------------------------------------------------------------------


def exe(firstTime):
  options = {}
  pencil.write(pencil.reset)
  pencil.cls()
  pencil.write(mitm.process)

  if firstTime:
    pencil.readw(
      "You enter an attic-ish room which is completely dusty. There is a grey coloured door with a padlock on it, and a white coloured door..."
    )
    pencil.readw(
      "There is a table in the corner, and at the other end of the room are stairs that go downwards..."
    )
  else:
    pencil.write(
      "You enter an attic-ish room which is completely dusty. There is a grey coloured door with a padlock on it, and a white coloured door.\n"
    )
    pencil.write(
      "There is a table in the corner, and at the other end of the room are stairs that go downwards.\n"
    )

  pencil.write(pencil.reset)
  if not c.flags["_hammer"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset +
                 " Inspect the table\n")
    options[1] = table

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset +
                 " Inspect the white door\n")
    options[2] = whiteDoor

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset +
                 " Inspect the grey door\n")
    options[3] = greyDoor

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "4]" + mitm.reset +
                 " Inspect the stairs\n")
    options[4] = stairs

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
