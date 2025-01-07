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

    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        # loop over the array
        for i in range(n):
            # i will not same as previous elemenet avoid duplicates
            # for the first 0 index element previous element not possible
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # need j
            for j in range(i + 1, n):
                # j will not same as previous element avoid duplicates
                # firstly we considerd the element at j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # poniters
                k = j + 1
                l = n - 1

                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if total_sum < target:
                        # need more
                        k += 1
                    elif total_sum > target:
                        # need less
                        l -= 1
                    elif total_sum == target:
                        # yes we find 4 elements

                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1
                        # once 4 element found than pointer will move
                        # ensuring that they are not same element as previous element

                        # pointers are moving so we need to ensure k did not cross l

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        print(ans)
        return ans

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("-inf")
        nums.sort()
        n = len(nums)
        for i in range(n):
            # poniter left , right
            left = i + 1
            right = n - 1
            # left pointer not cross right pointer
            while left < right:
                # count the sum
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1

                # else:
                #     return closest

            # if sum - target < closest - target
            # update the closet with sum
            # if sum < target
            # need more value
            # if sum > target
            # need less value

            # return closet

            pass

        return closest

    def maxlen(self, arr: List[int]) -> int:
        num_map = {}
        sum_ = 0
        ans = 0
        n = len(arr)

        for i in range(n):
            sum_ += arr[i]
            if sum_ == 0:
                ans = i + 1

            else:
                if sum_ in num_map:
                    ans = max(ans, i - num_map[sum_])
                else:
                    num_map[sum_] = i
        print(sum_)
        return ans

    def over_lap_arr(self, intervals: List[List[int]]) -> List[int]:
        # # sort the array
        # # ans array for return
        # ans = []
        # n = len(intervals)
        # # itereate over array
        # for i in range(n):
        #     # take first (start) and second (end) value
        #     start = intervals[i][0]
        #     end = intervals[i][1]

        #     # if current overlap array is already part of interval than skip it
        #     if ans and ans[-1][1] >= end:
        #         continue

        #     # stand at once time check other
        #     for j in range(i + 1, n):

        #         # if current array[j][1] second value is less than end value
        #         if intervals[j][0] < end:
        #             end = max(end, intervals[j][1])
        #         else:
        #             break
        #         # than end value should be bigger of end and arr[j][1]
        #         # if current array[j][1] second value is greater than end value skip it
        #     ans.append([start, end])
        # return ans
        ans = []
        n = len(intervals)
        intervals.sort()
        for i in range(n):
            if len(ans) == 0 or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][0])
        return ans

    def mereg_sorted_arr(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        k = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[k]
            if k < len(nums2):
                k += 1
        nums1.sort()

    def max_product(self, nums: List[int]) -> int:
        maxi = 1
        prefix = 0
        suffix = 0
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n - i - 1]

            maxi = max(maxi, max(prefix, suffix))
        return maxi


s = Solution()
# a = [1, 2, 3, 0, 0, 0]
# b = [2, 5, 6]
# a1 = 3
# b1 = 3
# print(s.mereg_sorted_arr(a, a1, b, b1))
# print(a)
print(s.max_product([2, 3, -2, 4]))
