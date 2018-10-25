from game.user_input import UserInput

def test_validation_too_long():
  new_user_input = UserInput()
  validation_errors = new_user_input.validate_input("A11")
  print(validation_errors)
  assert validation_errors.is_valid == False
  assert validation_errors.errors[0] == str("Input is 1 characters too long...")

def test_validation_too_short():
  new_user_input = UserInput()
  validation_errors = new_user_input.validate_input("A")
  assert validation_errors.is_valid == False
  assert validation_errors.errors[0] == str("Input is 1 characters too short...")

def test_validation_invalid_first_character():
  new_user_input = UserInput()
  validation_errors = new_user_input.validate_input("D2")
  assert validation_errors.is_valid == False
  assert validation_errors.errors[0] == str("\"D\" is not one of the valid selctions in position 1... (A - C)")

def test_validation_invalid_second_character():
  new_user_input = UserInput()
  validation_errors = new_user_input.validate_input("A4")
  assert validation_errors.is_valid == False
  assert validation_errors.errors[0] == str("\"4\" is not one of the valid selctions in position 2... (1 - 3)")

def test_validation_multi_error():
  new_user_input = UserInput()
  validation_errors = new_user_input.validate_input("RESPECT")
  assert validation_errors.is_valid == False
  assert validation_errors.errors[0] == str("Input is 5 characters too long...")
  assert validation_errors.errors[1] == str("\"R\" is not one of the valid selctions in position 1... (A - C)")
  assert validation_errors.errors[2] == str("\"E\" is not one of the valid selctions in position 2... (1 - 3)")

def test_validation_big_board_one_off_cases():
  class State:
    def __init__(self):
      self.board_size = 8
  new_user_input = UserInput({"state": State()})
  validation_errors = new_user_input.validate_input("I9")
  assert validation_errors.is_valid == False
  assert validation_errors.errors[0] == str("\"I\" is not one of the valid selctions in position 1... (A - H)")
  assert validation_errors.errors[1] == str("\"9\" is not one of the valid selctions in position 2... (1 - 8)")

def test_conversion_A_to_0_and_1_to_0():
  new_user_input = UserInput()
  assert new_user_input.convert("A1") == [0, 0]

def test_conversion_I_to_8_and_9_to_8():
  new_user_input = UserInput()
  assert new_user_input.convert("I9") == [8, 8]

def test_conversion_B_to_2_and_R_to_2():
  new_user_input = UserInput()
  assert new_user_input.convert("C4") == [2, 3]

def test_position_validation_valid():
  new_user_input = UserInput()
  class State:
    def __init__(self):
      self.board = [[1, 1, 1], [1, 1, 1], [1, 0, 1]]
  assert new_user_input.validate_position([2, 1], State()) == True

def test_position_validation_invalid():
  new_user_input = UserInput()
  class State:
    def __init__(self):
      self.board = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
  assert new_user_input.validate_position([2, 1], State()) == False
