import board

##
# Quickly looks up lines and how close they are to being a win for a given x
# and y location.
##
class LineLookup:
  def __init__(self):
    self.slotToLines = [[] for i in range(board.WIDTH * board.HEIGHT)]
    self.lines = []
    self.initLines()
    self.winner = None
    self.player = 1

  ##
  # Returns an object that gives information on lines the slot is part
  # of and how close those lines are to a win for a given player, assuming
  # the player plays in the given slot.
  ##
  def getLineCompleteness(self, move, player=None):
    if player is None: player = self.player
    result = [0 for i in range(4)]
    for line in self.getLines(move):
      numPieces = line.getPieceCount(player)
      if numPieces != None:
        result[numPieces] += 1
    return LineCompletenessInfo(result)

  def getLines(self, move):
    return self.slotToLines[board.getIndex(move)]

  def initLines(self):
    # Horizontal
    for y in range(board.HEIGHT):
      for x in range(board.WIDTH - 3):
        line = Line()
        self.lines.append(line)
        for i in range(4):
          self.addLine((x + i, y), line)

    # Vertical
    for x in range(board.WIDTH):
      for y in range(board.HEIGHT - 3):
        line = Line()
        self.lines.append(line)
        for i in range(4):
          self.addLine((x, y + i), line)

    # Diagonal
    for x in range(board.WIDTH - 3):
      for y in range(board.HEIGHT - 3):
        bottomToTopLine = Line()
        topToBottomLine = Line()
        self.lines.append(bottomToTopLine)
        self.lines.append(topToBottomLine)
        for i in range(4):
          self.addLine((x + i, y + i), bottomToTopLine)
          self.addLine((x + i, y + (3-i)), topToBottomLine)

  def reset(self):
    self.winner = None
    self.player = 1
    for line in self.lines:
      line.reset()

  def addLine(self, move, line):
    self.slotToLines[board.getIndex(move)].append(line)

  def makeMove(self, move):
    for line in self.getLines(move):
      line.addPiece(self.player)
      if line.getPieceCount(self.player) is 4:
        self.winner = self.player
    self.player *= -1

class Line:
  def __init__(self):
    self.reset()

  def reset(self):
    self.pieceCount = 0
    self.player = None
    self.winPossible = True

  def addPiece(self, player):
    if not self.winPossible:
      return
    if self.isOppositePlayer(player):
      self.winPossible = False
    else:
      self.pieceCount += 1
      self.player = player

  def isOppositePlayer(self, player):
    return self.player is player * -1

  def getPieceCount(self, player):
    if self.isOppositePlayer(player) or not self.winPossible:
      return None
    return self.pieceCount

class LineCompletenessInfo:
  def __init__(self, data):
    self.data = data

  def hasWin(self):
    return self.data[3] != 0

if __name__ == '__main__':
  # TESTS
  from test import *
  lookup = LineLookup()
  assertEquals(7, lookup.getLineCompleteness((3, 0), 1).data[0])
  assertEquals(3, lookup.getLineCompleteness((0, 0), 1).data[0])

  lookup.makeMove((0, 0))
  assertEquals(6, lookup.getLineCompleteness((3, 0), 1).data[0])
  assertEquals(1, lookup.getLineCompleteness((3, 0), 1).data[1])

  lookup.makeMove((1, 0))
  assertEquals(5, lookup.getLineCompleteness((3, 0), 1).data[0])
  assertEquals(0, lookup.getLineCompleteness((3, 0), 1).data[1])
  assertEquals(5, lookup.getLineCompleteness((3, 0), -1).data[0])
  assertEquals(1, lookup.getLineCompleteness((3, 0), -1).data[1])

  lookup.makeMove((6, 0))
  lookup.makeMove((2, 0))
  assertEquals(False, lookup.getLineCompleteness((4, 0), -1).hasWin())
  lookup.makeMove((6, 1))
  lookup.makeMove((3, 0))
  assertEquals(True, lookup.getLineCompleteness((4, 0), -1).hasWin())
  assertEquals(False, lookup.getLineCompleteness((4, 0), 1).hasWin())
