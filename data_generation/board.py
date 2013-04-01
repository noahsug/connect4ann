WIDTH = 7
HEIGHT = 6
UNFINISHED = 2
INVALID_MOVE = -1

def getIndex(move):
  (x, y) = move
  return x * HEIGHT + y

def pieceStr(piece):
  if piece is 0: return '-'
  if piece is 1: return 'x'
  if piece is -1: return 'o'
