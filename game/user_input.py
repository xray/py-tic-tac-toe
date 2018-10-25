import warnings
from game.view import View
from game.state import State

DEFAULT_DEPENDENCIES = {
  "view": View(),
  "state": State()
}

class ValidationResult:
  def __init__(self, is_valid, errors):
    self.is_valid = is_valid
    self.errors = errors

class UserInput:
  def __init__(self, injected_dependencies=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies.get("view")
    self.state = dependencies.get("state")
  
  def prompt(self):
    player_input = input("Make your move: ")
    return player_input
  
  def get_valid_input(self, game_state=None):
    if game_state == None:
      game_state = self.state
    player_in = self.prompt()
    if self.validate_input(player_in).is_valid:
      player_in_conversion = self.convert(player_in)
      if self.validate_position(player_in_conversion, game_state):
        return player_in_conversion
      else:
        return self.get_valid_input(game_state)
    else:
      return self.get_valid_input(game_state)

  def validate_position(self, position, game_state):
    if game_state.board[position[0]][position[1]] != 0:
      self.view.error("This position is already populated...")
      return False
    else:
      return True

  def validate_input(self, player_input):
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
      for validation_issues in validation_errors:
        self.view.error(validation_issues)
      return ValidationResult(False, validation_errors)
    else:
      return ValidationResult(True, [])

  def convert(self, player_input):
    player_input = player_input.upper()
    conversion = []
    conversion.append(ord(player_input[0].lower())-97)
    conversion.append(int(player_input[1]) - 1)
    return conversion
