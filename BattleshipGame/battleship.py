# Puts a ship on the board, taking in an array, x pos, starting y pos,
# a ship length to determain the stoping location for the ship,
# and a ship value used to show the ship on the matrix
def place_ship(a, x, ys, sl, s):
    for i in range(sl):
        a[x][ys] = s
        ys += 1
# Place a player on the board, don't need it anymore
# Takes in array, x, and y pos, and p for showing the player as a value on the matrix
def place_player(a, x, y, p):
    a[x][y] = p

# Used to move the player, not needed for that anymore
# Moves to the right through the array
def move_player_right(a, x, y, p):
    a[x][y] = 0
    y = y + 1
    a[x][y] = p
    return [x, y]

# Same as move player right, except we traverse down instead of right
def move_player_down(a, x, y, p):
    a[x][y] = 0
    x = x + 1
    a[x][y] = p
    return [x, y]

# Draws the map by taking in an array and printing the value for each item in that array
def print_map(a):
    for i in a:
        print(i)
    print()
# Main game loop    
def main():
    a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    player_location = [0,0, 1]
    ship_three = [3, 2, 3, 2]
    place_ship(a, ship_three[0], ship_three[1], ship_three[2], ship_three[3])
    print_map(a)
    place_player(a, player_location[0], player_location[1], player_location[2])
    print_map(a)
    player_location[0:2] = move_player_right(a, player_location[0], player_location[1], player_location[2])
    print_map(a)
    player_location[0:2] = move_player_right(a, player_location[0], player_location[1], player_location[2])
    print_map(a)
    player_location[0:2] = move_player_down(a, player_location[0], player_location[1], player_location[2])
    print_map(a)
    

main()
