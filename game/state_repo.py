from game.repo_dat import RepoDat as db

class StateRepo:
  def __init__(self, storage_type=db):
    self.db = db()

  def write_state(self, state):
    self.db.write(state)

  def read_state(self, game_id):
    return self.db.read(game_id)
  
  def delete_state(self, game_id):
    return self.db.delete(game_id)
