import os
import json

class SaveJSON:
  def __init__(self):
    self.working_dir = os.getcwd()
    self.data_folder = os.path.join(self.working_dir, r'data')
    return

  def create_data_folder(self):
    if not os.path.exists(self.data_folder):
      os.makedirs(self.data_folder)
  
  def write_state_to_file(self):
    
