from game.view import View
from game.state_manager import StateManager
from game.in_cli import InCLI
from game.game_input import GameInput
from game.state_repo import StateRepo

DEFAULT_DEPENDENCIES = {
  "View": View(),
  "StateManager": StateManager(),
  "InCLI": InCLI(),
  "GameInput": GameInput(),
  "StateRepo": StateRepo()
}

class TicTacToe:
  def __init__(self, injected_dependencies=None, game_id=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies["View"]
    self.state_manager = dependencies["StateManager"]
    self.user_input = dependencies["InCLI"]
    self.game_input = dependencies.get("GameInput")
    self.state_repo = dependencies.get("StateRepo")
    self.game_id = self.setup_game_id(game_id)

  def play(self, game_id=None):
    if game_id == None:
      game_id = self.game_id
    state = self.state_repo.read_state(game_id)
    self.view.board(state.board["status"])
    current_player = state.player_turn
    self.view.notify("Player " + str(current_player) + ", you're up!")
    user_input = self.validate_input(state, state.player_ids[state.player_turn - 1])
    updated_state = self.state_manager.update(state, {"coordinates": user_input})
    game_complete = self.state_manager.is_game_complete(updated_state)
    if game_complete[0]:
      self.view.board(updated_state.board["status"])
      if game_complete[1]:
        self.view.notify("The game ended in a draw...")
      else:
        self.view.who_won(state)
      self.view.notify("The Game is now over...")
      self.state_repo.delete_state(game_id)
      exit()
    else:
      return self.play(updated_state.game_id)
  
  def setup_game_id(self, game_id=None):
    if game_id == None:
      print("Hello World")
      new_state = self.state_manager.create()
      return new_state.game_id
    else:
      print("other thing")
      return game_id

  def validate_input(self, state, player_id):
    user_in = self.user_input.input_text(state)
    if self.game_input.handle_input(state, player_id, user_in).success:
      return user_in
    else:
      return self.validate_input(state, player_id)