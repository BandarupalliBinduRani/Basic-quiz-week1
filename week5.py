import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4

def print_board(board):
    for row in board:
        print(" ".join(str(tile).rjust(4) if tile != 0 else '    ' for tile in row))
    print()

def move_board(board, direction):
    rotated_board = list(map(list, zip(*board[::-1])))
    if direction == 'UP':
        new_board = [merge_tiles(row) for row in rotated_board]
    elif direction == 'DOWN':
        new_board = [merge_tiles(row[::-1])[::-1] for row in rotated_board]
    elif direction == 'LEFT':
        new_board = [merge_tiles(row) for row in board]
    elif direction == 'RIGHT':
        new_board = [merge_tiles(row[::-1])[::-1] for row in board]
    return list(map(list, zip(*new_board[::-1])))

def merge_tiles(row):
    new_row = [0] * 4
    index = 0
    for tile in row:
        if tile != 0:
            if new_row[index] == 0:
                new_row[index] = tile
            elif new_row[index] == tile:
                new_row[index] *= 2
                index += 1
            else:
                index += 1
                new_row[index] = tile
    return new_row

def is_game_over(board):
    for row in board:
        if 0 in row or any(row[i] == row[i+1] for i in range(3)):
            return False
    for col in range(4):
        if any(board[i][col] == board[i+1][col] for i in range(3)):
            return False
    return True

def main():
    board = initialize_board()

    while True:
        clear_screen()
        print_board(board)

        if is_game_over(board):
            print("Game Over!")
            break

        direction = input("Enter direction (UP, DOWN, LEFT, RIGHT): ").upper()

        if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            new_board = move_board(board, direction)
            if new_board != board:
                board = new_board
                add_new_tile(board)
        elif direction == 'QUIT':
            break
        else:
            print("Invalid direction. Please enter UP, DOWN, LEFT, RIGHT.")

if __name__== "__main__":
    main()
