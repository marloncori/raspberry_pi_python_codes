class Board(list):
    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


class Game(object):
    MARKER_X = "X"
    MARKER_O = "O"
    CTRLS = [
        "left",
        None,
        "right",
        "up",
        None,
        "down",
    ]
    EXIT = "stop"
    START = [2, 2]
    DEFAULT = [["O"] * 5 for _ in range(5)]

    def __init__(self):
        self.flag = True
        self.arena = Board(Game.DEFAULT)
        self.curr_pos = Game.START[:]
        self.prev_pos = Game.START[:]
        self.move_player()

    def move_player(self):
        px, py = self.prev_pos
        cx, cy = self.curr_pos
        if (-1 < cx < 5) and (-1 < cy < 5):
            self.arena[py][px] = Game.MARKER_O
            self.arena[cy][cx] = Game.MARKER_X
        else:
            print("Please enter a proper direction.")
            self.curr_pos = self.prev_pos[:]
            self.move_player()

    def play(self):
        print("You are: \nX")
        while self.flag:
            print(str(self.arena))
            ctrl = input("Move left, right, up, down, or stop? \n >>> Direction: ").lower()
            if ctrl in Game.CTRLS:
                d = Game.CTRLS.index(ctrl)
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[d > 2] += d - (1 if d < 3 else 4)
                self.move_player()
            elif ctrl == Game.EXIT:
                self.flag = False
            else:
                print("Please enter a proper direction.")


if __name__ == '__main__':
    my_game = Game()
    my_game.play()
