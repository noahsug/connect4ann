from game import Game
from multi_heuristic import MultiHeuristic
from random_heuristic import RandomHeuristic
from potential_wins_heuristic import PotentialWinsHeuristic
import board

game = Game()
h1 = MultiHeuristic(PotentialWinsHeuristic(), RandomHeuristic())
h2 = MultiHeuristic(PotentialWinsHeuristic(), RandomHeuristic())
game.setHeuristic(h1, 1)
game.setHeuristic(h2, -1)

data = {}

def printGame():
  for state in states[:]:
    print state
  print game.currentState.toString()

  if (result == '-'):
    print "GAME ENDED IN DRAW"
  else:
    print 'AND THE WINNER IS', result

def recordData(states, result):
  for (state, player) in states:
    if not (state in data):
      data[state] = {'x': 0, 'o': 0, '-': 0, 'player': player}
    data[state][result] += 1

def outputData():
  for state in data:
    resultInfo = data[state]
    player = board.pieceStr(resultInfo['player'])
    oppositePlayer = board.pieceStr(resultInfo['player'] * -1)
    score = resultInfo[oppositePlayer] - resultInfo[player]
    total = resultInfo['x'] + resultInfo['o'] + resultInfo['-']
    print '%s,%g' % (state, float(score) / total)

for i in range(100000):
  (states, result) = game.play()
  recordData(states, result)
  game.reset()

outputData()
