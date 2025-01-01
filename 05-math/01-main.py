from typing import List


def nCr_value(num: int, column: int) -> int:
    ans = 1
    for i in range(0, column):
        ans = ans * (num - i)
        ans = ans / (i + 1)

    return int(ans)


def pascal_triangle_row_1(num: int):
    for c in range(1, num + 1):
        print(nCr_value(num - 1, c - 1), end=" ")


def pascal_triangle_row_2(num: int):
    ans = 1
    for i in range(1, num):
        ans = int(ans * (num - i))
        ans = int(ans / i)
        print(ans, end=" ")


def getRow(rowIndex: int) -> List[int]:
    row = [1]
    ans = 1
    for i in range(0, rowIndex):
        ans = ans * (rowIndex - i)
        ans = ans // (i + 1)
        print(ans)
        row.append(ans)

    return row


print(getRow(3))
