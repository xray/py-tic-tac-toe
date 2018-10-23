from game.validation_result import ValidationResult

class GameValidation:
  def __init__(self, validation_result=ValidationResult):
    self.validation_result = validation_result
  
  def validate_position(self, game_state, position):
    if game_state.board["status"][position[0]][position[1]] != 0:
      result = self.validation_result(False, ["This position is already populated..."])
      return result
    else:
      return self.validation_result(True, [])