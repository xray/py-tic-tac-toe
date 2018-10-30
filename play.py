import sys
from game.tic_tac_toe import TicTacToe

try:
  if len(sys.argv) < 2:
    game_id = None
  else:
    game_id = sys.argv[1]
  ttt = TicTacToe(game_id=game_id)
  ttt.play()
except KeyboardInterrupt:
  print("\n")
  print("To pickup where you left off enter the code below as an argument the next time you launch the game...")
  print("Command example: python play.py [Game Code]")
  print("Game Code: " + ttt.game_id)
