from typing import List


class SimplHash:
    def frqOfElement(self, arr: List[int]):
        ans = [0 for _ in range(len(arr))]  # [0] * len(arr)


sol = SimplHash()

print(sol.frqOfElement([2, 3, 2, 3, 5]))
