from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        ans = n * (n + 1) // 2
        for num in nums:
            ans = ans - num
        return ans

    def remove_duplicates_from_arr_1(self, nums: List[int]) -> int:
        """
        TC = O(n log n) n is length of the array and log n for sorting the array
        SC = O(n) We are creating n size
        """
        nums[:] = sorted(set(nums))

        s = sorted(set(nums))
        j = 0
        for num in s:
            nums[j] = num
            j += 1

        return len(s)

    def remove_duplicates_from_arr_2(self, nums: List[int]) -> int:
        """
        TC = O(n)
        SC = O(1)
        """
        n = len(nums)
        j = 0
        for i in range(1, n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            print(nums)

        return j + 1

    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        non_zero_index = 0

        for i in range(0, n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # set zero to end

        for i in range(non_zero_index, n):
            nums[i] = 0

        print(nums)

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, current_count = 0, 0
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        return max(max_count, current_count)

    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans ^ num

        return ans

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        num_hash = {}
        for i in range(0, n):
            req = target - nums[i]

            # find req in hash
            if req in num_hash:
                if nums[i] + req == target:
                    return [i, nums[req]]

            num_hash[nums[i]] = i

        print(num_hash)

    def sort_colors1(self, nums: List[int]) -> None:
        count_0, count_1, count_2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1

        # sort zero
        for i in range(0, count_0):
            nums[i] = 0

        # sort one
        for i in range(count_0, count_1 + count_0):
            nums[i] = 1

        # sort two

        for i in range(count_1 + count_0, len(nums)):
            nums[i] = 2

    def sort_colors2(self, nums: List[int]) -> None:
        low, mid = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        print(nums)

    def majorityElement1(self, nums: List[int]) -> int:
        n = len(nums)
        num_map = {}

        for i in range(0, n):
            num_map[nums[i]] = num_map.get(nums[i], 0) + 1

            if num_map.get(nums[i]) > n // 2:
                return nums[i]

        return -1

    def majorityElement2(self, nums: List[int]) -> int:
        count, el = 0, 0

        for num in nums:
            if count == 0:
                el = num
                count = 1
            elif el == num:
                count += 1
            else:
                count -= 1

        return el


def generateSumArrays(nums: List[int]) -> None:
    ans = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums) + 1):
            # ans.append(nums[i:j])
            temp = []
            for k in range(i, j):
                temp.append(nums[k])

            ans.append(temp)

    print(ans)


s = Solution()
# print(s.two_sum([2, 7, 11, 15], 9))
# print(s.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
# print(s.two_sum([3, 3], 6))
# print(s.missingNumber([0, 1]))
# print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(generateSumArrays([1, 2, 3, 4]))
