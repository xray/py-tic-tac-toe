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
    self.is_game_complete = False
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