from game.storage_dat import StorageDat as db

class StateStorage:
  def __init__(self, storage_type=db):
    self.db = db()

  def write_state(self, state):
    self.db.write(state)

  def read_state(self, state_id):
    return self.db.read(state_id)
