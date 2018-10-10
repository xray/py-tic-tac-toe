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

def test_conversion_T_to_0_and_L_to_0():
  new_user_input = UserInput()
  assert new_user_input.convert("TL") == [0, 0]

def test_conversion_M_to_1_and_M_to_1():
  new_user_input = UserInput()
  assert new_user_input.convert("MM") == [1, 1]

def test_conversion_B_to_2_and_R_to_2():
  new_user_input = UserInput()
  assert new_user_input.convert("BR") == [2, 2]
