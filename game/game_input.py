from game.game_validation import GameValidation

class GameInput:
  def __init__(self, game_validation=GameValidation()):
    self.game_validation = game_validation

  def handle_coordinates(self, state, coords):
    return self.game_validation.validate_position(state, coords)
