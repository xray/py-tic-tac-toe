class State:
  def __init__(self):
    self.is_game_complete = False
    self.user_input = []
    self.player1_turn = True
    self.board = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
  
  def update_input(self, player_input):
    self.user_input = player_input
  
  def update_board(self, coordinates):
    if self.player1_turn == True:
      self.board[coordinates[0]][coordinates[1]] = 1
    else:
      self.board[coordinates[0]][coordinates[1]] = 2
    self.player1_turn = not self.player1_turn