from game.game_validation import GameValidation
from game.validation_result import ValidationResult

class GameInput:
  def __init__(self, game_validation=GameValidation(), validation_result=ValidationResult):
    self.game_validation = game_validation
    self.validation_result = validation_result

  def handle_input(self, state, player_id, coords):
    validate_player_result = self.game_validation.validate_player(state, player_id)
    validate_position_result = self.game_validation.validate_position(state, coords)
    errors = []
    if validate_player_result.success == False:
      errors.append(validate_player_result.errors[0])
    if validate_position_result.success == False:
      errors.append(validate_position_result.errors[0])
    if len(errors) > 0:
      print(errors)
      return self.validation_result(False, errors)
    else:
      return self.validation_result(True, [])
