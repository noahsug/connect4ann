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
      data[state] = {'1': 0, '-1': 0, '0': 0}
    if result is player:
      data[state]['1'] += 1
    elif result is 0:
      data[state]['0'] += 1
    else:
      data[state]['-1'] += 1

def outputData():
  for state in data:
    resultInfo = data[state]
    score = resultInfo['1'] - resultInfo['-1']
    total = resultInfo['1'] + resultInfo['-1'] + resultInfo['0']
    print '%s,%g' % (state, float(score) / total)

for i in range(100000):
  (states, result) = game.play()
  recordData(states, result)
  game.reset()

outputData()
