from game.validation_result import ValidationResult

class CLIValidation:
  def validate_move_text(self, state, text_input):
    board_size = state.board["size"]
    text_input = list(text_input.upper())

    errors = []

    for validator in [self.is_too_long, self.is_too_short, self.has_invalid_character_first_position, self.has_invalid_character_second_position]:
      errors += validator(board_size, text_input)
    
    return ValidationResult(len(errors) == 0, errors)
    
  def is_too_long(self, board_size, input_list):
    if len(input_list) > 2:
      return ["Input is " + str(len(input_list) - 2) + " characters too long..."]
    
    return []
  
  def is_too_short(self, board_size, input_list):
    if len(input_list) < 2:
      return ["Input is " + str(2 - len(input_list)) + " characters too short..."]
    
    return []

  def has_invalid_character_first_position(self, board_size, input_list):
    if len(input_list) > 0:
      if ord(input_list[0].upper()) < 65 or ord(input_list[0].upper()) > (64 + board_size):
        key_cap = chr(65 + (board_size - 1))
        return ["\"" + str(input_list[0]) + "\" is not one of the valid selctions in position 1... (A - " + key_cap + ")"]
    
    return []
  
  def has_invalid_character_second_position(self, board_size, input_list):
    if len(input_list) > 1:
      if ord(input_list[1].upper()) < 49 or ord(input_list[1].upper()) > (48 + board_size):
        key_cap = chr(48 + board_size)
        return ["\"" + str(input_list[1]) + "\" is not one of the valid selctions in position 2... (1 - " + key_cap + ")"]
    
    return []
