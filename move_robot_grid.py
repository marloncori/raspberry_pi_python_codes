class robot:
    def __init__ (self, name, grid, position):
        self.name = name
        self.position = position
        self.grid = grid

    def robot_position(self, position):
        position = [x,y]
        return robot.position

    def robot_neighbours(self, position):
        position = [x,y]
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        return results

    def move_north(self):
        north = [x,y+1]
        robot.robot_position = north
        return robot.robot_position


class game_board:
    def __init__(self, width, height): 
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.name = " . "
        self.walls = []
        self.traps = []
        
    def boundary(self, point): #defines the grids boundaries
        [self.x,self.y] = point
        return 0 <= self.x < self.width and 0 <= self.y < self.height

    def node_neighbours(self, point): #defines the current nodes neighbours
        [self.x,self.y] = point
        results = [(self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y), (self.x, self.y+1)]
        results = filter(self.grid_boundary, results) #filters out the boundary results
        results = filter(self.can_pass_through, results) #filters out the coordinates that you can pass through from those you can't
        return results

    def can_pass_through(self, point):
        return point not in self.walls
        return point not in self.traps

#constructsthe2Dgrid
def build_grid(grid):
    for x in range(grid.width):
        for y in range (grid.height):
            print(x, y)
    return "grid created" + widht + " " + height

board = game_board(250, 150)
position = [50, 80]
board.boundary(position)
board.node_neighbours(position)
board.can_pass_through(position)
grid = build_grid(board)

robot = robot("test_bot", grid, position)
robot.neighbour([39, 22])
robot.position([45, 78])



    
