rows = int(input())
matrix = []

for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)
even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(even_matrix)