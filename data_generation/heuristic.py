class Heuristic:
  def __init__(self):
    pass

  def getMove(self, state):
    # TODO: Implement - this is the important part
    return 0

  def isGameOver(self, state):
    # TODO: Implement - this is the same for all heuristics (they should extend this class)
    return state.get(0, 0) is 1

  ##
  # @return {int} The player who won (either -1 or 1).
  # This should only be called after isGameOver() returned true.
  ##
  def getWinner(self):
    # TODO: Implement - again, the same for all heuristics
    return 0
