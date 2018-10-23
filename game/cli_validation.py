from game.validation_result import ValidationResult

class CLIValidation:
  def __init__(self, validation_result=ValidationResult):
    self.validation_result = validation_result

  def validate_move_text(self, text_input, state):
    board_size = state.board["size"]
    text_input = text_input.upper()
    selection = list(text_input)
    required_length = 2
    validation_errors = []
    if len(selection) > required_length:
      validation_errors.append("Input is " + str(len(selection) - 2) + " characters too long...")
    if len(selection) < required_length:
      validation_errors.append("Input is " + str(2 - len(selection)) + " characters too short...")
    if len(selection) > 0:
      if ord(selection[0].upper()) < 65 or ord(selection[0].upper()) > (64 + board_size):
        key_cap = chr(65 + (board_size - 1))
        validation_errors.append("\"" + str(selection[0]) + "\" is not one of the valid selctions in position 1... (A - " + key_cap + ")")
    if len(selection) > 1:
      if ord(selection[1].upper()) < 49 or ord(selection[1].upper()) > (48 + board_size):
        key_cap = chr(48 + board_size)
        validation_errors.append("\"" + str(selection[1]) + "\" is not one of the valid selctions in position 2... (1 - " + key_cap + ")")
    if len(validation_errors) > 0:
      return ValidationResult(False, validation_errors)
    else:
      return ValidationResult(True, [])
