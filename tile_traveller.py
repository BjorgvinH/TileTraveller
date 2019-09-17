#starting by defining the playing field with xy coordinates
# A function will be used to move the player on the playing field
# If the move from the function is valid the move will be performed if invalid an error message will appear

def movement (direction):
    x_movement = 0
    y_movement = 0
    if direction =='N':
        y_movement = 1
    elif direction == 'S':
        y_movement = -1
    elif direction == 'W':
        x_movement = -1
    elif direction == 'E':
        x_movement = 1
    return (x_movement,y_movement)

#playing field   
x_ás= 1
y_ás = 1


direction = input ('You can travel: ')







