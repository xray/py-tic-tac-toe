import pytest
from game.user_input import UserInput

def test_validation_too_long():
  new_user_input = UserInput()
  with pytest.raises(UserWarning) as error:
    new_user_input.validate("RESPECT")
    assert error.value == "Input is 5 characters too long..."

def test_validation_too_short():
  new_user_input = UserInput()
  with pytest.raises(UserWarning) as error:
    new_user_input.validate("A")
    assert error.value == "Input is 1 characters too short..."

def test_validation_invalid_first_character():
  new_user_input = UserInput()
  with pytest.raises(UserWarning) as error:
    new_user_input.validate("AB")
    assert error.value == "\"A\" is not one of the valid selctions... (T, M, or B)"

def test_validation_invalid_second_character():
  new_user_input = UserInput()
  with pytest.raises(UserWarning) as error:
    new_user_input.validate("TB")
    assert error.value == "\"A\" is not one of the valid selctions... (L, M, or R)"