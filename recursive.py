# iterative solution
def Pascal(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]

    prev_triangle = Pascal(n-1)
    prev_row = prev_triangle[-1]
    next_row = [1]
    for i in range(len(prev_row)-1):
        next_row.append(prev_row[i]+prev_row[i+1])
    next_row.append(1)
    prev_triangle.append(next_row)
    return prev_triangle

result = Pascal(7)
for array in result:
    print(array)