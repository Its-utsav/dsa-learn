from typing import List, Set, Tuple


def nCr(num: int, c: int) -> int:
    ans = 1
    for i in range(0, c):
        ans = ans * (num - i)
        ans = ans // (i + 1)
    return int(ans)


class Solution:
    def generate_row(self, row: int):
        ans = 1
        ans_row = [1]

        for i in range(1, row):
            ans = int(ans * (row - i))
            ans = int(ans // i)
            ans_row.append(ans)

        return ans_row

    def pascal_triangle(self, nums: int) -> List[List[int]]:
        ans = []
        for i in range(1, nums + 1):
            ans.append(self.generate_row(i))

        return ans

    def majority_element_ii(self, nums: List[int]) -> int:
        n = len(nums)
        count1, count2 = 0, 0
        ele1, ele2 = 0, 0

        for num in nums:
            if count1 == 0 and ele2 != num:
                ele1 = num
                count1 = 1
            elif count2 == 0 and ele1 != num:
                ele2 = num
                count2 = 1
            elif num == ele1:
                count1 += 1
            elif num == ele2:
                count2 += 2
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == ele1:
                count1 += 1
            if num == ele2:
                count2 += 1
        ans = []
        if count1 >= n // 2:
            ans.append(ele1)

        if count2 >= n // 2:
            ans.append(ele2)

        return ans

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n - 2):
            print(ans)
            if nums[i] == nums[i - 1] and i > 0:
                continue

            # pointers
            j = i + 1
            k = n - 1

            # sum of three

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:  # small value need higher value
                    j += 1
                elif total_sum > 0:  # big value need small values
                    k -= 1
                elif total_sum == 0:  # haha get triplest

                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1

                    # current element is same as previous just move ahead

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans


s = Solution()
print(s.three_sum([1, -1, -1, 0]))
