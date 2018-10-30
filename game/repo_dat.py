import os
import pickle

class RepoDat:
  def __init__(self):
    current_dir = os.getcwd()
    self.data_folder = os.path.join(current_dir, r'data')
    if not os.path.exists(self.data_folder):
      os.makedirs(self.data_folder)
  
  def write(self, state):
    game_id = state.game_id
    with open(os.path.join(self.data_folder, str(game_id) + ".dat"), "wb") as outfile:  
      pickle.dump(state, outfile)

  def read(self, game_id):
    with open(os.path.join(self.data_folder, game_id + ".dat"), "rb") as save_game:
      sg_obj = pickle.load(save_game)
      return sg_obj
  
  def delete(self, game_id):
    try:
      os.remove(os.path.join(self.data_folder, game_id + ".dat"))
      return True
    except:
      return False