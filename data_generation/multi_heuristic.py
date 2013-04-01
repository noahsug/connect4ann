from heuristic import Heuristic
import util

class MultiHeuristic(Heuristic):

  def __init__(self, h1, h2):
    self.heuristics = [h1, h2]

  def getMove(self):
    heuristic = util.getRandomElement(self.heuristics)
    return heuristic.getMove()

  def setState(self, state):
    self.state = state
    for heuristic in self.heuristics:
      heuristic.setState(state)
