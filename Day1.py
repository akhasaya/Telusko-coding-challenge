# iterative solution
def Pascal(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]

    rows = [[1],[1,1]]
    prev_row = [1,1]
    for i in range(2, n):
        next_row = [1]
        for i in range(len(prev_row)-1):
            next_row.append(prev_row[i]+prev_row[i+1])
        next_row.append(1)
        rows.append(next_row)
        prev_row = next_row

    return rows

result = Pascal(5)
for array in result:
    print(array)
