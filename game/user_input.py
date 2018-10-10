class UserInput:
  def __init__(self):
    return
  
  def prompt(self):
    player_input = input("Make your Selection: ")
    try:
      self.validate(player_input)
      return input()
    except UserWarning as error:
      print("\033[93m" + str(error) + "\033[0m")
      self.prompt()

  def validate(self, player_input):
    player_input = player_input.upper()
    selection = list(player_input)
    required_length = 2
    if len(selection) > required_length:
      raise UserWarning("Input is " + str(len(selection) - 2) + " characters too long...")
    if len(selection) < required_length:
      raise UserWarning("Input is " + str(2 - len(selection)) + " characters too short...")
    if selection[0] != "T" and selection[0] != "M" and selection[0] != "B":
      raise UserWarning("\"" + str(selection[0]) + "\" is not one of the valid selctions... (T, M, or B)")
    if selection[1] != "L" and selection[1] != "M" and selection[1] != "R":
      raise UserWarning("\"" + str(selection[1]) + "\" is not one of the valid selctions... (L, M, or R)")
    return True
  

