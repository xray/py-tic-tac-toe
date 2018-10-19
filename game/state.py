import uuid
import datetime
from game.view import View

DEFAULT_DEPENDENCIES = {
  "view": View()
}

class State:
  def __init__(self, previous_state=None, changes=None):
    if changes == None:
      changes = {}
    if previous_state != None:
      state_options = {
        "game_id": previous_state.game_id,
        "board": previous_state.board,
        "player_count": previous_state.player_count,
        "player_ids": previous_state.player_ids,
        "players_turns": previous_state.player_turn,
        "game_complete": False,
        "history": previous_state.history
      }
    else:
      state_options = {}

    state_config = dict(state_options, **changes)
    
    self.game_id = self.set_up_game_id(state_config.get("game_id"))
    self.board = self.set_up_board(state_config.get("board"))
    self.player_ids = self.set_up_player_ids(players=state_config.get("player_ids"), player_count=state_config.get("player_count", 2))
    self.player_count = state_options.get("player_count", 2)
    self.player_turn = self.set_up_player_turn(state_config.get("players_turns"))
    self.game_complete = state_config.get("game_complete", False)
    self.history = self.set_up_history(previous_state=previous_state, history=state_config.get("history"))

  def retrieve(self):
    return self

  def set_up_game_id(self, game_id=None):
    if game_id == None:
      time = datetime.datetime.now()
      game_id = str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "-" + str(time.hour) + "-" + str(time.minute) + "-" + str(time.second) + "-" + str(time.microsecond)
    return game_id
  
  def set_up_board(self, board=None):
    if board == None or board.get("status") == None:
      if board == None:
        board = {}
      for length in range(board.get("size", 3)):
        new_section = []
        for width in range(board.get("size", 3)):
          new_section.append(0)
        if board.get("status") == None:
          board["status"] = []
        board["status"].append(new_section)
    return board

  def set_up_player_ids(self, players=None, player_count=2):
    if players == None:
      players = []
      for index in range(player_count):
        players.append(uuid.uuid4())
    return players

  def set_up_player_turn(self, turn=None):
    if turn == None:
      return 1
    else:
      return turn + 1
  
  def set_up_history(self, previous_state=None, history=None):
    if previous_state == None:
      return []
    else:
      history.append(previous_state)
      return history

class StateManager:
  def __init__(self, board_size=3, number_of_players=2, injected_dependencies=None):
    if injected_dependencies == None:
      injected_dependencies = {}
    dependencies = dict(DEFAULT_DEPENDENCIES, **injected_dependencies)
    self.view = dependencies.get("view")

  def create(self, board_size=3, number_of_players=2):
    new_game = State(changes={
      "board": {
        "size": self.regulate_board_size(board_size)
        },
      "player_count": number_of_players
    })
    return new_game

  def update_board(self, state, coordinates):
    current_board = state.board["status"]
    for index, player in enumerate(len(state.player_ids)):
      if ((index + 1) % state.player_turn) == 0:
        current_board[coordinates[0]][coordinates[1]] = (index + 1)
    return State(state, {"board": current_board})
  
  def regulate_board_size(self, board_size):
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
