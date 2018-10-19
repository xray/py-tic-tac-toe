from game.view import View
from game.user_input import UserInput
from game.state import StateManager

DEFAULT_DEPENDENCIES = {
  "View": View(),
  "StateManager": StateManager(),
  "UserInput": UserInput()
}

class TicTacToe:
  def __init__(self, injected_dependencies=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies["View"]
    self.state_manager = dependencies["StateManager"]
    self.user_input = dependencies["UserInput"]
    self.play()

  def play(self):
    self.view.board(self.state_manager.board)
    if self.state_manager.player1_turn:
      self.view.notify("Player 1, you're up!")
    else:
      self.view.notify("Player 2, it's your turn!")
    self.state_manager.update_board(self.user_input.get_valid_input(self.state_manager))
    game_complete = self.state_manager.is_game_complete()
    if game_complete[0]:
      self.view.board(self.state_manager.board)
      if game_complete[1]:
        self.view.notify("The game ended in a draw...")
      else:
        self.view.who_won(self.state_manager.player1_turn)
      self.view.notify("The Game is now over...")
      exit()
    else:
      return self.play()
