from game.main import Main

def test_output():
  new_game = Main()
  assert new_game.game_loop() == True