from game_state import GameState as State
from heuristic import Heuristic
import random

class RandomHeuristic(Heuristic):

  def getMove(self, state, player):
    availableMoves = range(State.WIDTH)
    random.shuffle(availableMoves)
    for move in availableMoves:
      if state.get(move, State.HEIGHT-1) is 0:
        return move
    print 'ERROR', 'RandomHeuristic.getMove() called but no valid moves available'
