class State:
  def __init__(self):
    self.is_game_complete = False
    self.user_input = None
  
  def update_input(self, player_input):
    self.user_input = player_input

