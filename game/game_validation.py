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

  def validate_player(self, game_state, player_id):
    whos_turn = game_state.player_ids[(game_state.player_turn - 1)] 
    if player_id == whos_turn:
      return self.validation_result(True, [])
    else:
      if player_id in game_state.player_ids:
        player_number = game_state.player_ids.index(player_id) + 1
        message = "It is not Player " + str(player_number) + "'s turn to play."
        return self.validation_result(False, [message])
      else:
        return self.validation_result(False, ["There is no player with that ID in this game."])