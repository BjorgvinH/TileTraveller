#starting by defining the playing field with xy coordinates
# A function will be used to move the player on the playing field
# If the move from the function is valid the move will be performed if invalid an error message will appear

def movement_y (direction):
    y_movement = 0
    if direction =='N':
        y_movement = 1
    elif direction == 'S':
        y_movement = -1
    return(y_movement)

def movement_x(direction):
    x_movement = 0 
    if direction == 'W':
        x_movement = -1
    elif direction == 'E':
        x_movement = 1
    return(x_movement)
    


def travel(x,y):
    N = ''
    S = ''
    W = ''
    E = ''
    if y < 3 and x != 2:
         N='(N)orth'
         return(N)     
    elif y > 1:
        if y == 3 and x ==2:
            E = '(E)ast'
            W = '(W)est'
            return (E,W)
        S = '(S)outh'
        return(S)
    elif x== 2 and y == 2:
        S='(S)outh'
        W='(W)est'
        return (S,W)
    elif x==2 and y == 2:
        N='(N)orth'
        S='(S)outh'
        E='(E)ast' 
        return(N,S,E)   
    



#playing field   
x_axis= 1
y_axis = 1

move = input('Direction:')
change_in_direction = 0 


while y_axis in range (0,4):
    position = travel (x_axis, y_axis)
    print('you can travel:',position)
    move = input('Direction:')
    if move == 'N' or move == 'S':
        change_in_direction = movement_y(move)
        y_axis += change_in_direction
    elif move == 'W' or move == 'E':
        change_in_direction = movement_x(move)
        x_axis += change_in_direction
    if x_axis == 3 and y_axis == 1:
        break

print('Victory!')
    









