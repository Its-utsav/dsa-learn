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

    def max_sub_array(self, nums: List[int]) -> int:
        """
        TC -> O(n),
        SC -> O(1)
        """
        max_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum += num

            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        """
        Use full when all elements of array are less than zero
        """
        if max_sum < 0:
            return 0
        return max_sum

    def stock_buy_and_sell_1(self, nums: List[int]) -> int:
        max_profit = 0
        current_profit = 0
        n = len(nums)

        for i in range(0, n):
            for j in range(i + 1, n - 1):
                current_profit = nums[j] - nums[i]
                max_profit = max(current_profit, max_profit)

        return max_profit

    def stock_buy_and_sell_2(self, nums: List[int]) -> int:
        max_profit = 0
        min_profit = nums[0]
        diff = 0

        for num in nums:
            diff = num - min_profit
            max_profit = max(diff, max_profit)
            min_profit = min(num, min_profit)

        return max_profit

    def rearrange_array_elements(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        ans = [0] * n
        pos_index, neg_index = 0, 1
        for i in range(0, n):
            if nums[i] > 0:
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                ans[neg_index] = nums[i]
                neg_index += 2

            print(ans)

        return ans

    def permutation(self, nums: List[int]) -> List[List[int]]:
        """
        https://pythontutor.com/render.html#code=def%20permutation%28%20nums%29%20%3A%0A%20%20%20%20ans%20%3D%20%5B%5D%0A%20%20%20%20%23%20base%20case%0A%20%20%20%20if%20len%28nums%29%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20%5Bnums.copy%28%29%5D%0A%20%20%20%20for%20i%20in%20range%28len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20%23%20store%20first%20el%0A%20%20%20%20%20%20%20%20n%20%3D%20nums.pop%280%29%0A%20%20%20%20%20%20%20%20permuts%20%3D%20permutation%28nums%29%0A%20%20%20%20%20%20%20%20%23%20add%20first%20one%20ele%0A%20%20%20%20%20%20%20%20for%20perm%20in%20permuts%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20perm.append%28n%29%0A%20%20%20%20%20%20%20%20%23%20store%20in%20ans%0A%20%20%20%20%20%20%20%20ans.extend%28permuts%29%0A%20%20%20%20%20%20%20%20nums.append%28n%29%0A%20%20%20%20return%20ans%0A%20%20%20%20%0Aprint%28permutation%28%5B1,2,3%5D%29%29&cumulative=true&curInstr=46&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
        """
        """
        TC -> O(n! * n) n is the length of the array
        SC -> O(n^2)
        """
        ans = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):

            # store first el
            n = nums.pop(0)
            permuts = self.permutation(nums)
            # add first one ele
            for perm in permuts:
                perm.append(n)

            # store in ans
            ans.extend(permuts)

            nums.append(n)
            print(f"i ={i} ,n = {n}, permuts = {permuts}, ans = {ans}, og=  {nums}")
        return ans

    def rotate(self, matrix: List[List[int]]) -> None:
        ans = [[0] * len(matrix) for i in range(len(matrix))]
        # ans = [[0] * len(matrix)] * len(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                ans[i][j] = matrix[i][j]
        print(ans)
        pass


def generateSumArrays(nums: List[int]):
    ans = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums) + 1):
            # ans.append(nums[i:j])
            temp = []
            for k in range(i, j):
                temp.append(nums[k])

            ans.append(temp)

    print(ans)


def rearrange_array_elements_2(nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    pos, neg = [], []

    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    for i in range(0, len(nums) // 2):
        ans[2 * i] = pos[i]
        ans[2 * i + 1] = neg[i]

    return ans


def rearrange_array_elements_3(nums: List[int]) -> List[int]:
    pos, neg = [], []
    ans = [0] * (len(nums))

    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    if len(pos) > len(neg):
        # fill equal amount of elements
        for i in range(0, len(neg)):
            print(ans)
            ans[i * 2] = pos[i]
            ans[i * 2 + 1] = neg[i]

        # now fill all postive values
        index = len(neg) * 2
        print(index, len(nums), len(pos))

        for i in range(len(pos) - len(neg)):
            ans[index] = pos[len(neg) + i]
            index += 1
    else:
        for i in range(0, len(pos)):
            ans[2 * i] = pos[i]
            ans[2 * i + 1] = neg[i]

        index = len(pos) * 2

        for i in range(len(neg) - len(pos)):
            ans[index] = neg[len(pos) + i]
            index += 1

    return ans


s = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.rotate(a))
# print(rearrange_array_elements_3([-1, -2, -4, -5, 3, 1]))
