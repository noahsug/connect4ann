WIDTH = 7
HEIGHT = 6
INIT_STATE = [ 0 for i in range(WIDTH * HEIGHT + 1) ]

class GameState:
  WIDTH = 7
  HEIGHT = 6

  def __init__(self, board=INIT_STATE):
    self.board = board

  def get(self, x, y):
    return self.board[x * HEIGHT + y]

  ##
  # @param {int} move A number between 0-6 that represents the column where
  #    the next piece should be placed.
  # @param {int} player The player making the move (either -1 or 1).
  # @return {GameState} The game state after the move has been made.
  ##
  def makeMove(self, move, player):
    board = self.board[:]
    for i in range(move * HEIGHT, (move+1) * HEIGHT):
      if (board[i] == 0):
        board[i] = player
        break
    else:
      # @TODO: What do we do in case the row is full?
      print "Impossible move"

    return GameState(board)

  def toString(self):
    return self.board
