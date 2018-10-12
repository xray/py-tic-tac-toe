from game.state import State

def test_dynamic_board():
  assert State().create_board(5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_update_board():
  new_state = State()
  new_state.update_board([2, 1])
  assert new_state.board == [[0, 0, 0], [0, 0, 0], [0, 1, 0]]

def test_board_size():
  assert State().regulate_board_size(5) == 5

def test_board_size_too_big():
  assert State().regulate_board_size(10) == 9