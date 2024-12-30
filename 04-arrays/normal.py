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


print(three_sum_v2([-1, 0, 1, 2, -1, -4]))
