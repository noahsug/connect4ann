from game_state import GameState as State
from heuristic import Heuristic
import random

class PotentialLinesHeuristic(Heuristic):

  def getMove(self, state, player):
    maxLines = 0
    maxMoves = []
    for move in range(State.WIDTH):
      if state.get(move, State.HEIGHT-1) is 0:
        potentialState = state.makeMove(move, player)
        lines = self.countLines(potentialState, player)

        if (lines > maxLines):
          maxLines = lines
          del maxMoves[:]
          maxMoves.append(move)
        elif (lines == maxLines):
          maxMoves.append(move)

    random.shuffle(maxMoves)
    return maxMoves[0]
        
        
        
    print 'ERROR', 'PotentialLinesHeuristic.getMove() called but no valid moves available'

  ##
  # Counts the number of lines that have at least 1 of my pieces and are not blocked by opponent's pieces.
  # @param state the state (not necessarily current) to be counted.
  # @param {int} player the current player. 
  # @return {int} number of potential lines.
  ##
  def countLines(self, state, player):
    lines = 0
    oppositePlayer = -1 * player
    #Horizontal
    for y in range(State.HEIGHT):
      for x in range(State.WIDTH - 3):
        if ((state.get(x, y) == player
          or state.get(x+1, y) == player
          or state.get(x+2, y) == player
          or state.get(x+3, y) == player)
          and (state.get(x, y) != oppositePlayer
          and state.get(x+1, y) != oppositePlayer
          and state.get(x+2, y) != oppositePlayer
          and state.get(x+3, y) != oppositePlayer)):
          lines += 1

    #Vertical
    for x in range(State.WIDTH):
      for y in range(State.HEIGHT - 3):
        if ((state.get(x, y) == player
          or state.get(x, y+1) == player
          or state.get(x, y+2) == player
          or state.get(x, y+3) == player)
          and (state.get(x, y) != oppositePlayer
          and state.get(x, y+1) != oppositePlayer
          and state.get(x, y+2) != oppositePlayer
          and state.get(x, y+3) != oppositePlayer)):
          lines += 1

    #Diagonal
    for x in range(State.WIDTH - 3):
      for y in range(State.HEIGHT - 3):
        #bottom-left to top-right
        if ((state.get(x, y) == player
          or state.get(x+1, y+1) == player
          or state.get(x+2, y+2) == player
          or state.get(x+3, y+3) == player)
          and (state.get(x, y) != oppositePlayer
          and state.get(x+1, y+1) != oppositePlayer
          and state.get(x+2, y+2) != oppositePlayer
          and state.get(x+3, y+3) != oppositePlayer)):
          lines += 1

        #Top-left to bottom-right
        if ((state.get(x, y+3) == player
          or state.get(x+1, y+2) == player
          or state.get(x+2, y+1) == player
          or state.get(x+3, y) == player)
          and(state.get(x, y+3) != oppositePlayer
          and state.get(x+1, y+2) != oppositePlayer
          and state.get(x+2, y+1) != oppositePlayer
          and state.get(x+3, y) != oppositePlayer)):
          lines += 1

    return lines
