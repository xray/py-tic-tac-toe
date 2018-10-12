import warnings
from game.view import View
from game.state import State

DEFAULT_DEPENDENCIES = {
  "view": View(),
  "state": State()
}

class UserInput:
  def __init__(self, injected_dependencies=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies.get("view")
    self.state = dependencies.get("state")
  
  def prompt(self):
    player_input = input("Make your move: ")
    validation = self.validate(player_input)
    if validation == True:
      return self.convert(player_input)
    else:
      for validation_issues in validation:
        self.view.error(validation_issues)
      return self.prompt()

  def validate(self, player_input):
    player_input = player_input.upper()
    selection = list(player_input)
    required_length = 2
    validation_errors = []
    if len(selection) > required_length:
      validation_errors.append("Input is " + str(len(selection) - 2) + " characters too long...")
    if len(selection) < required_length:
      validation_errors.append("Input is " + str(2 - len(selection)) + " characters too short...")
    if len(selection) > 0:
      if ord(selection[0].upper()) < 65 or ord(selection[0].upper()) > (64 + self.state.board_size):
        key_cap = chr(65 + (self.state.board_size - 1))
        validation_errors.append("\"" + str(selection[0]) + "\" is not one of the valid selctions in position 1... (A - " + key_cap + ")")
    if len(selection) > 1:
      if ord(selection[1].upper()) < 49 or ord(selection[1].upper()) > (48 + self.state.board_size):
        key_cap = chr(48 + self.state.board_size)
        validation_errors.append("\"" + str(selection[1]) + "\" is not one of the valid selctions in position 2... (1 - " + key_cap + ")")
    if len(validation_errors) > 0:
      return validation_errors
    else:
      return True

  def convert(self, player_input):
    player_input = player_input.upper()
    conversion = []
    conversion.append(ord(player_input[0].lower())-97)
    conversion.append(int(player_input[1]) - 1)
    return conversion
