from game.validation_result import ValidationResult

class GameValidation:
  def __init__(self, validation_result=ValidationResult):
    self.validation_result = validation_result
  
  def validate_position(self, game_state, position):
    if game_state.board_is_filled(position):
      return self.validation_result(False, ["This position is already populated..."])
    else:
      return self.validation_result(True, [])

  def validate_player(self, game_state, player_id):
    if player_id == game_state.current_player():
      return self.validation_result(True, [])
    else:
      if game_state.player_exists(player_id):
        player_number = game_state.player_ids.index(player_id) + 1
        message = "It is not Player " + str(player_number) + "'s turn to play."
        return self.validation_result(False, [message])
      else:
        return self.validation_result(False, ["There is no player with that ID in this game."])
