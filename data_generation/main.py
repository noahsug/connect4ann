from game import Game
from random_heuristic import RandomHeuristic
from potential_lines_heuristic import PotentialLinesHeuristic

game = Game()
game.setHeuristic(RandomHeuristic(), 1)
game.setHeuristic(PotentialLinesHeuristic(), -1)

(states, result) = game.play()

for state in states:
  print state
print game.currentState.toString()
print 'AND THE WINNER IS', result

