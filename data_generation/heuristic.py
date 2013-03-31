from game_state import GameState as State

class Heuristic:
  def getMove(self, state, player):
    # To be implemented by the inheriting classes.
    return 0

  ##
  # Report the result of a game, or that it is unfinished.
  # @param {GameState} state
  # @return {int} The game result:
  #     2 for unfinished game,
  #     1 for first player victory,
  #     -1 for second player victory,
  #     0 for draw
  ##
  def getGameResult(self, state):
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
    for col in range(State.WIDTH):
      if state.get(col, State.HEIGHT-1) is 0:
        return State.UNFINISHED
    return 0

