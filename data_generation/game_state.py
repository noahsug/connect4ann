WIDTH = 7
HEIGHT = 6
INIT_STATE = [ 0 for i in range(WIDTH * HEIGHT + 1) ]

class GameState:
  def __init__(self, board=INIT_STATE):
    self.board = board

  def get(self, x, y):
    return self.board[x * y + y]

  ##
  # @param {int} move A number between 0-6 that represents the column where
  #    the next peice should be placed.
  # @param {int} player The player making the move (either -1 or 1).
  # @return {GameState} The game state after the move has been made.
  ##
  def makeMove(self, move, player):
    board = self.board[:]
    board[move] = player # TODO: this isn't correct!
    return GameState(board)

  def toString(self):
    return self.board
