
def adorn():
    print("#" * 30)
    sleep(0.2)
    print("  C H E S S    M O T I O N    A N A L Y S E R")
    sleep(0.2)
    print("#" * 30)
    sleep(0.2)
    
def get_coordinates():
    adorn()
    print("\n\t Welcome to the Chess analyser!")
    sleep(0.5)
    print("\t Please enter coordinates of current")
    sleep(0.5)
    print("\t  square where the Queen is standing now.)
    print("\n\t   [ ENTER A VALUE FROM 1 TO 8 ]
    sleep(0.5)
    x_1 = int(input("\t\t >>> column: "))
    current_square.append(x_1)
    y_1 = int(input("\t\t >>> row: "))
    current_square.append(y_1)
          
    print("\n\t Now tell the coordinates of the square")
    sleep(0.5)
    print("\t where you\'d like to move the Queen.)
    sleep(0.5)
    print("\t    [ ENTER A VALUE FROM 1 TO 8 ]")
    x_2 = int(input("\t\t >>> column: "))
    sleep(0.5)
    next_square.append(x_2)
    y_2 = int(input("\t\t >>> row: "))
    sleep(0.5)
    next_square.append(y_2)
    print("\n\t\t Processing the data...")
    sleep(0.5)
    return current_square, next_square

def can_move(square_1, square_2):
    col_1, row_1 = square_1
    col_2, row_2 = square_2
    if col_1 == col_2 or row_1 == row_2 or abs(col_1 - col_2) == abs(row_1 - row_2):
        msg = "YES!"
    else:
        msg = "NO..."
    return msg

def queen_motion(info):
    print("   -------------------------------------")
    print("   | Can the Queen move?  " + info + " |")
    print("   -------------------------------------")

def start_app():


if __name__ == '__main__':
    try:

    except (KeyboardInterrupt, SystemExit):
        print(" Use has stopped program execution. Goodbye!")
        
    
