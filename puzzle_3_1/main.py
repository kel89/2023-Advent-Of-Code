

f = open("puzzle_3_1/input.txt", "r")
matrix = []
syms = []
for l in f:
    matrix.append([x for x in [*l] if x != "\n"])
    for x in l:
        syms.append(x)
# print(matrix)

symbols = ['%', '#', '*', '+', '$', '.', '-', '=', '/', '@', '&']
def is_symbol(x):
    return x in symbols


def get_adjoining_nums(i, j):
    nums = []

    if i > 0:
        # Check upper left
        if j > 0:
            pass

        # Check above

        # Check top right
        if j < len(matrix[i]):
            pass

    if j > 0:
        # CHeck left
        pass
    
    # Check right
    if j < len(matrix[i]):
        pass

    if i < len(matrix) -1:
        # Check lower left
        if j > 0:
            pass

        # CHeck below

        # Check lower right
        if j < len(matrix[i]):
            pass

i = 0
j = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        if matrix[i][j].isdigit():
            # Find entire digit
            j2 = j
            while matrix[i][j2].isdigit() and j2 < (len(matrix[i])-1):
                j += 1
            num = int(matrix[i][j:j2+1])
            print(num)
            j = j2 + 1
        j += 1
    i += 1



# for i in len(matrix):
#     for j in len(l):
#         if matrix[i][j].isdigit()
