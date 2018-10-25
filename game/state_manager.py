import uuid
import datetime
import copy
from game.view import View
from game.state import State
from game.state_repo import StateRepo

class StateManager:
  def __init__(self, state=State, view=View(), state_repo=StateRepo()):
    self.view = view
    self.state = state
    self.state_repo = state_repo

  def create(self, state_configuration=None):
    state_defaults = {
      "board_size": 3,
      "player_count": 2,
      "player_turn": 1
    }
    if state_configuration == None:
      state_configuration = {}
    state_configuration = dict(state_defaults, **state_configuration)
    configured_board = self.board_config(state_configuration.get("board_size", 3), state_configuration.get("board_status"))
    configured_game_id = self.game_id_config(state_configuration.get("game_id"))
    configured_player_ids = self.player_ids_config(player_count=state_configuration.get("player_count", 2))
    configured_player_turn = state_configuration.get("player_turn", 1)
    configured_game_completion = state_configuration.get("game_complete", False)
    configured_history = state_configuration.get("history", [])
    new_state = self.state(dict({
      "game_id": configured_game_id,
      "player_ids": configured_player_ids,
      "player_turn": configured_player_turn,
      "game_complete": configured_game_completion,
      "history": configured_history
    }, **configured_board))
    self.state_repo.write_state(new_state)
    return new_state

  def update(self, state, changes, update_turn=True):
    unchanged_state = copy.deepcopy(state)
    if changes.get("coordinates") != None:
     updated_board = self.update_board(state, changes.get("coordinates"))
    else:
      updated_board = {}
    if update_turn == True:
      if state.player_turn == (state.player_count):
        state.player_turn = 1
      else:
        state.player_turn += 1
      state.history.append(unchanged_state)
    updated_completion = self.is_game_complete(state)
    updated_state = self.state(dict({
      "game_id": state.game_id,
      "player_ids": state.player_ids,
      "player_turn": state.player_turn,
      "game_complete": updated_completion,
      "history": state.history
    }, **updated_board))
    self.state_repo.write_state(updated_state)
    return updated_state


  def update_board(self, state, coordinates):
    current_board = state.board["status"]
    current_board[coordinates[0]][coordinates[1]] = state.player_turn
    return {
      "board": {
        "size": state.board["size"],
        "status": current_board
      }
    }

  def board_config(self, board_size=3, board_status=None):
    regulated_size = self.regulate_board_size(board_size)
    if board_status == None:
      board_status = []
      for length in range(board_size):
        new_section = []
        for width in range(board_size):
          new_section.append(0)
        board_status.append(new_section)
    return {
      "board": {
        "size": board_size,
        "status": board_status
      }
    }

  def game_id_config(self, game_id):
    if game_id == None:
      time = datetime.datetime.now()
      game_id = str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "-" + str(time.hour) + "-" + str(time.minute) + "-" + str(time.second) + "-" + str(time.microsecond)
    return game_id

  def player_ids_config(self, players=None, player_count=2):
    if players == None:
      players = []
      for index in range(player_count):
        players.append(uuid.uuid4())
    return players

  def regulate_board_size(self, board_size=3):
    if board_size > 9:
      self.view.error(UserWarning("Board size cannot exceed 9x9..."))
      return 9
    if board_size < 3:
      self.view.error(UserWarning("Board size cannot be smaller than 3x3"))
      return 3
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
  
  def is_game_complete(self, game_state):    
    possible_wins_to_check = []
    win_count = 0
    spaces_filled = 0

    for rows in game_state.board["status"]:
      possible_wins_to_check.append(self.check_identical_values(rows))
    
    for column in range(len(game_state.board["status"])):
      column_possibility = []
      for lists in game_state.board["status"]:
        column_possibility.append(lists[column])
      possible_wins_to_check.append(self.check_identical_values(column_possibility))

    for diagonal_left_to_right in range(2):
      diagonal_possibility = []
      current_position = 0
      for lists in game_state.board["status"]:
        diagonal_possibility.append(lists[current_position])
        current_position += 1
      possible_wins_to_check.append(self.check_identical_values(diagonal_possibility))

    for diagonal_right_to_left in range(2):
      diagonal_possibility = []
      current_position = game_state.board["size"] - 1
      for lists in game_state.board["status"]:
        diagonal_possibility.append(lists[current_position])
        current_position -= 1
      possible_wins_to_check.append(self.check_identical_values(diagonal_possibility))

    for cats_game in game_state.board["status"]:
      for cats_game_possibility in cats_game:
        if cats_game_possibility != 0:
          spaces_filled += 1
        
    if spaces_filled == game_state.board["size"] * game_state.board["size"]:
      return True, True
    else:
      if any(possible_wins_to_check):
        return True, False
      else:
        return False, False
