# IMPORTS
from HQ import control
import _CORE_ as c
from colorify import fg, bg, pencil, mitm
from time import sleep

# --------------------------------------------------------------------------------------------------------------

# CONTROL STACK AND FUNCTIONS
stack = []


def push(fn):
  stack.append(fn)


def pop():
  stack.pop()


def peek():
  return stack[len(stack) - 1]


# --------------------------------------------------------------------------------------------------------------

# INITIALIZATION
# push(control["atticRoom"])

push(control["danceHall"])

# --------------------------------------------------------------------------------------------------------------


# GAME CONTROL VARIABLES AND FUNCTIONS
def start():
  isFirstTime = True
  while True:
    if c.stackCommand == '':
      pass
    else:
      tokens = c.stackCommand.split(' ')
      if tokens[0] == "ADD":
        push(control[tokens[1]])
        isFirstTime = True
        c.stackCommand = ''
      elif tokens[0] == "POP":
        pop()
        c.stackCommand = ''

    if isFirstTime:
      peek()(True)
      isFirstTime = False
    else:
      peek()(False)


# --------------------------------------------------------------------------------------------------------------

# MAIN PROGRAM
pencil.cls()
pencil.writew(mitm.title + "MAN IN THE MIRROR: ", 0.1)
sleep(0.5)
pencil.writew("THE ESCAPE" + mitm.reset + "\n")
dir(c)
pencil.read(mitm.userChoice + "Press ENTER to continue..." + mitm.reset)
pencil.cls()
pencil.write(mitm.process + "INSTRUCTIONS:")
pencil.read(
  mitm.reset +
  ''' This game displays all text as if it is being typed. Please don't press anything till it's done.
Press ENTER only when a line ends with three dots (...)\n\n'''+
f'''Cutscenes are colored in {mitm.cutscene}magenta{mitm.reset}, so wait till the complete cutscene is completed before pressing ENTER.'''+
'''\n\nPress ENTER to dive down deep into the world of uncertainity...''')
start()
