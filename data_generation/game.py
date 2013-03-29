from game_state import GameState as State

class Game:
  def __init__(self):
    self.pastStates = []
    self.currentState = State()

  def goToNextState(self, state):
    self.pastStates.append(self.currentState.toString())
    self.currentState = state

  ##
  # @return {int} The player whose turn it is (either -1 or 1).
  ##
  def getPlayer(self):
    return ((len(self.pastStates) + 1) % 2) * 2 - 1

  def setHeuristic(self, heuristic):
    self.heuristic = heuristic

  def takeTurn(self):
    move = self.heuristic.getMove(self.currentState)
    nextState = self.currentState.makeMove(move, self.getPlayer())
    self.goToNextState(nextState)

  def play(self):
    while not self.heuristic.isGameOver(self.currentState):
      self.takeTurn()
    winner = self.heuristic.getWinner()
    return (self.pastStates[1:], winner)
