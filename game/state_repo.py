from game.repo_dat import RepoDat as db

class StateRepo:
  def __init__(self, storage_type=db):
    self.db = db()

  def write_state(self, state):
    self.db.write(state)

  def read_state(self, state_id):
    return self.db.read(state_id)
