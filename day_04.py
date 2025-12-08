from pathlib import Path
from utils import read_input

def create_grid(file_content):
    grid = []
    for line in file_content:
        grid_row = [char for char in line]
        grid.append(grid_row)
    return grid

def solve_first_part(grid):
    part_one_answer = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] == '@':
                adjacent_roll_count = 0
                for x in range(row-1, row+2):
                    for y in range(col-1, col+2):
                        if (x == row and y == col) or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[row]):
                            continue
                        if grid[x][y] == "@":
                            adjacent_roll_count += 1
                if adjacent_roll_count < 4:
                    part_one_answer += 1
    return part_one_answer

def solve_second_part(grid):
    part_two_answer = 0
    while True:
        current_removed = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == '@':
                    adjacent_roll_count = 0
                    for x in range(row-1, row+2):
                        for y in range(col-1, col+2):
                            if (x == row and y == col) or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[row]):
                                continue
                            if grid[x][y] == "@":
                                adjacent_roll_count += 1
                    if adjacent_roll_count < 4:
                        current_removed += 1
                        grid[row][col] = 'x'
        if current_removed == 0:
            break
        part_two_answer += current_removed
    return part_two_answer

def day_04():
    print("Advent of Code 2025 - day 4")
    file_path = Path('.', 'data', 'input_04.txt')
    file_content = read_input(file_path)
    if file_content:
        grid = create_grid(file_content)
        first_solution = solve_first_part(grid)
        print(f"Solution for part one: {first_solution}")
        second_solution = solve_second_part(grid)
        print(f"Solution for part two: {second_solution}")

day_04()