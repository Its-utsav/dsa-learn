## pascal triangle

```python
def nCr_value(num: int, column: int) -> int:
    ans = 1
    for i in range(0, column):
        ans = ans * (num - i)
        ans = ans / (i + 1)

    return int(ans)

def pascal_triangle( nums: int) -> List[List[int]]:
    ans = []
    for i in range(1, nums + 1):
        temp = []
        for j in range(1, i + 1):
            temp.append(nCr(i - 1, j - 1))
        ans.append(temp)
    return ans
```

- approx. $O(n^3)$
