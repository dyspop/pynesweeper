import random

# returns a field of mines randomly created with an unrevealed state from a grid.
def make_mines(grid):
  mine_field = []
  for x in range(0, grid[0]):
    mine_strip = []
    for y in range(0, grid[1]):
      # True = "revealed", False = "hidden"
      mine_strip.append([
        # Bomb or not
        random.choice([0,1]),
        # Revealed
        False,
        # Bomb neighbor count placeholder
        0
      ])
    mine_field.append(mine_strip)
  return mine_field

def validate_neighbor(coordinates):
  x = coordinates[0]
  y = coordinates[1]
  try:
    if x >= 0 and y >= 0:
      data = (mine_field[x][y][0],"valid")
    else:
      data = (0,"valid")
  except (IndexError, ValueError):
    data = (0,"invalid")
  return data

def count_neighbors(coordinates):
  x = coordinates[0]
  y = coordinates[1]
  count = 0
  # count around the x y except where there isn't anything
  for a in range(x-1,x+1):
    for b in range(y-1,y+1):
      valid = validate_neighbor([a, b])
      # if valid[0] == 0 and valid[1] == "valid":
        # select_position(x,y)
      count = count + valid[0]
  return count

def spread_select(x, y):
  for a in range(x-1,x+1):
    for b in range(y-1,y+1):
      if mine_field[a][b][0] == 0:
        count_neighbors([a, b])
        select_position(a, b)

def display_field():
  for x, mine_strip in enumerate(mine_field):
    row = []
    for y, position in enumerate(mine_strip):
      if position[1] == True:
        count = count_neighbors([max(0,x), max(0,y)])
        spread_select(x, y)
        row.append(str(count))
      else:
        row.append("*")
    print(row)

def end_game():
  print("BOMB! YOU LOSE")

def validate_selection(input):
  # if selection is a list or is within bounds
  if (type(selection) is list) or (0 < x > grid[0]) or (0 < y > grid[1]):
    print("Valid selection.")
  else:
    print("That's not a valid selection, try again.")
    take_selection(input)

def select_position(x, y):
  if mine_field[x][y][0] == 1:
    end_game()
    exit()
  else:
    mine_field[x][y][1] = True

def take_selection(input):
  var = input("Input the x,y coordinates of the position you'd like to reveal:")
  try:
    selection = list(map(int, var.split(',')))
    x = selection[0]
    y = selection[1]
    select_position(x, y)
  except(ValueError):
    display_field()
  display_field()
  take_selection(input)

grid = (6,6)
mine_field = make_mines(grid)
# test field
# mine_field = [
#   [[1, False, 0], [0, False, 0], [1, False, 0]], 
#   [[0, False, 0], [0, False, 0], [0, False, 0]], 
#   [[0, False, 0], [0, False, 0], [0, False, 0]]
# ]

# uncomment the next line to see the bombs
#print(mine_field)
display_field()

take_selection(input)

