from pathlib import Path
from utils import read_input

def solve_puzzle(file_content):
    first_part_answer = 0
    second_part_answer = 0
    id_ranges = file_content.split(',')
    for id_range in id_ranges:
        first_id, last_id = map(int, id_range.split('-'))
        for id in range(first_id, last_id + 1):
            str_id = str(id)
            if str_id[:len(str_id) // 2] == str_id[len(str_id) // 2:]:
                first_part_answer += id
                second_part_answer += id
            else:
                chunk_size = 1
                while chunk_size <= len(str_id) // 2:
                    if len(set([str_id[i:i + chunk_size] for i in range(0, len(str_id), chunk_size)])) == 1:
                        second_part_answer += id
                        break
                    chunk_size += 1
    return first_part_answer, second_part_answer

def day_02():
    print("Advent of Code 2025 - day 2")
    file_path = Path('.', 'data', 'input_02.txt')
    file_content = read_input(file_path)
    if file_content:
        solution = solve_puzzle(file_content[0])
        print(f"Solution for part one: {solution[0]}")
        print(f"Solution for part two: {solution[1]}")

day_02()