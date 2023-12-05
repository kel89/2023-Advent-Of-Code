def is_valid(row, col, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= row < rows and 0 <= col < cols and matrix[row][col].isdigit()

def extract_number(row, col, matrix):
    number = ""
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if is_valid(new_row, new_col, matrix) and matrix[new_row][new_col].isdigit():
            number += matrix[new_row][new_col]

    return number

def sum_adjacent_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j].isdigit():
                adjacent_to_symbol = False
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = i + dx, j + dy
                    if is_valid(new_row, new_col, matrix) and matrix[new_row][new_col] != '.':
                        adjacent_to_symbol = True
                        break
                if adjacent_to_symbol:
                    total_sum += int(extract_number(i, j, matrix))

    return total_sum

# Example engine schematic
engine_schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

result = sum_adjacent_numbers(engine_schematic)
print("The sum of part numbers adjacent to symbols is:", result)
