import board
from line_lookup import LineLookup

class GameState:
  INIT_STATE = [ 0 for i in range(board.WIDTH * board.HEIGHT) ]

  def __init__(self, board=INIT_STATE[:]):
    self.board = board
    self.lineLookup = LineLookup()
    self.player = 1

  def reset(self):
    self.lineLookup.reset()
    self.player = 1
    self.board = self.INIT_STATE[:]

  def get(self, move):
    return self.board[board.getIndex(move)]

  def set(self, move, value):
    self.board[board.getIndex(move)] = value

  def getPlayer(self):
    return self.player

  def getWinner(self):
    return self.lineLookup.winner

  def getLineCompleteness(self, move, player=None):
    return self.lineLookup.getLineCompleteness(move, player)

  ##
  # @param {int} col A number between 0-6 that represents the column where
  #    the next piece should be placed.
  ##
  def getMoveForColumn(self, x):
    for y in range(board.HEIGHT):
      if self.get((x, y)) is 0:
        return (x, y)
    return board.INVALID_MOVE

  def getAvailableMoves(self):
    for x in range(board.WIDTH):
      move = self.getMoveForColumn(x)
      if move != board.INVALID_MOVE:
        yield move

  ##
  # @return {GameState} The game state after the move has been made.
  ##
  def makeMove(self, move):
    self.set(move, self.player)
    self.lineLookup.makeMove(move)
    self.player *= -1

  def toString(self):
    return ','.join([str(i) for i in self.board])

  def toReadableString(self):
    result = []
    row = [0 for i in range(board.WIDTH)]
    for y in range(board.HEIGHT-1, -1, -1):
      for x in range(board.WIDTH):
        row[x] = self.get((x, y))
      result.append(' '.join([self.pieceStr(piece) for piece in row]))
    result.append('-' * 2 * board.WIDTH)
    return '\n'.join(result)

  @staticmethod
  def pieceStr(piece):
    if piece is 0: return '-'
    if piece is 1: return 'x'
    if piece is -1: return 'o'
