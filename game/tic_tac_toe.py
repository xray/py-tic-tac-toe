from game.view import View
from game.user_input import UserInput
from game.state import State

DEFAULT_DEPENDENCIES = {
  "view": View(),
  "state": State(),
  "userInput": UserInput()
}

class TicTacToe:
  def __init__(self, injected_dependencies={}):
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies["view"]
    self.state = dependencies["state"]
    self.user_input = dependencies["userInput"]
    self.play()

  def play(self):
    self.state.update_input(self.user_input.prompt())
    if self.state.is_game_complete:
      print("Done")
    else:
      self.play()
