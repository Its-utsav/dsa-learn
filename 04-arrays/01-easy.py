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

    def rotate_1(self, matrix: List[List[int]]) -> None:
        ans = [[0] * len(matrix) for i in range(len(matrix))]
        # ans = [[0] * len(matrix)] * len(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                ans[j][n - i - 1] = matrix[i][j]
        print(ans)

    def rotate_2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transponse
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #  reverese

        for i in range(n):
            matrix[i].reverse()

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)  # Number of row
        n = len(matrix[0])  # Number of column

        # row matrix [....][0]
        # col matrix[0][....]
        col0 = 1  #  track first column change
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # mark row

                    # mark column
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # matrix[...][0] => 0
        # matrix[0][...] => 0
        # than marks rest of the elements

        # mark element as 0 other than first row , column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # now remining part

        # set column as 0
        if col0 == 0:
            for i in range(m):
                matrix[0][i] = 0

        # only first is 0
        if matrix[0][0] == 0:

            for j in range(m):
                matrix[j][0] = 0

        print(matrix)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        top, left = 0, 0
        right, bottom = n - 1, m - 1

        while left <= right and top <= bottom:
            # left -> right (top side)
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1

            # right -> bottom (right side)
            for j in range(top, bottom + 1):
                ans.append(matrix[j][right])

            right -= 1

            if top <= bottom:
                # right -> left (bottom side)
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

                bottom -= 1

            if left <= right:
                # bottom -> top (left)
                for j in range(bottom, top - 1, -1):
                    ans.append(matrix[j][left])

                left += 1

        return ans

    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        n = len(nums)

        # find the break point
        for i in range(n - 2, 0, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # handle break point not found tha given permutaion is the largest
        if index == -1:
            nums.reverse()
            return

        # swap the break point element with nearest greater element

        for i in range(n - 1, 0, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]

        # reverse the reaminign elements index + 1 -> n-1
        nums[index + 1 :] = reversed(nums[index + 1 :])
        print(nums)

    def leaders(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = []
        right_max = nums[n - 1]
        res.append(right_max)
        # print(res)
        for i in range(n - 2, -1, -1):
            if nums[i] >= right_max:
                res.append(nums[i])
                right_max = nums[i]

        print(res)
        res = list(reversed(res))
        # i, j = 0, len(res) - 1
        # while i <= len(res) // 2:
        #     temp = res[i]
        #     res[i] = res[j]
        #     res[j] = temp
        #     i += 1
        #     j -= 1

        return res

    def linear_search(self, nums: List[int], x: int) -> bool:
        for num in nums:
            if num == x:
                return True

        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        count = 0
        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                current_num = num

                print(current_num)
                while current_num + 1 in num_set:
                    count += 1
                    current_num += 1

            longest = max(count, longest)

        return longest

    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        temp = []
        for num in nums:
            if num == val:
                count += 1
            elif num != val:
                temp.append(num)
        ans = len(temp)
        for i in range(ans, count):
            temp.append("_")

        return ans


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


def setZeroes_1(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    row = [0] * m
    col = [0] * n

    # set 1 for  row , column  where element is 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(m):
        for j in range(n):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

    print(matrix)


def setZeroes_2(matrix: List[List[int]]) -> None:
    pass


def genper(nums: List[int], ans: List[List[int]], index) -> None:
    if index >= len(nums):
        ans.append(nums[:])
        return
    for i in range(index, len(nums)):
        nums[i], nums[index] = nums[index], nums[i]
        genper(nums, ans, index + 1)
        nums[i], nums[index] = nums[index], nums[i]


def generate_permutation_in_sorted(nums: List[int]) -> List[List[int]]:
    ans = []
    genper(nums, ans, 0)
    return ans


def nextPermutation(nums: List[int]) -> None:
    permutations = generate_permutation_in_sorted(nums)
    # print(permutations)
    for i in range(len(permutations)):
        if nums == permutations[i]:
            return permutations[i + 1]


def linear_search(nums: List[int], x: int) -> bool:
    for num in nums:
        if num == x:
            return True
    return False


def longestConsecutive_1(nums: List[int]) -> int:
    """
    TC -> O(n^2)
    SC -> O(1)
    """
    longest = 1
    n = len(nums)
    for i in range(n):
        current_num = nums[i]
        current_count = 1
        while linear_search(nums, current_num + 1):
            current_count += 1
            current_num += 1
        longest = max(current_count, longest)
    return longest


def longestConsecutive_2(nums: List[int]) -> int:
    """
    TC -> O(n^2)
    SC -> O(1)
    """
    n = len(nums)
    longest = 1
    count = 0
    last_small = float("-inf")
    nums.sort()  # O(log n)

    for i in range(n):
        if nums[i] - 1 == last_small:
            count += 1
            last_small = nums[i]
        elif nums[i] != last_small:
            count = 1
            last_small = nums[i]

        longest = max(longest, count)

    return longest


s = Solution()
a = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
b = [[0, 1]]
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = [0, 1, 2, 2, 3, 0, 4, 2]
print(s.removeElement(d, 2))
# print(longestConsecutive_2(d))
