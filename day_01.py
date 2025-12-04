from pathlib import Path
from utils import read_input

def getPasswords(file_content):
    part_one_password = 0
    part_two_password = 0
    dial_position = 50
    for line in file_content:
        rotation_direction = line[0]
        rotation_distance = int(line[1:])
        for _ in range(rotation_distance):
            if rotation_direction == 'L':
                dial_position = ((dial_position - 1 + 100) % 100)
            elif rotation_direction == 'R':
                dial_position = (dial_position + 1) % 100
            if dial_position == 0:
                part_two_password += 1
        if dial_position == 0:
            part_one_password += 1
    return (part_one_password, part_two_password)

def day_01():
    print("Advent of Code 2025 - day 1")
    file_path = Path('.', 'data', 'input_01.txt')
    file_content = read_input(file_path)
    if file_content:
        passwords = getPasswords(file_content)
        print(f"Solution for part one: {passwords[0]}")
        print(f"Solution for part two: {passwords[1]}")

day_01()