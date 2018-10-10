from game.view import View

def test_dynamic_section():
  new_view = View()
  options = [0, 1, 2]
  assert new_view.dynamic_section(options) == "│   ┃ ✕ ┃ ◯ │"