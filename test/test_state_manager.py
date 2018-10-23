from game.state_manager import StateManager

def test_new_state():
  sm = StateManager()
  new_state = sm.create()
  assert new_state.board == {'size': 3, 'status': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}
  assert new_state.player_turn == 1
  assert new_state.player_count == 2
  assert new_state.history == []

def test_update_state():
  sm = StateManager()
  new_state = sm.create()
  updated_state = sm.update(new_state, {"coordinates": [1, 1]})
  assert updated_state.board == {'size': 3, 'status': [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}
  assert updated_state.player_turn == 2

def test_dynamic_board():
  sm = StateManager()
  new_state = sm.create({"board_size": 5})
  assert new_state.board["status"] == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_board_size():
  sm = StateManager()
  assert sm.regulate_board_size(5) == 5

def test_board_size_too_big():
  sm = StateManager()
  assert sm.regulate_board_size(10) == 9

def test_win_top_row():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
        "size": 3
      }
  assert sm.is_game_complete(MockState()) == (True, False)

def test_win_left_column():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
        "size": 3
      }
  assert sm.is_game_complete(MockState()) == (True, False)

def test_win_middle_column():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
        "size": 3
      }
  assert sm.is_game_complete(MockState()) == (True, False)

def test_incomplete_left_column():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[1, 0, 0], [1, 0, 0], [0, 0, 0]],
        "size": 3
      }
  assert sm.is_game_complete(MockState()) == (False, False)

def test_incomplete_left_column_one_move():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
        "size": 3
      }
  assert sm.is_game_complete(MockState()) == (False, False)

def test_diagonal_left_to_right():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        "size": 4
      }
  assert sm.is_game_complete(MockState()) == (True, False)

def test_diagonal_right_to_left():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]],
        "size": 4
      }
  assert sm.is_game_complete(MockState()) == (True, False)

def test_cats_game():
  sm = StateManager()
  class MockState:
    def __init__(self):
      self.board = {
        "status": [[1, 2, 1, 2], [2, 1, 2, 1], [2, 1, 2, 1], [1, 2, 1, 2]],
        "size": 4
      }
  assert sm.is_game_complete(MockState()) == (True, True)

def test_check_identical_values_all_ones():
  sm = StateManager()
  test_array = [1, 1, 1, 1]
  assert sm.check_identical_values(test_array) == True

def test_check_identical_values_all_twos():
  sm = StateManager()
  test_array = [2, 2, 2, 2]
  assert sm.check_identical_values(test_array) == True

def test_check_identical_values_all_zeros():
  sm = StateManager()
  test_array = [0, 0, 0, 0]
  assert sm.check_identical_values(test_array) == False
