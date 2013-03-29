from game import Game
from heuristic import Heuristic

game = Game()
game.setHeuristic(Heuristic())

print game.play()

