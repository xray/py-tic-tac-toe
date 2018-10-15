from game.view import View
from game.user_input import UserInput
from game.state import State

DEFAULT_DEPENDENCIES = {
  "view": View(),
  "state": State(),
  "userInput": UserInput()
}

class TicTacToe:
  def __init__(self, injected_dependencies=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies["view"]
    self.state = dependencies["state"]
    self.user_input = dependencies["userInput"]
    self.play()

  def play(self):
    self.view.board(self.state.board)
    if self.state.player1_turn:
      self.view.notify("Player 1, you're up!")
    else:
      self.view.notify("Player 2, it's your turn!")
    self.state.update_input(self.user_input.get_valid_input(self.state))
    self.state.update_board(self.state.user_input)
    if self.state.is_game_complete():
      self.view.board(self.state.board)
      self.view.who_won(self.state.player1_turn)
      self.view.notify("The Game is now over...")
      exit()
    else:
      return self.play()
