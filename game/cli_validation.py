from game.validation_result import ValidationResult

class CLIValidation:
  def __init__(self, validation_result=ValidationResult):
    self.validation_result = validation_result

  def validate_move_text(self, state, text_input):
    board_size = state.board["size"]
    text_input = list(text_input.upper())
    validation_errors = self.is_too_long(text_input, [])
    validation_errors = self.is_too_short(text_input, validation_errors)
    validation_errors = self.has_invalid_character_first_position(board_size, text_input, validation_errors)
    validation_errors = self.has_invalid_character_second_position(board_size, text_input, validation_errors)
    
    if len(validation_errors) > 0:
      return ValidationResult(False, validation_errors)
    else:
      return ValidationResult(True, [])
  
  def is_too_long(self, input_list, err_list=[], required_length=2):
    if len(input_list) > required_length:
      err_list.append("Input is " + str(len(input_list) - 2) + " characters too long...")
    return err_list
  
  def is_too_short(self, input_list, err_list=[], required_length=2):
    if len(input_list) < required_length:
      err_list.append("Input is " + str(2 - len(input_list)) + " characters too short...")
    return err_list

  def has_invalid_character_first_position(self, board_size, input_list, err_list=[]):
    if len(input_list) > 0:
      if ord(input_list[0].upper()) < 65 or ord(input_list[0].upper()) > (64 + board_size):
        key_cap = chr(65 + (board_size - 1))
        err_list.append("\"" + str(input_list[0]) + "\" is not one of the valid selctions in position 1... (A - " + key_cap + ")")
    return err_list
  
  def has_invalid_character_second_position(self, board_size, input_list, err_list=[]):
    if len(input_list) > 1:
      if ord(input_list[1].upper()) < 49 or ord(input_list[1].upper()) > (48 + board_size):
        key_cap = chr(48 + board_size)
        err_list.append("\"" + str(input_list[1]) + "\" is not one of the valid selctions in position 2... (1 - " + key_cap + ")")
    return err_list