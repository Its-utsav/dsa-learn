from typing import List


class Solution:
    def digit_total(self, target: int, num: int) -> bool:
        if num < target:
            return False

        if target == num:
            return True

        return self.digit_total(target, num // 10)

    def punishmentNumber(self, num: int) -> int:
        nums = []  # numbers that square's sum equals to the number itself
        ans = 0
        for i in range(1, num + 1):
            square = i * i
            # print(i, nums, square)

            if self.digit_total(i, square):
                ans += square
                print(i)

        print(ans)

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = {}  # store the number and thier index
        # for index, num in enumerate(nums):
        #     print(index, num)

        for i in range(len(nums)):
            num = nums[i]
            if num in hs and i - hs[num] <= k:
                return True
            hs[num] = i

        print(hs)
        return False

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [-1, -1]
        n = len(grid)
        hs = [0] * (n**2)

        for arr in grid:
            for i in range(n):
                # print("Value")
                hs[arr[i] - 1] += 1

        for i in range(len(hs)):
            if hs[i] == 2:  # twice
                ans[0] = i + 1
            if hs[i] == 0:  # missing
                ans[1] = i + 1
        return ans

    def minimumRecolor(self, blocks: str, k: int) -> int:
        ans = float("inf")
        count = 0  # that store the w -> b
        left = 0
        n = len(blocks)

        for right in range(n):
            if blocks[right] == "W":
                count += 1

            if right - left + 1 == k:
                ans = min(ans, count)

                if blocks[left] == "W":
                    count -= 1

                left += 1

        return ans

    def bs_helper(self, nums: List[int], key: int) -> int:
        n = len(nums)
        ans = n
        low, high = 0, n
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < key:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans

    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg = self.bs_helper(nums, 0)  # total negtive number since 0 is not - or +
        pos = n - self.bs_helper(nums, 1)
        # print(neg, pos)
        return max(neg, pos)

    def maxOfSubarrays(self, arr, k):
        ans = []
        n = len(arr)
        left = 0
        valid = arr[left:k]
        ans.append(max(valid))
        for i in range(k + 1, n + 1):
            left += 1
            valid = arr[left:i]
            ans.append(max(valid))
        return ans


s = Solution()
print(s.maxOfSubarrays([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
# print(s.maximumCount([-3, -2, -1, 0, 0, 1, 2]))
# print(s.maximumCount([5, 20, 66, 1314]))

# print(s.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
# print(s.punishmentNumber(37))
