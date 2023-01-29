from sys import stdout, stdin
from time import sleep


class bg:
  black = "\u001b[40m"
  red = "\u001b[41m"
  green = "\u001b[42m"
  yellow = "\u001b[43m"
  blue = "\u001b[44m"
  magenta = "\u001b[45m"
  cyan = "\u001b[46m"
  white = "\u001b[47m"

  def rgb(r, g, b):
    return f"\u001b[48;2;{r};{g};{b}m"


class fg:
  black = "\u001b[30m"
  red = "\u001b[31m"
  green = "\u001b[32m"
  yellow = "\u001b[33m"
  blue = "\u001b[34m"
  magenta = "\u001b[35m"
  cyan = "\u001b[36m"
  white = "\u001b[37m"

  def rgb(r, g, b):
    return f"\u001b[38;2;{r};{g};{b}m"


class pencil:
  reset = "\u001b[0m"
  bold = "\u001b[1m"
  underline = "\u001b[4m"
  reverse = "\u001b[7m"

  clear = "\u001b[2J"
  clearline = "\u001b[2K"

  up = "\u001b[1A"
  down = "\u001b[1B"
  right = "\u001b[1C"
  left = "\u001b[1D"

  nextline = "\u001b[1E"
  prevline = "\u001b[1F"

  top = "\u001b[0;0H"

  def cls():
    pencil.write(fg.white + bg.black + pencil.clear + pencil.top)

  def to(x, y):
    return f"\u001b[{y};{x}H"

  def write(text="\n"):
    stdout.write(text)
    stdout.flush()

  def writew(text="\n", wait=0.05):
    for char in text:
      stdout.write(char)
      stdout.flush()
      sleep(wait)

  def writewb(*stuff, wait=0.5):
    for s in stuff:
      pencil.writew(s)
      sleep(wait)

  def read(begin=""):
    text = ""
    stdout.write(begin)
    stdout.flush()
    while True:
      char = ord(stdin.read(1))
      if char == 3:
        return
      elif char in (10, 13):
        return text
      else:
        text += chr(char)

  def readw(begin="", wait=0.05):
    text = ""
    for char in begin:
      stdout.write(char)
      stdout.flush()
      sleep(wait)

    while True:
      char = ord(stdin.read(1))
      if char == 3:
        return
      elif char in (10, 13):
        return text
      else:
        text += chr(char)


# MAN IN THE MIRROR


# constants for colors
class mitm:
  reset = bg.black + fg.white
  process = fg.black + bg.cyan
  option = fg.black + bg.green
  userChoice = fg.black + bg.yellow
  cutscene = fg.black + bg.magenta
  item = fg.black + bg.rgb(254, 80, 0)
  question = fg.white + bg.rgb(128, 0, 128)
  title = fg.black + bg.red
  error = fg.red + bg.black
