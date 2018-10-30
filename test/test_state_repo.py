import os
from game.state_repo import StateRepo
from game.state_manager import StateManager

def test_write_state():
  sr = StateRepo()
  sm = StateManager()
  new_state = sm.create({
    "game_id": "debug_testing",
    "board_size": 5,
    "board_status": [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
    })
  sr.write_state(new_state)
  read_data = sr.read_state("debug_testing")
  assert read_data.board == {
    "size": 5,
    "status": [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
  }

def test_read_state():
  sr = StateRepo()
  sm = StateManager()
  new_state = sm.create({"game_id": "debug_testing"})
  sr.write_state(new_state)
  read_data = sr.read_state("debug_testing")
  assert read_data.board == {
    "size": 3,
    "status": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  }

def test_overwrite_state():
  sr = StateRepo()
  sm = StateManager()
  new_state = sm.create({
    "game_id": "debug_testing",
    "board_size": 5,
    "board_status": [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
    })
  sr.write_state(new_state)
  read_data = sr.read_state("debug_testing")
  assert read_data.board == {
    "size": 5,
    "status": [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
  }
  overwrite_state = sm.update(read_data, {"coordinates": [2, 2], "player_ids": ["debug", "testing"]})
  sr.write_state(overwrite_state)
  overwritten_read_data = sr.read_state("debug_testing")
  assert overwritten_read_data.board == {
    "size": 5,
    "status": [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 1, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
  }
  print(overwritten_read_data.history)
  assert overwritten_read_data.history[0].board == {
    "size": 5,
    "status": [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
  }

def test_delete_state():
  sr = StateRepo()
  sm = StateManager()
  current_dir = os.getcwd()
  data_folder_path = os.path.join(current_dir, r'data')

  new_state = sm.create({"game_id": "debug_testing"})
  state_file_location = os.path.join(data_folder_path, str(new_state.game_id) + ".dat")
  sr.write_state(new_state)
  sr.delete_state(new_state.game_id)
  
  assert os.path.exists(state_file_location) == False
  