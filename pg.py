import os
import pickle
from game.state import State, StateManager

# import datetime
# import json

# indigo = {
#   "shalala": 123456,
#   "bongo": "cat",
#   "multi": ["big", "orange", "scary", "pumpkins"],
#   "dictception": {
#     "magnets": "How do they work?",
#     "life": 42
#   }
# }

# with open(os.path.join(data_folder, "savegame.json")) as json_file:
#   data = json.load(json_file)
#   print(data["multi"])


# time = datetime.datetime.now()
# time_string = str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "-" + str(time.hour) + "-" + str(time.minute) + "-" + str(time.second) + "-" + str(time.microsecond)
# print(time_string)


# for index in range(10):
#   print(index)

# new_boi = {}

# if new_boi.get("list_boi") == None:
#   new_boi["list_boi"] = []
# new_boi["list_boi"].append("memes")

# print(new_boi)

def display_state(yuh):
  print()
  print("Game ID: " + str(yuh.game_id))
  print("Board: " + str(yuh.board))
  print("Player IDs: " + str(yuh.player_ids))
  print("Player Turn: " + str(yuh.player_turn))
  print("Game Complete: " + str(yuh.game_complete))
  print("State History: " + str(yuh.history))
  print()

def write_to_file(data):
  current_dir = os.getcwd()
  data_folder = os.path.join(current_dir, r'pg_data')
  if not os.path.exists(data_folder):
    os.makedirs(data_folder)
  with open(os.path.join(data_folder, str(data.game_id) + ".dat"), "wb") as outfile:  
    pickle.dump(game_state, outfile)
  
def read_file(id):
  current_dir = os.getcwd()
  data_folder = os.path.join(current_dir, r'pg_data')
  with open(os.path.join(data_folder, id + ".dat"), "rb") as save_game:
    sg_obj = pickle.load(save_game)
    return game_state

test_state = StateManager()
game_state = test_state.create()
game_id = game_state.game_id

write_to_file(game_state)

display_state(read_file(game_id))

current_board = read_file(game_id).board
current_board["status"] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
write_to_file(State(previous_state=game_state, changes={"board": current_board}))

updated_state = read_file(game_id)

display_state(updated_state)

print(updated_state.history[0].board)