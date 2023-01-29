import _CORE_ as c
from colorify import pencil, mitm, bg, fg
from time import sleep

# --------------------------------------------------------------------------------------------------------------


def table():
  pencil.cls()
  pencil.writewb(mitm.process + "You go to the table and search on it. ",
                 "Nothing interesting.")
  pencil.readw("You then check the desk and find a coin...")
  pencil.read("YOU FOUND " + mitm.item + "COIN" + mitm.reset)
  c.flags["_coin"] = True


# --------------------------------------------------------------------------------------------------------------


def telephone():
  pencil.cls()
  pencil.writewb(mitm.process + "You go to the telephone and inspect it. ",
                 " It looks like it still works.")
  pencil.readw("\nJust that the telephone receiver is missing...")

  if c.flags["_telephone"] and not c.flags[".attachedCable"]:
    cho = pencil.read(mitm.question + "Attach the " + mitm.item +
                      "TELEPHONE RECEIVER" + mitm.question + "?(Y/N):" +
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
        "You attached the receiver, and then you hear the dial tone...")
      pencil.readw("But it looks like you need a coin to use it...")
      c.flags[".attachedCable"] = True

  if c.flags[".attachedCable"]:
    pencil.readw(mitm.process +
                 "You have attached the receiver, and it just needs a coin...")

    if c.flags["_coin"] and c.flags["_deliveryCard"]:
      cho = pencil.read(mitm.question + "Use the " + mitm.item + "COIN" +
                        mitm.question + "?(Y/N):" + mitm.reset + " " +
                        mitm.userChoice).upper()
      if cho == 'N':
        return
      elif cho != 'Y':
        print()
        pencil.write(bg.black + fg.red + "Invalid option!" + mitm.reset)
        return
      else:
        pencil.write(mitm.process)
        pencil.readw("You insert the coin, and dial the number...")
        pencil.readw(
          "You ask them to bring a couple old mattresses stacked on each other, in the truck..."
        )
        pencil.readw(
          "Though confused why would a person want old matresses, they agree to it..."
        )
        pencil.readw(mitm.item + "CALL PLACED.")
        c.flags[".callPlaced"] = True


# --------------------------------------------------------------------------------------------------------------


def mainDoor():
  pencil.cls()
  pencil.writewb(mitm.process + "You go to the main door and try to open it. ",
                 "No matter how much you try, it doesn't move an inch.")
  pencil.readw("\nLooks like the only option you have now is the window...")


# --------------------------------------------------------------------------------------------------------------


def exe(firstTime):
  options = {}
  pencil.write(pencil.reset)
  pencil.cls()
  pencil.write(mitm.process)
  if firstTime:
    pencil.writew(
      "You enter the reception, which is completely empty aside from a table, a help desk, and a telephone. "
    )
    sleep(0.5)
    pencil.writewb("Finally you see it. ", "The entrance door too. ")
    pencil.readw("You can now escape!...")

  if not c.flags["_coin"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "1]" + mitm.reset +
                 " Inspect the table\n")
    options[1] = table

  if not c.flags[".callPlaced"]:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "2]" + mitm.reset +
                 " Inspect the telephone\n")
    options[2] = telephone

  if not False:
    sleep(0.5)
    pencil.write(mitm.reset + "    " + mitm.option + "3]" + mitm.reset +
                 " Inspect the main door\n")
    options[3] = mainDoor

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
