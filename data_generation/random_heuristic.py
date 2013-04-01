from heuristic import Heuristic
import util

class RandomHeuristic(Heuristic):

  def getMove(self):
    availableMoves = [move for move in self.state.getAvailableMoves()]
    return util.getRandomElement(availableMoves)
