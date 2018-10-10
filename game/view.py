class View:
  def __init__(self):
    return
   
  def dynamic_section(self, selections):
    staged = []
    for state in selections:
      if state == 0:
        staged.append(" ")
      elif state == 1:
        staged.append("✕")
      else:
        staged.append("◯")
    return "│ " + staged[0] + " ┃ " + staged[1] + " ┃ " + staged[2] + " │"

  def board(self, board_state):
    board_top =    "╭───┰───┰───╮"
    board_middle = "┝━━━╋━━━╋━━━┥"
    board_bottom = "╰───┸───┸───╯"
    print(board_top)
    print(self.dynamic_section(board_state[0]))
    print(board_middle)
    print(self.dynamic_section(board_state[1]))
    print(board_middle)
    print(self.dynamic_section(board_state[2]))
    print(board_bottom)
    return True

  def error(self, err):
    print("\033[93m" + str(err) + "\033[0m")

  def notify(self, msg):
    print(msg)