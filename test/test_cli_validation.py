from game.cli_validation import CLIValidation
from game.state_manager import StateManager

def test_input_too_long():
  cli_valid = CLIValidation()
  text_input = "A11"
  text_input = list(text_input.upper())
  validation_errors = cli_valid.is_too_long(text_input)
  assert validation_errors[0] == str("Input is 1 characters too long...")

def test_input_too_short():
  cli_valid = CLIValidation()
  text_input = "A"
  text_input = list(text_input.upper())
  validation_errors = cli_valid.is_too_short(text_input)
  assert validation_errors[0] == str("Input is 1 characters too short...")

def test_input_invalid_first_character():
  cli_valid = CLIValidation()
  sm = StateManager()
  new_state = sm.create()
  text_input = "D2"
  text_input = list(text_input.upper())
  board_size = new_state.board["size"]
  validation_errors = cli_valid.has_invalid_character_first_position(board_size, text_input)
  assert validation_errors[0] == str("\"D\" is not one of the valid selctions in position 1... (A - C)")

def test_input_invalid_second_character():
  cli_valid = CLIValidation()
  sm = StateManager()
  new_state = sm.create()
  text_input = "A4"
  text_input = list(text_input.upper())
  board_size = new_state.board["size"]
  validation_errors = cli_valid.has_invalid_character_second_position(board_size, text_input)
  assert validation_errors[0] == str("\"4\" is not one of the valid selctions in position 2... (1 - 3)")

def test_validation_multi_error():
  cli_valid = CLIValidation()
  sm = StateManager()
  new_state = sm.create()
  validation_errors = cli_valid.validate_move_text(new_state, "RESPECT")
  assert validation_errors.success == False
  assert validation_errors.errors[0] == str("Input is 5 characters too long...")
  assert validation_errors.errors[1] == str("\"R\" is not one of the valid selctions in position 1... (A - C)")
  assert validation_errors.errors[2] == str("\"E\" is not one of the valid selctions in position 2... (1 - 3)")

def test_validation_big_board_one_off_cases():
  cli_valid = CLIValidation()
  sm = StateManager()
  new_state = sm.create({"board_size": 8})
  validation_errors = cli_valid.validate_move_text(new_state, "I9")
  assert validation_errors.success == False
  assert validation_errors.errors[0] == str("\"I\" is not one of the valid selctions in position 1... (A - H)")
  assert validation_errors.errors[1] == str("\"9\" is not one of the valid selctions in position 2... (1 - 8)")