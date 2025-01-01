from typing import List, Set, Tuple


def majority_element_ii_v1(nums: List[int]) -> int:
    n = len(nums)
    ans = []
    count = 0
    for i in range(n):
        for j in range(n):
            if nums[i] not in ans and nums[i] == nums[j]:
                count += 1
        if count > n // 3:
            ans.append(nums[i])
        count = 0
        if len(ans) == 2:
            break
    print(ans)


def majority_element_ii_v2(nums: List[int]) -> int:
    n = len(nums)
    ans = []
    num_hash = {}

    for num in nums:
        num_hash[num] = num_hash.get(num, 0) + 1

        if num_hash.get(num) > n // 3 and num not in ans:
            ans.append(num)

        print(num_hash, ans)

        if len(ans) == 2:
            return ans

    return ans


def three_sum_v1(nums: List[int]) -> List[List[int]]:

    s = set()  # set due to only uniue
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    temp = tuple(temp)
                    s.add(temp)

    ans = [list(i) for i in s]
    return ans


def three_sum_v2(nums: List[int]) -> List[List[int]]:
    s: Set[Tuple[int]] = set()
    n = len(nums)
    for i in range(n):
        hash_set: Set[int] = set()
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])

            if third in hash_set:
                temp = [nums[i], nums[j], third]
                temp.sort()
                temp = tuple(temp)
                s.add(temp)

            hash_set.add(nums[j])

    print(s)
    ans = [list(i) for i in s]
    return ans


def pascal_getRow(rowIndex: int) -> List[int]:
    row = [1]
    val = 1
    for i in range(1, rowIndex):
        val = val * (rowIndex - 1) // i
        row.append(val)

    return row


def four_sum_v1(nums: List[int], target: int) -> List[List[int]]:
    s: Set[Tuple[int]] = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]

                        temp.sort()
                        temp = tuple(temp)
                        s.add(temp)

    ans = [list(i) for i in s]
    return ans


def four_sum_v2(nums: List[int], target: int) -> List[List[int]]:
    s = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            hash_set = set()
            for k in range(j + 1, n):
                temp_sum = nums[i] + nums[j] + nums[k]
                req = target - temp_sum

                if req in hash_set:
                    temp = [nums[i], nums[j], nums[k], req]
                    temp.sort()
                    temp = tuple(temp)
                    s.add(temp)

                hash_set.add(nums[k])
    # print(s)
    ans = [list(i) for i in s]
    return ans


def roman_to_int(s: str) -> int:
    val = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    ans = 0
    for ch in s:
        ans += val[ch]
        print(ans, val[ch])
    return ans


def lengthOfLastWord(s: str) -> int:
    l = 0
    s = s.strip()

    for i in range(len(s) - 1, 0, -1):
        print(s[i] != " ")
        if s[i] != " ":
            l += 1
        else:
            break

    return l


print(lengthOfLastWord("Hello World"))
