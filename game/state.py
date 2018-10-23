class State:
  def __init__(self, details):
    self.game_id = details.get("game_id")
    self.board = details.get("board")
    self.player_ids = details.get("player_ids")
    self.player_count = len(details.get("player_ids"))
    self.player_turn = details.get("player_turn")
    self.game_complete = details.get("game_complete")
    self.history = details.get("history")