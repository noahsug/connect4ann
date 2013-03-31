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
    
  ##
  # Determine whether or not a position can be played (eg whether there is a blank below it, or it is occupied)
  ##
  def validatePos(self, state, x, y):
    if (state.get(x, y) == 0
        and (y == 0 or state.get(x, y-1) != 0)):
      return True
    return False

  ##
  # Get a move that will either immediately result in victory or prevent immediate defeat.
  # return {int} the column to place in, or -1 for no forced moves.
  ##
  def getForcedMove(self, state):
    
    #Horizontal victory block
    for y in range(State.HEIGHT):
      for x in range(State.WIDTH - 3):
        if (self.validatePos(state, x, y)
            and state.get(x+1, y) != 0
            and state.get(x+2, y) == state.get(x+1, y)
            and state.get(x+3, y) == state.get(x+1, y)):
          return x
          
        if (state.get(x, y) != 0
            and self.validatePos(state, x+1, y)
            and state.get(x+2, y) == state.get(x, y)
            and state.get(x+3, y) == state.get(x, y)):
          return (x+1)
          
        if (state.get(x, y) != 0
            and state.get(x+1, y) == state.get(x, y)
            and self.validatePos(state, x+2, y)
            and state.get(x+3, y) == state.get(x, y)):
          return (x+2)
        
        if (state.get(x, y) != 0
            and state.get(x+1, y) == state.get(x, y)
            and state.get(x+2, y) == state.get(x, y)
            and self.validatePos(state, x+3, y)):
          return (x+3)
    
    #Vertical victory block.
    for x in range(State.WIDTH):
      for y in range(State.HEIGHT - 3):
        if (state.get(x, y) != 0
            and state.get(x, y+1) == state.get(x, y)
            and state.get(x, y+2) == state.get(x, y)
            and self.validatePos(state, x, y+3)):
          return x
    
    #Diagonal victories
    for x in range(State.WIDTH - 3):
      for y in range(State.HEIGHT - 3):
        #bottom-left to top-right
        if (self.validatePos(state, x, y)
            and state.get(x+1, y+1) != 0
            and state.get(x+2, y+2) == state.get(x+1, y+1)
            and state.get(x+3, y+3) == state.get(x+1, y+1)):
          return x

        if (state.get(x, y) != 0
            and self.validatePos(state, x+1, y+1)
            and state.get(x+2, y+2) == state.get(x, y)
            and state.get(x+3, y+3) == state.get(x, y)):
          return (x+1)

        if (state.get(x, y) != 0
            and state.get(x+1, y+1) == state.get(x, y)
            and self.validatePos(state, x+2, y+2)
            and state.get(x+3, y+3) == state.get(x, y)):
          return (x+2)

        if (state.get(x, y) != 0
            and state.get(x+1, y+1) == state.get(x, y)
            and state.get(x+2, y+2) == state.get(x, y)
            and self.validatePos(state, x+3, y+3)):
          return (x+3)

        #Top-left to bottom-right
        if (self.validatePos(state, x, y+3)
            and state.get(x+1, y+2) != 0
            and state.get(x+2, y+1) == state.get(x+1, y+2)
            and state.get(x+3, y) == state.get(x+1, y+2)):
          return x
          
        if (state.get(x, y+3) != 0
            and self.validatePos(state, x+1, y+2)
            and state.get(x+2, y+1) == state.get(x, y+3)
            and state.get(x+3, y) == state.get(x, y+3)):
          return (x+1)

        if (state.get(x, y+3) != 0
            and state.get(x+1, y+2) == state.get(x, y+3)
            and self.validatePos(state, x+2, y+1)
            and state.get(x+3, y) == state.get(x, y+3)):
          return (x+2)

        if (state.get(x, y+3) != 0
            and state.get(x+1, y+2) == state.get(x, y+3)
            and state.get(x+2, y+1) == state.get(x, y+3)
            and self.validatePos(state, x+3, y)):
          return (x+3)
    
    return -1
