from game import Game
from random_heuristic import RandomHeuristic

game = Game()
game.setHeuristic(RandomHeuristic())

(states, result) = game.play()

for state in states:
  print state
print 'AND THE WINNER IS', result

