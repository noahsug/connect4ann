class GameState:
  WIDTH = 7
  HEIGHT = 6
  INIT_STATE = [ 0 for i in range(WIDTH * HEIGHT + 1) ]
  UNFINISHED = 2

  def __init__(self, board=INIT_STATE):
    self.board = board

  def get(self, x, y):
    return self.board[x * self.HEIGHT + y]

  def set(self, x, y, value):
    self.board[x * self.HEIGHT + y] = value

  ##
  # @param {int} move A number between 0-6 that represents the column where
  #    the next piece should be placed.
  # @param {int} player The player making the move (either -1 or 1).
  # @return {GameState} The game state after the move has been made.
  ##
  def makeMove(self, move, player):
    for row in range(self.HEIGHT):
      if self.get(move, row) is 0:
        result = GameState(self.board[:])
        result.set(move, row, player)
        return result
    print 'ERROR invalid move!'

  def toString(self):
    result = []
    row = [0 for i in range(self.WIDTH)]
    for y in range(self.HEIGHT-1, 0, -1):
      for x in range(self.WIDTH):
        row[x] = self.get(x, y)
      result.append(' '.join([self.pieceStr(piece) for piece in row]))
    result.append('-' * 2 * self.WIDTH)
    return '\n'.join(result)

  @staticmethod
  def pieceStr(piece):
    if piece is 0: return '-'
    if piece is 1: return 'x'
    if piece is -1: return 'o'
