from game.in_cli import InCLI

def test_conversion_A_to_0_and_1_to_0():
  in_cli = InCLI()
  assert in_cli.convert_input("A1") == [0, 0]

def test_conversion_I_to_8_and_9_to_8():
  in_cli = InCLI()
  assert in_cli.convert_input("I9") == [8, 8]

def test_conversion_C_to_2_and_4_to_3():
  in_cli = InCLI()
  assert in_cli.convert_input("C4") == [2, 3]
