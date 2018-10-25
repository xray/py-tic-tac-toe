from game.view import View

DEFAULT_DEPENDENCIES = {
  "view": View()
}

class State:
  def __init__(self, board_size=3, injected_dependencies=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies.get("view")
    self.user_input = []
    self.player1_turn = True
    self.board_size = self.regulate_board_size(board_size)
    self.board = self.create_board(self.board_size)
  
  def update_input(self, player_input):
    self.user_input = player_input

  def create_board(self, board_size=None):
    if board_size == None:
      board_size = self.board_size
    new_board = []
    for length in range(board_size):
      new_section = []
      for width in range(board_size):
        new_section.append(0)
      new_board.append(new_section)
    return new_board

  def update_board(self, coordinates):
    if self.player1_turn:
      self.board[coordinates[0]][coordinates[1]] = 1
    else:
      self.board[coordinates[0]][coordinates[1]] = 2
    self.player1_turn = not self.player1_turn
  
  def regulate_board_size(self, board_size=None):
    if board_size == None:
      board_size = self.board_size
    if board_size > 9:
      self.view.error(UserWarning("Board size cannot exceed 9x9..."))
      return 9
    else:
      return board_size

  def check_identical_values(self, list_to_check):
    number_of_values = len(list_to_check)
    number_of_ones_in_list = 0
    number_of_twos_in_list = 0
    for value in list_to_check:
      if value == 1:
        number_of_ones_in_list += 1
      if value == 2:
        number_of_twos_in_list += 1
    return number_of_ones_in_list == number_of_values or number_of_twos_in_list == number_of_values


  def is_game_complete(self, game_state=None):
    if game_state == None:
      game_state = self
    
    possible_wins_to_check = []
    win_count = 0
    spaces_filled = 0

    for rows in game_state.board:
      possible_wins_to_check.append(rows)
    
    for column in range(len(game_state.board)):
      column_possibility = []
      for lists in game_state.board:
        column_possibility.append(lists[column])
      possible_wins_to_check.append(column_possibility)

    for diagonal_left_to_right in range(2):
      diagonal_possibility = []
      current_position = 0
      for lists in game_state.board:
        diagonal_possibility.append(lists[current_position])
        current_position += 1
      possible_wins_to_check.append(diagonal_possibility)

    for diagonal_right_to_left in range(2):
      diagonal_possibility = []
      current_position = game_state.board_size - 1
      for lists in game_state.board:
        diagonal_possibility.append(lists[current_position])
        current_position -= 1
      possible_wins_to_check.append(diagonal_possibility)

    for cats_game in game_state.board:
      for cats_game_possibility in cats_game:
        if cats_game_possibility == 0:
          continue
        else:
          spaces_filled += 1
    
    if spaces_filled == game_state.board_size * game_state.board_size:
      return True, True
    else:
      for possible_win in possible_wins_to_check:
        if self.check_identical_values(possible_win) == True:
          win_count += 1
      if win_count > 0:
        return True, False
      else:
        return False, False