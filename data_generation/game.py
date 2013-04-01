from game_state import GameState as State
import board

class Game:
  def __init__(self):
    self.pastStateData = []
    self.currentState = State()

  def reset(self):
    self.currentState.reset()
    self.pastStateData = []

  def makeMove(self, move):
    self.pastStateData.append((self.currentState.toString(), self.currentState.getPlayer()))
    self.currentState.makeMove(move)

  def getHeuristic(self):
    if (self.currentState.getPlayer() == 1):
      return self.starterHeuristic
    else:
      return self.followerHeuristic

  def setHeuristic(self, heuristic, player):
    heuristic.setState(self.currentState)
    if (player == 1):
      self.starterHeuristic = heuristic
    else:
      self.followerHeuristic = heuristic

  def takeTurn(self):
    move = self.getHeuristic().getForcedMove()
    if move is None:
      move = self.getHeuristic().getMove()
    self.makeMove(move)

  def play(self):
    result = board.UNFINISHED
    while result is board.UNFINISHED:
      self.takeTurn()
      result = self.getHeuristic().getGameResult()
    return (self.pastStateData[1:], board.pieceStr(result))
