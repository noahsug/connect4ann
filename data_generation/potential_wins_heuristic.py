from score_heuristic import ScoreHeuristic
import math
import board
import random

class PotentialWinsHeuristic(ScoreHeuristic):
  WEIGHTS = [1, 2, 3, 10000]
  POWERS = [1, 2, 3, 1]

  def getScore(self, move):
    score = self.getCompletenessScore(move, self.state.player)
    score -= self.getPieceAboveScore(move)
    return score

  def getPieceAboveScore(self, move):
    (x, y) = move
    if y + 1 >= board.HEIGHT: return 0
    return self.getCompletenessScore((x, y + 1), self.state.player*-1) / 4

  def getCompletenessScore(self, move, player):
    score = 0
    completenessData = self.state.getLineCompleteness(move, player).data
    for (numComplete, numLines) in enumerate(completenessData):
      score += self.WEIGHTS[numComplete] * math.pow(numLines, self.POWERS[numComplete])
    return score

if __name__ == '__main__':
  # TESTS
  from test import *
  from game_state import GameState as State
  state = State()
  heuristic = PotentialWinsHeuristic()
  heuristic.setState(state)

  assertEquals((3, 0), heuristic.getMove())

  state.makeMove((3, 0))
  state.makeMove((3, 1))
  assertEquals((2, 0), heuristic.getMove())

  state.makeMove((3, 2))
  state.makeMove((3, 3))
  state.makeMove((3, 4))
  state.makeMove((3, 5))
  assertEquals((1, 0), heuristic.getMove())

  state.makeMove((1, 0))
  assertEquals((1, 1), heuristic.getMove())
