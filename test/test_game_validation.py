from game.game_validation import GameValidation
from game.state_manager import StateManager

def test_position_validation_valid():
  game_valid = GameValidation()
  sm = StateManager()
  new_state = sm.create({"board_size": 3, "board_status": [[1, 1, 1], [1, 1, 1], [1, 0, 1]]})
  result = game_valid.validate_position(new_state, [2, 1])
  assert result.success == True
  assert result.errors == []

def test_position_validation_invalid():
  game_valid = GameValidation()
  sm = StateManager()
  new_state = sm.create({"board_size": 3, "board_status": [[0, 0, 0], [0, 0, 0], [0, 1, 0]]})
  result = game_valid.validate_position(new_state, [2, 1])
  assert result.success == False
  assert result.errors == ["This position is already populated..."]

def test_player_validate_valid():
  game_valid = GameValidation()
  sm = StateManager()
  new_state = sm.create({"game_id": "debug_testing"})
  result = game_valid.validate_player(new_state, new_state.player_ids[0])
  assert result.success == True
  assert result.errors == []

def test_player_validate_invalid():
  game_valid = GameValidation()
  sm = StateManager()
  new_state = sm.create({"game_id": "debug_testing"})
  result = game_valid.validate_player(new_state, new_state.player_ids[1])
  assert result.success == False
  assert result.errors == ["It is not Player 2's turn to play."]

def test_player_validate_non_existent():
  game_valid = GameValidation()
  sm = StateManager()
  new_state = sm.create({"game_id": "debug_testing"})
  result = game_valid.validate_player(new_state, "LOGIC")
  assert result.success == False
  assert result.errors == ["There is no player with that ID in this game."]