class ValidationResult:
  def __init__(self, result, errors):
    self.success = result
    self.errors = errors
