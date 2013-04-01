from heuristic import Heuristic

class ScoreHeuristic(Heuristic):

  def getMove(self):
    bestScore = bestMove = None
    for move in self.state.getAvailableMoves():
      score = self.getScore(move)
      if bestScore is None or score > bestScore:
        bestScore = score
        bestMove = move
    return bestMove

  def getScore(self, move):
    return 0
