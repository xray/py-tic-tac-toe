from game.state import StateManager

def test_dynamic_board():
  new_state = StateManager()
  assert new_state.create_board(5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_update_board():
  new_state = StateManager()
  new_state.update_board([2, 1])
  assert new_state.board == [[0, 0, 0], [0, 0, 0], [0, 1, 0]]

def test_board_size():
  new_state = StateManager()
  assert new_state.regulate_board_size(5) == 5

def test_board_size_too_big():
  new_state = StateManager()
  assert new_state.regulate_board_size(10) == 9

def test_win_top_row():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 3
      self.board = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
  assert new_state.is_game_complete(MockStateManager()) == (True, False)

def test_win_left_column():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 3
      self.board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
  assert new_state.is_game_complete(MockStateManager()) == (True, False)

def test_win_middle_column():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 3
      self.board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
  assert new_state.is_game_complete(MockStateManager()) == (True, False)

def test_incomplete_left_column():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 3
      self.board = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]
  assert new_state.is_game_complete(MockStateManager()) == (False, False)

def test_incomplete_left_column_one_move():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 3
      self.board = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
  assert new_state.is_game_complete(MockStateManager()) == (False, False)

def test_diagonal_left_to_right():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 4
      self.board = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
  assert new_state.is_game_complete(MockStateManager()) == (True, False)

def test_diagonal_right_to_left():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 4
      self.board = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
  assert new_state.is_game_complete(MockStateManager()) == (True, False)

def test_cats_game():
  new_state = StateManager()
  class MockStateManager:
    def __init__(self):
      self.board_size = 4
      self.board = [[1, 2, 1, 2], [2, 1, 2, 1], [2, 1, 2, 1], [1, 2, 1, 2]]
  assert new_state.is_game_complete(MockStateManager()) == (True, True)

def test_check_identical_values_all_ones():
  new_state = StateManager()
  test_array = [1, 1, 1, 1]
  assert new_state.check_identical_values(test_array) == True

def test_check_identical_values_all_twos():
  new_state = StateManager()
  test_array = [2, 2, 2, 2]
  assert new_state.check_identical_values(test_array) == True

def test_check_identical_values_all_zeros():
  new_state = StateManager()
  test_array = [0, 0, 0, 0]
  assert new_state.check_identical_values(test_array) == False
