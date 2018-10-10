from game.view import View

DEFAULT_DEPENDENCIES = {
  "view": View()
}

class UserInput:
  def __init__(self, injected_dependencies={}):
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies["view"]
  
  def prompt(self):
    player_input = input("Make your move: ")
    try:
      self.validate(player_input)
      return self.convert(player_input)
    except UserWarning as error:
      self.view.error(error)
      self.prompt()

  def validate(self, player_input):
    player_input = player_input.upper()
    selection = list(player_input)
    required_length = 2
    if len(selection) > required_length:
      raise UserWarning("Input is " + str(len(selection) - 2) + " characters too long...")
    if len(selection) < required_length:
      raise UserWarning("Input is " + str(2 - len(selection)) + " characters too short...")
    if selection[0] != "T" and selection[0] != "M" and selection[0] != "B":
      raise UserWarning("\"" + str(selection[0]) + "\" is not one of the valid selctions... (T, M, or B)")
    if selection[1] != "L" and selection[1] != "M" and selection[1] != "R":
      raise UserWarning("\"" + str(selection[1]) + "\" is not one of the valid selctions... (L, M, or R)")
    return True

  def convert(self, player_input):
    player_input = player_input.upper()
    conversion = []
    selection = list(player_input)
    if selection[0] == "T":
      conversion.append(0)
    elif selection[0] == "M":
      conversion.append(1)
    else:
      conversion.append(2)
    if selection[1] == "L":
      conversion.append(0)
    elif selection[1] == "M":
      conversion.append(1)
    else:
      conversion.append(2)
    return conversion
