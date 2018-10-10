from game.view import View

class Main:
  def __init__ (self, injected_dependencies={}):
    default_dependencies = {"view": View}
    dependencies = dict(default_dependencies, **injected_dependencies)
    self.view = dependencies["view"]()

  def game_loop (self):
    board_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return self.view.board(board_state)
