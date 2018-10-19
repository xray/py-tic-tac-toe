from game.view import View

class Question:
  def __init__(self, query, default_response=True):
    self.text = query
    self.default_response = default_response

class Choice:
  def __init__(self, view=View()):
    self.view = view

  def create(self, query, default_response=True):
    return self.pose(Question(query, default_response))
  
  def pose(self, question):
    

    return True