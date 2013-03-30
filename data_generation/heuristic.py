from game_state import GameState as State

class Heuristic:
  def __init__(self):
    pass

  def getMove(self, state):
    # TODO: Implement - this is the important part
    return 0

  ##
  # Report the result of a game, or that it is unfinished.
  # @param {State}
  # @return {int}:
  # 2 for unfinished game,
  # 1 for first player victory,
  # -1 for second player victory,
  # 0 for draw
  ##
  def getGameResult(self, state):
    # TODO: Implement - this is the same for all heuristics (they should extend this class)
    #Horizontal victory
    for y in range(State.HEIGHT):
      for x in range(State.WIDTH - 3):
        player = state.get(x, y)
        if (player != 0
            and state.get(x+1, y) == player
            and state.get(x+2, y) == player
            and state.get(x+3, y) == player):
          return player

    #Vertical victory
    for x in range(State.WIDTH):
      for y in range(State.HEIGHT - 3):
        player = state.get(x, y)
        if (player != 0
            and state.get(x, y+1) == player
            and state.get(x, y+2) == player
            and state.get(x, y+3) == player):
          return player

    #Diagonal victories
    for x in range(State.WIDTH - 3):
      for y in range(State.HEIGHT - 3):
        #bottom-left to top-right
        player = state.get(x, y)
        if (player != 0
            and state.get(x+1, y+1) == player
            and state.get(x+2, y+2) == player
            and state.get(x+3, y+3) == player):
          return player

        #Top-left to bottom-right
        player = state.get(x, y+3)
        if (player != 0
            and state.get(x+1, y+2) == player
            and state.get(x+2, y+1) == player
            and state.get(x+3, y) == player):
          return player

    #If neither player has won, check for a draw.
    if (state.get(0, 5) != 0
        and state.get(1, 5) != 0
        and state.get(2, 5) != 0
        and state.get(3, 5) != 0
        and state.get(4, 5) != 0
        and state.get(5, 5) != 0
        and state.get(6, 5) != 0):
      return 0

    # None of the conditions are met - unfinished game.
    return 2
