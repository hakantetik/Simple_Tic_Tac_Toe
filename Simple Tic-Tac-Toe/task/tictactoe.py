# write your code here
import string

s = "_________"
line = 9 * "-"

x_signature = "XXX"
o_signature = "OOO"


def dashboard(dash):
    print(f"""
    {line}
    | {dash[0]} {dash[1]} {dash[2]} |
    | {dash[3]} {dash[4]} {dash[5]} |
    | {dash[6]} {dash[7]} {dash[8]} |
    {line}
    """)


dashboard(s)

coordinates_valid = True

while coordinates_valid:

    # checks if ends or not
    def check_if_end(x_wins, o_wins):
        global s
        horizontals = [s[0] + s[1] + s[2], s[3] + s[4] + s[5], s[6] + s[7] + s[8]]
        verticals = [s[0] + s[3] + s[6], s[1] + s[4] + s[7], s[2] + s[5] + s[8]]
        diagonals = [s[0] + s[4] + s[8], s[2] + s[4] + s[6]]
        if (x_wins in horizontals) or (x_wins in verticals) or (x_wins in diagonals):
            print("X wins")
            if o_wins in horizontals or o_wins in verticals or o_wins in diagonals:
                print("Impossible")
            return True
        elif o_wins in horizontals or o_wins in verticals or o_wins in diagonals:
            print("O wins")
            return True
        elif "_" not in s and abs(s.count("X") - s.count("O") < 2):
            print("Draw")
            return True
        elif abs(s.count("X") - s.count("O")) >= 2:
            print("Impossible")


    coordinates = input("Make a move")
    dash_coordinates = {
        (1, 1): 0,
        (1, 2): 1,
        (1, 3): 2,
        (2, 1): 3,
        (2, 2): 4,
        (2, 3): 5,
        (3, 1): 6,
        (3, 2): 7,
        (3, 3): 8
    }

    # splitting for x and y koordinates
    x_coordinate = coordinates.split()[0]
    y_coordinate = coordinates.split()[1]

    # X user coordinate tuple
    position = tuple
    if (x_coordinate not in string.digits) or (y_coordinate not in string.digits):
        print("You should enter numbers!")
        continue
    elif (int(x_coordinate) == 0 or int(x_coordinate) > 3) or (int(y_coordinate) == 0 or int(y_coordinate) > 3):
        print("Coordinates should be from 1 to 3!")
        continue
    elif s[dash_coordinates[int(x_coordinate), int(y_coordinate)]] != "_":
        print("This cell is occupied! Choose another")
        continue
    else:
        position = (int(x_coordinate), int(y_coordinate))
        s_list = list(s)
        s_list[dash_coordinates[position]] = "X"
        s = "".join(s_list)
        dashboard(s)
        if check_if_end(x_signature, o_signature):
            break
        else:
            pass

    # computers move
    computers_move = input()
    xc_coordinate = computers_move.split()[0]
    yc_coordinate = computers_move.split()[1]
    position_c = (int(xc_coordinate), int(yc_coordinate))
    s_list_c = list(s)
    s_list_c[dash_coordinates[position_c]] = "O"
    s = "".join(s_list_c)
    dashboard(s)
    if check_if_end(x_signature, o_signature):
        break
    else:
        pass
