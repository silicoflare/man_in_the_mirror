# Very important file. Don't mess with it unless you know what's happening in here.

# important constants
enter = '⎆'

# use this variable to modify stack
stackCommand = ''

# The flags which will be set when an event happens
# Types:
#       1] _ = item flag
#       2] . = action flag
#       3] # = cutscene flag
flags = {
  # attic room falgs
  "_chestKey": False,
  ".openChest": False,
  "_clay": False,
  "_copper": False,
  ".copperMolten": False,
  "_smallKey": False,
  ".smelt": False,
  ".openAttic": False,

  # attic flags
  "_hammer": False,
  "#acidFound": False,
  ".brokeLock": False,
  "#neutralized": False,

  # water room flags
  "_telephone": False,
  ".waterReacted": False,
  ".pushed": False,

  # chemical room flags
  "_sodium": False,
  ".learnReaction": False,
  ".seeReaction": False,

  # banquet hall falgs
  "#heightFromWin": False,
  "_knife": False,
  "_safeKey": False,

  # dance room flags
  "_crowbar": False,
  ".openedWindow": False,
  "_deliveryCard": False,
  ".planned": False,

  # reception flags
  "_coin": False,
  ".callPlaced": False,
  ".attachedCable": False
}