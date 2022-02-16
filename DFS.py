import enum
import os
import abc
import string
import math
from queue import Queue
# Helper functions to aid in your implementation. Can edit/remove

"""#######################################################################
The code below includes the helper functions and data structure used in the whole program
#######################################################################"""
col_mapping = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

def is_within_board(row, col, total_row, total_col):
    return row  < total_row and row  >= 0 and col < total_col and col >= 0

obstacles = []
def no_obstacle(row, col):
    return (row, col) not in obstacles

def can_travel(board, col, row):
    return ((row, col) not in board.obstacles and board.map[row][col] != ".")

"""#######################################################################
The code below refers to the classes of the chess pieces, including King, Queen, Bishop, Rook and Knight
Each piece class stores information about the movement and generate all the available positions it can move to.
To initialize each piece class, users are expected to provide the total rows and total columns of the game board.
#######################################################################"""

class Piece:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
    def get_blocked_positions(self, curr_pos):
        pass

class King(Piece):
    def get_blocked_positions(self, curr_pos):
        row, col = curr_pos[0], curr_pos[1]
        states = list()
        #explore in clockwise direction
        if (is_within_board(row - 1, col, self.rows, self.cols) and no_obstacle(row - 1, col)):
            states.append(State((row - 1, col)))
        if (is_within_board(row - 1, col + 1, self.rows, self.cols) and no_obstacle(row - 1, col + 1)):
            states.append(State((row - 1, col + 1)))
        if (is_within_board(row, col + 1, self.rows, self.cols) and no_obstacle(row, col + 1)):
            states.append(State((row, col + 1)))
        if (is_within_board(row + 1, col + 1, self.rows, self.cols) and no_obstacle(row + 1, col + 1)):
            states.append(State((row + 1, col + 1)))
        if (is_within_board(row + 1, col, self.rows, self.cols) and no_obstacle(row + 1, col)):
            states.append(State((row + 1, col)))
        if (is_within_board(row + 1, col - 1, self.rows, self.cols) and no_obstacle(row + 1, col - 1)):
            states.append(State((row + 1, col - 1)))
        if (is_within_board(row , col - 1, self.rows, self.cols) and no_obstacle(row, col - 1)):
            states.append(State((row, col - 1)))
        if (is_within_board(row - 1, col - 1, self.rows, self.cols) and no_obstacle(row - 1, col - 1)):
            states.append(State((row - 1, col - 1)))
        return states
    def get_next(self, board, curr_pos):
        row, col = curr_pos[0], curr_pos[1]
        states = list()
        if (is_within_board(row - 1, col, self.rows, self.cols) and can_travel(board, col, row - 1)):
            states.append(State((row - 1, col)))
        if (is_within_board(row - 1, col + 1, self.rows, self.cols) and can_travel(board, col + 1, row - 1)):
            states.append(State((row - 1, col + 1)))
        if (is_within_board(row, col + 1, self.rows, self.cols) and can_travel(board, col + 1, row)):
            states.append(State((row, col + 1)))
        if (is_within_board(row + 1, col + 1, self.rows, self.cols) and can_travel(board, col + 1, row + 1)):
            states.append(State((row + 1, col + 1)))
        if (is_within_board(row + 1, col, self.rows, self.cols) and can_travel(board, col, row + 1)):
            states.append(State((row + 1, col)))
        if (is_within_board(row + 1, col - 1, self.rows, self.cols) and can_travel(board, col - 1, row + 1)):
            states.append(State((row + 1, col - 1)))
        if (is_within_board(row , col - 1, self.rows, self.cols) and can_travel(board, col - 1, row)):
            states.append(State((row, col - 1)))
        if (is_within_board(row - 1, col - 1, self.rows, self.cols) and can_travel(board, col - 1, row - 1)):
            states.append(State((row - 1, col - 1)))
        return states

class Queen(Piece):
    def get_blocked_positions(self, curr_pos):
        row, col = curr_pos[0], curr_pos[1]
        states = []
        for i in range(self.cols):
            if (no_obstacle(row, i)):
                states.append(State((row, i)))
            else:
                break
        for i in range(self.rows):
            if (no_obstacle(i, col)):
                states.append(State((i, col)))
            else:
                break
        dx, dy = row - 1, col - 1
        while (dx >= 0 and dy >= 0):
            if (no_obstacle(dx, dy)):
                states.append(State((dx, dy)))
            else:
                break
        dx, dy = row + 1, col + 1
        while (dx < self.rows and dy < self.cols):
            if (no_obstacle(dx, dy)):
                states.append(State((dx, dy)))
            else:
                break
        return states

class Bishop(Piece):
    def get_blocked_positions(self, curr_pos):
        dx, dy = row - 1, col - 1
        while (dx >= 0 and dy >= 0):
            if (no_obstacle(dx, dy)):
                states.append(State((dx, dy)))
            else:
                break
        dx, dy = row + 1, col + 1
        while (dx < self.rows and dy < self.cols):
            if (no_obstacle(dx, dy)):
                states.append(State((dx, dy)))
            else:
                break
    pass

class Rook(Piece):
    def get_blocked_positions(self, curr_pos):
        row, col = curr_pos[0], curr_pos[1]
        states = []
        for i in range(self.cols):
            if (no_obstacle(row, i)):
                states.append(State((row, i)))
            else:
                break
        for i in range(self.rows):
            if (no_obstacle(i, col)):
                states.append(State((i, col)))
            else:
                break
        return states

class Knight(Piece):
    def get_blocked_positions(self, curr_pos):
        row, col = curr_pos[0], curr_pos[1]
        horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
        vertical = [1, 2, 2, 1, -1, -2, -2, -1]
        states = []
        for i in range(len(horizontal)):
            dx, dy = row - horizontal[i], col - vertical[i]
            if is_within_board(dx, dy, self.rows, self.cols) and no_obstacle(dx, dy):
                states.append(State((dx, dy)))
        return states
    def get_next(self, board, curr_pos):
        row, col = curr_pos[0], curr_pos[1]
        horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
        vertical = [1, 2, 2, 1, -1, -2, -2, -1]
        states = []
        for i in range(len(horizontal)):
            dx, dy = row - horizontal[i], col - vertical[i]
            if is_within_board(dx, dy, self.rows, self.cols) and can_travel(board, dx, dy):
                states.append(State((dx, dy)))
        return states

"""#######################################################################
The code below refers to the generation of the game board.
To initialize the board class, users are expected to provide the size of the board (rows * cols), the number of obstacles,
the position of each obstacles (as a list), the enemies information (type and position, represented as a list), the 
starting position of the King piece, and the goal position(s) of the map.
#######################################################################"""

class Board:
    def __init__(this, rows, cols, obstacle_no, obstacles, enemies, start_pos, goal_pos):
        this.rows = rows
        this.cols = cols
        this.obstacle_no = obstacle_no
        this.map = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append('0')
            this.map.append(col)
        this.obstacles = obstacles.copy()
        for i in range(len(obstacles)):
            this.map[obstacles[i][0]][obstacles[i][1]] = 'X'
        for i in range(len(enemies)):
            type = enemies[i][0]
            if type == "King":
                this.map[enemies[i][1]][enemies[i][2]] = '♔'
            elif type == "Queen":
                this.map[enemies[i][1]][enemies[i][2]] = '♕'
            elif type == "Rook":
                this.map[enemies[i][1]][enemies[i][2]] = '♖'
            elif type == "Bishop":
                this.map[enemies[i][1]][enemies[i][2]] = '♗'
            elif type == "Knight":
                this.map[enemies[i][1]][enemies[i][2]] = '♘'
        this.map[start_pos[0]][start_pos[1]] = '♚'
        this.start_pos = (start_pos[0], start_pos[1])
        this.goal_pos = goal_pos
        if goal_pos != None:
            for i in range(len(goal_pos)):
                this.map[goal_pos[i][0]][goal_pos[i][1]] = 'G'

    def print(this, show_curs=False):
        if show_curs:
            for i in range(this.rows + 1):
                if i + 1 == this.rows + 1:
                    for length in range(int(math.log(i + 1))):
                        print(" ", end="")
                    print(" | ", end = "")
                    count = 0
                    for c in string.ascii_lowercase:
                        if count >= this.cols:
                            break
                        print(c, end = " | ")
                        count += 1
                    print()
                else:
                    if i < 10:
                        print("",i, end = " | ")
                    else:
                        print(i, end = " | ")
                if i < this.rows:
                    for j in range(this.cols):
                        print(this.map[i][j], end=" | ")
                    print()
        else:
            for i in range(this.rows):
                for j in range(this.cols):
                    print(this.map[i][j], end=" | ")
                print()
        print()

"""#######################################################################
The code below refers to the node of the graph when launching the algorithm, instead of state.
Each state (node) stores the current position of the piece to escape, its parent node (for tracing), and its state (which
is just current position in tuple format)
#######################################################################"""
class State:
    def __init__(self, curr_pos):
        self.curr_row = curr_pos[0]
        self.curr_col = curr_pos[1]
        self.parent = None
        self.state = curr_pos
    def __repr__(self):
        return "(" + str(chr(97 + self.curr_col)) + "," + str(self.curr_row) + ")"

class ActionList:
    def __init__(self, list):
        self.list = list

    def append(self, elm):
        self.list.append(elm)

    def __repr__(self):
        string = ""
        for i in range(len(self.list)):
            if i != len(self.list) - 1:
                string += str(self.list[i]) + ","
            else:
                string += str(self.list[i])
        return "[" + string + "]"


"""#######################################################################
The code below refers to the actual searching algorithm adopted in the program
#######################################################################"""

def search():
    frontier = list()
    king = King(board.rows, board.cols)
    curr = State(board.start_pos)
    curr.parent = None
    frontier.append(curr)
    nodesExplored = 0
    actions = []
    while not len(frontier) == 0:
        board.map[curr.curr_row][curr.curr_col] = '.'
        curr = frontier.pop()
        board.map[curr.curr_row][curr.curr_col] = '♚'
        nodesExplored += 1
        if (curr.curr_row, curr.curr_col) in board.goal_pos:
            while curr.parent is not None:
                temp1 = []
                temp = ActionList(temp1)
                temp.append(curr.parent)
                temp.append(curr)
                actions.append(temp)
                curr = curr.parent
            actions.reverse()
            return actions, nodesExplored
        expand = king.get_next(board, curr.state)
        for node in expand:
            node.parent = curr
            frontier.append(node)
    return actions, 0


### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: List of moves and nodes explored
def run_DFS():
    # You can code in here but you cannot remove this function or change the return type
    moves, nodesExplored = search() #For reference
    return moves, nodesExplored #Format to be returned

"""#######################################################################
The code below refers to the reading of the input text file.
It is assume that the input text file is always in a correct input format.
#######################################################################"""

def read_board_data(file):
    lines = file.readlines()
    col_no, goal_pos, obstacle_no, obstacles, row_no, start_pos = read_board_layout_and_start_goal(lines)
    idx, cost_matrix = read_cost(col_no, lines, row_no)
    enemies = read_enemies_data(idx, lines, row_no, col_no, obstacles)

    return row_no, col_no, obstacle_no, obstacles, enemies, start_pos, goal_pos, cost_matrix


def read_enemies_data(idx, lines, row_no, col_no, obstacles):
    enemy_count = lines[idx].replace("Number of Enemy King, Queen, Bishop, Rook, Knight (space between):", "").split()
    total_enemy = 0
    enemies = []
    idx += 2
    for i in range(len(enemy_count)):
        total_enemy += int(enemy_count[i])
    #mark enemy positions as obstacles
    for num in range(total_enemy):
        data = lines[idx].replace('[', "").replace(']', "").split(',')
        data_piece = data[0]
        data_pos = data[1]
        data_row = int(data_pos[1])
        data_col = col_mapping[data_pos[0]]
        enemies.append((data_piece, data_row, data_col))
        obstacles.append((data_row, data_col))
        idx += 1
        # according to type of piece, set position as obstacle
        enemy = get_piece(data_piece, row_no, col_no)
        cannot_go = []
        cannot_go = enemy.get_blocked_positions((data_row, data_col))
        if cannot_go is not None:
            for block in cannot_go:
                tuple = (block.curr_row, block.curr_col)
                obstacles.append(tuple)
    return enemies

def get_piece(piece, rows, cols):
    if piece == "King":
        return King(rows, cols)
    elif piece == "Queen":
        return Queen(rows, cols)
    elif piece == "Rook":
        return Rook(rows, cols)
    elif piece == "Bishop":
        return Bishop(rows, cols)
    elif piece == "Knight":
        return Knight(rows, cols)

def print_cost_matrix():
    for i in range(len(cost_matrix)):
        print(cost_matrix[i])

def read_cost(col_no, lines, row_no):
    cost_matrix = init_cost_matrix(col_no, row_no)
    for i in range(len(lines)):
        curr = i + 5
        if (lines[curr].__contains__("Number of Enemy King, Queen, Bishop, Rook, Knight (space between):")):
            idx = curr
            break
        data = lines[curr].replace('[', "").replace(']', "").split(',')
        data_row = int(data[0][1:len(data[0])])
        data_col = int(col_mapping[data[0][0]])
        cost_matrix[data_row][data_col] = int(data[1])
    return idx, cost_matrix


def init_cost_matrix(col_no, row_no):
    cost_matrix = []
    for i in range(row_no):
        cost_cols = []
        for j in range(col_no):
            cost_cols.append(1)
        cost_matrix.append(cost_cols)
    return cost_matrix


def read_board_layout_and_start_goal(lines):
    row_no = int(lines[0].replace("Rows:", ""))
    col_no = int(lines[1].replace("Cols:", ""))
    obstacle_no = int(lines[2].replace("Number of Obstacles:", ""))
    str = lines[3].replace("Position of Obstacles (space between):", "").split()
    obstacles = []
    goal_pos = []
    for pos in str:
        obstacles.append((int(pos[1]), col_mapping[pos[0]]))
    idx = -1
    for i in range(4, len(lines)):
        if lines[i].__contains__("Starting Position of Pieces [Piece, Pos]:"):
            idx = i + 1
    if idx != -1:
        str = lines[idx]
        start_pos = (int(str[str.index(',') + 2: str.index(']')]), col_mapping[str[str.index(',') + 1]])
    if lines[-1].__contains__("Goal Positions (space between):"):
        str = lines[-1].replace("Goal Positions (space between):", "")
        if (str == "-"):
            goal_pos = None
        else:
            str = str.split()
            for i in range(len(str)):
                goal_pos.append((int(str[i][1]), col_mapping[str[i][0]]))
    else:
        goal_pos = None #no goal
    return col_no, goal_pos, obstacle_no, obstacles, row_no, start_pos

"""#######################################################################
The code below is the main code to execute the program. It is assume that the directory exists and the file(s) can be found.
#######################################################################"""

"""
file = open("Public Testcases/3.txt")
cost_matrix = []
row_no, col_no, obstacle_no, obstacles, enemies, start_pos, goal_pos, cost_matrix = read_board_data(file)
board = Board(row_no, col_no, obstacle_no, obstacles, enemies, start_pos, goal_pos)
print(run_DFS())
"""
for filename in os.listdir("Public Testcases"):
    file = open("Public Testcases/" + filename)
    row_no, col_no, obstacle_no, obstacles, enemies, start_pos, goal_pos, cost_matrix = read_board_data(file)
    board = Board(row_no, col_no, obstacle_no, obstacles, enemies, start_pos, goal_pos)
    print(run_DFS())
    board.print()

    