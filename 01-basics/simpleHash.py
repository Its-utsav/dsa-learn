from typing import List


class SimplHash:
    def frq_of_array_element(self, arr: List[int]) -> List[int]:
        """
        TC,SD -> O(n)
        """
        n = len(arr)
        ans = [0] * (n + 1)
        for i in range(0, n):
            ans[arr[i]] += 1

        return ans[1:]

    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        TC -> O(n) + O(n) + O(n) = O(3n) == O(n)
        SC -> O(n) n is lenght of the nums list
        """
        numHash = {}
        for num in nums:
            numHash[num] = numHash.get(num, 0) + 1

        max_frq = max(numHash.values())
        c = 0
        for num in numHash:
            if numHash[num] == max_frq:
                c += 1

        return max_frq * c


sol = SimplHash()

print(sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
print(sol.maxFrequencyElements([1, 2, 3, 4, 5]))
