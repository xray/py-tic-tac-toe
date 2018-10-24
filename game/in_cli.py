from game.cli_validation import CLIValidation

class InCLI:
  def __init__(self, cli_validation=CLIValidation()):
    self.cli_validation = cli_validation
  
  def input_text(self, state):
    player_input = input("Make a move: ")
    if self.cli_validation.validate_move_text(state, player_input).success:
      return self.convert_input(player_input)
    else:
      return self.input_text

  def convert_input(self, validated_input):
    player_input = validated_input.upper()
    conversion = []
    conversion.append(ord(player_input[0].lower())-97)
    conversion.append(int(player_input[1]) - 1)
    return conversion
