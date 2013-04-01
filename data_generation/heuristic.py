import board

class Heuristic:

  def setState(self, state):
    self.state = state

  def getMove(self):
    pass

  ##
  # Report the result of a game, or that it is unfinished.
  # @param {GameState} state
  # @return {int} The game result:
  #     2 for unfinished game,
  #     1 for first player victory,
  #     -1 for second player victory,
  #     0 for draw
  ##
  def getGameResult(self):
    if self.state.getWinner() != None:
      return self.state.getWinner()
    moves = [move for move in self.state.getAvailableMoves()]
    if len(moves) is 0:
      return 0
    return board.UNFINISHED

  ##
  # Get a move that will either immediately result in victory or prevent immediate defeat.
  # return {int} the column to place in, or None for no forced moves.
  ##
  def getForcedMove(self):
    for move in self.state.getAvailableMoves():
      if self.isForced(move):
        return move
    return None

  def isForced(self, move):
    for player in [1, -1]:
      if self.state.getLineCompleteness(move, player).hasWin():
        return True
