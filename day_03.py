from pathlib import Path
from utils import read_input

def solve_first_part(file_content):
    part_one_answer = 0
    for line in file_content:
        first_digit = line[0]
        second_digit = max(line[1:])
        for i in range(1, len(line)-1):
            if int(line[i]) > int(first_digit):
                first_digit = line[i]
                second_digit = max(line[i+1:])
        largest_joltage = int(first_digit + second_digit)
        part_one_answer += largest_joltage
    return part_one_answer

def solve_second_part(file_content):
    part_two_answer = 0
    for line in file_content:
        largest_joltage = [int(char) for char in line[-12:]]
        rest_of_batteries = [int(char) for char in line[-13::-1]]
        for battery in rest_of_batteries:
            if battery >= largest_joltage[0]:
                joltage_was_removed = False
                for index in range(0, 11):
                    if largest_joltage[index] < largest_joltage[index+1]:
                        largest_joltage.pop(index)
                        joltage_was_removed = True
                        break
                if not joltage_was_removed:
                    largest_joltage.remove(min(largest_joltage))
                largest_joltage = [battery] + largest_joltage
        largest_joltage = int(''.join(str(x) for x in largest_joltage))
        part_two_answer += largest_joltage
    return part_two_answer

def day_03():
    print("Advent of Code 2025 - day 3")
    file_path = Path('.', 'data', 'input_03.txt')
    file_content = read_input(file_path)
    if file_content:
        first_solution = solve_first_part(file_content)
        print(f"Solution for part one: {first_solution}")
        second_solution = solve_second_part(file_content)
        print(f"Solution for part two: {second_solution}")

day_03()