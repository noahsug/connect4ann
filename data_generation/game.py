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

  def getHeuristic(self, player):
    if (player == 1):
      return self.starterHeuristic
    else:
      return self.followerHeuristic

  def setHeuristic(self, heuristic, player):
    if (player == 1):
      self.starterHeuristic = heuristic
    else:
      self.followerHeuristic = heuristic

  def takeTurn(self):
    player = self.getPlayer()
    move = self.getHeuristic(player).getMove(self.currentState, player)
    nextState = self.currentState.makeMove(move, player)
    self.goToNextState(nextState)

  def play(self):
    result = State.UNFINISHED
    while result is State.UNFINISHED:
      self.takeTurn()
      result = self.getHeuristic(self.getPlayer()).getGameResult(self.currentState)
    return (self.pastStates[1:], State.pieceStr(result))
