class View:
  def __init__(self):
    return
   
  def dynamic_section(self, selections):
    final_string = ""
    staged = []
    for state in selections:
      if state == 0:
        staged.append(" ")
      elif state == 1:
        staged.append("✕")
      else:
        staged.append("◯")
    final_string = final_string + "│ "
    for index, spaces in enumerate(selections):
      if index == (len(selections) - 1):
        final_string += staged[index]
      else:
        final_string += staged[index] + " ┃ "
    final_string += " │"
    return final_string

  def board(self, board_state):
    board_top_left =    "╭───┰"
    board_top_middle = "───┰"
    board_top_right = "───╮"
    board_left = "┝━━━╋"
    board_main = "━━━╋"
    board_right = "━━━┥"
    board_bottom_left = "╰───┸"
    board_bottom_middle = "───┸"
    board_bottom_right = "───╯"

    grid_size = len(board_state)
    print("    ", end="", flush=True)
    for space_number in range(grid_size):
      label_number = space_number + 1
      if label_number == grid_size:
        print(" " + str(label_number) + "  ")
      else:
        print(" " + str(label_number) + "  ", end="", flush=True)
    self.paint_board_caps(grid_size, board_top_left, board_top_middle, board_top_right)
    for index, sections in enumerate(board_state):
      coresponding_letter = chr(index + 65)
      print(" " + coresponding_letter + " ", end="", flush=True)
      print(self.dynamic_section(sections))
      if index < (grid_size - 1):
        print("   " + board_left, end="", flush=True)
        for spaces in range(grid_size - 2):
          print(board_main, end="", flush=True)
        print(board_right)

    self.paint_board_caps(grid_size, board_bottom_left, board_bottom_middle, board_bottom_right)
    return True

  def paint_board_caps(self, grid_size, left_piece, middle_piece, right_piece):
    print("   " + left_piece, end="", flush=True)
    for spaces in range(grid_size - 2):
      print(middle_piece, end="", flush=True)
    print(right_piece)

  def error(self, err):
    print("\033[93m" + str(err) + "\033[0m")

  def notify(self, msg):
    print(msg)
  
  def who_won(self, player_one_turn):
    if player_one_turn == True:
      print("Player 2 Wins!")
    else:
      print("Player 1 Wins!")