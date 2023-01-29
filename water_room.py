import _CORE_ as c
from colorify import mitm, pencil, bg, fg
from time import sleep


def closet():
  pencil.cls()
  if not c.flags["_crowbar"]:
    pencil.readw(mitm.process +
      "It looks a normal closet, but on close observation you find a gap small enough to put a lever rod and push it away..."
    )

  if c.flags[".pushed"]:
    pencil.readw(mitm.process +
      "It is a closet which has been pushed aside, revealing a safe...")
    if c.flags["_safeKey"]:
      cho = pencil.read(mitm.question + "Want to use the " + mitm.item +
                        "SAFE KEY" + mitm.question + "?(Y/N):" + mitm.reset +
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
        pencil.writew("You unlock the deskand find a telephone reciever.")
        pencil.readw(" You keep it with you...")
        pencil.read("You found " + mitm.item + "TELEPHONE RECEIVER" +
                    mitm.reset)
        c.flags["_telephone"] = True

  if c.flags["_crowbar"]:
    cho = pencil.read(mitm.question +
                      "Want to try to push the closet away using " +
                      mitm.item + "CROWBAR" + mitm.question + "?(Y/N):" +
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
        "You push away the rack using the crowbar. It reveals a safe in the wall...",
        0.05)
      c.flags[".pushed"] = True
      if c.flags["_safeKey"]:
        cho = pencil.read(mitm.question + "Want to use the " + mitm.item +
                          "SAFE KEY" + mitm.question + "?(Y/N):" + mitm.reset +
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
          pencil.writew("You unlock the deskand find a telephone reciever.")
          pencil.readw(" You keep it with you...")
          pencil.read("You found " + mitm.item + "TELEPHONE RECEIVER" +
                      mitm.reset)
          c.flags["_telephone"] = True


# --------------------------------------------------------------------------------------------------------------


def puddle():
  pencil.cls()
  pencil.readw(mitm.process +
    "You go to the puddle. The water is fresh enough for a reaction..."
  )
  if c.flags["_sodium"]:
    cho = pencil.read(mitm.question + "Want to use the " + mitm.item +
                      "SODIUM" + mitm.question + "?(Y/N):" + mitm.reset + " " +
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
      pencil.writew(
        "You pour sodium into the water which reacts explosively and leaves a residue."
      )
      pencil.readw(" You collect this residue in the bottle...")
      pencil.read("You found " + mitm.item + "NaOH" + mitm.reset)
      c.flags[".waterReacted"] = True


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
    pencil.readw(mitm.process +
      "You enter the white door. It has water dripping from the ceiling and has formed a puddle..."
    )
    pencil.readw("There is a huge closet leaned on the wall...")
  else:
    pencil.write(mitm.process +
      "You enter the white door. It has water dripping from the ceiling and has formed a puddle."
    )
    pencil.write("\nThere is a huge closet leaned on the wall.\n")

  pencil.write(pencil.reset)
  if not c.flags["_telephone"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset +
                 " Inspect the closet\n")
    options[1] = closet

  if not c.flags[".waterReacted"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset +
                 " Inspect the puddle\n")
    options[2] = puddle

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset +
                 " Exit the room\n")
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
