from typing import List, Set, Tuple

from collections import defaultdict


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


def valid_anagram(s: str, t: str) -> bool:
    # length should be same
    if len(s) != len(t):
        return False

    s_hash = {}
    for ch in s:
        s_hash[ch] = s_hash.get(ch, 0) + 1

    for ch in t:
        if s_hash[ch] not in s_hash or s_hash[ch] == 0:
            return False

    return True


def second_largest(arr: List[int]) -> int:
    maxi = -1
    sec_max = -1

    for num in arr:
        if num > maxi:
            sec_max = maxi
            maxi = num

        elif num > sec_max and num != maxi:
            sec_max = num

    return sec_max


def findUnion(a, b):
    # code here
    left = 0
    right = 0

    ans = []

    while left < len(a) and right < len(b):
        if a[left] <= b[right]:
            if len(ans) == 0 or ans[-1] != a[left]:
                ans.append(a[left])

            left += 1

        else:

            if len(ans) == 0 or ans[-1] != b[right]:
                ans.append(a[right])

            right += 1

    while left < len(a):
        if ans[-1] != a[left]:
            ans.append(a[left])

        left += 1
    while right < len(b):
        if ans[-1] != b[right]:
            ans.append(a[right])

        right += 1
    ans.sort()
    return ans
    # ans = []
    # s = set()
    # for i in a:
    #     s.add(i)

    # for i in b:
    #     s.add(i)

    # for i in s:
    #     ans.append(i)
    # ans.sort()
    # return ans


def lenOfLongestSubarr(arr: List[int], k: int) -> int:
    max_len = 0
    prefix_sum = 0
    pre_sum_hash = {}
    n = len(arr)

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_len = max(max_len, i + 1)

        diff = prefix_sum - k

        if diff in pre_sum_hash:
            l = i - pre_sum_hash[diff]
            max_len = max(max_len, l)
        # in map than get the  index and set the maxlen

        # add prefix sum in hash
        if prefix_sum not in pre_sum_hash:
            pre_sum_hash[prefix_sum] = i
    return max_len


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    ans = []
    hs = {}
    n = len(nums)
    for i in range(1, n + 1):
        hs[i] = 1

    print(hs)
    for num in nums:
        if num in hs:
            hs[num] -= 1
    print(hs)
    ans = []
    for k in hs:
        if hs[k] == 1:
            ans.append(k)
    return ans


def findMaxLength(nums: List[int]) -> int:
    count_0 = count_1 = 0

    for num in nums:
        if num == 0:
            count_0 += 1
        else:
            count_1 += 1

    print(count_1, count_0)


def replace_element(nums: List) -> List[int]:
    maxi = -1
    nums[len(nums) - 1] = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > maxi:
            maxi = nums[i]
        else:
            nums[i] = maxi

    return nums


def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False

    j = 0

    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1

    return j == len(s)


def longestCommonPrefix(strs: str) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        k = 0
        for j in range(0, min(len(strs[i]), len(prefix))):
            if strs[i][j] == prefix[k]:
                k += 1
            else:
                break

        prefix = prefix[:k]

    return prefix


def number_of_unique_email(emails: List[str]) -> int:
    s = set()

    for e in emails:
        local_name, domain_name = e.split("@")
        local_name = local_name.split("+")[0]
        local_name = local_name.replace(".", "")
        s.add((local_name, domain_name))
    return len(s)


def isIsomorphic_helper(s: str, t: str) -> True:
    mp = {}

    for i in range(len(s)):
        if (s[i] in mp) and (mp[s[i]] != t[i]):
            return False

        mp[s[i]] = t[i]
    return True


def isIsomorphic(s: str, t: str) -> bool:
    return isIsomorphic_helper(s, t) and isIsomorphic_helper(t, s)


def isIsomorphic_v2(s: str, t: str) -> bool:
    mpST = mpTS = {}

    for i in range(len(s)):
        if (s[i] in mpST and mpST[s[i]] != t[i]) or (
            (t[i] in mpTS and mpTS[t[i]] != s[i])
        ):
            return False

        mpST[s[i]] = t[i]
        mpTS[t[i]] = s[i]
    return True


def remove_duplicates(nums: List[int]) -> int:
    s = set(nums)
    j = 0
    c = 0
    for i in range(1, len(nums) - 1):

        if nums[i] == j:
            print(f"match at {i} {nums[i]} {j}")
            c += 1

        if c == 2:
            print(f"match at {i} {nums[i]} {j}")
            j += 1
            nums[i] = j
            c = 0
            continue

    print(nums)
    return j


def reverse_string(s: List[str]) -> List[str]:
    n = len(s)
    i = 0
    j = n - 1
    while i <= j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


def subarray_xor_as_k(arr: List[int], k: int) -> int:
    count = 0
    xr = 0  # default value
    mp = defaultdict(int)
    mp[xr] = 1
    for i in range(len(arr)):
        xr = xr ^ arr[i]
        x = xr ^ k
        count += mp[x]

        mp[xr] += 1

    return count


def nextGreaterElement(arr1: List[int], arr2: List[int]) -> List[int]:
    ans = [-1] * len(arr1)
    # mp = {}
    # for i in range(len(arr1)):
    #     mp[arr1[i]] = mp.get(arr1[i], i)

    mp = {n: i for i, n in enumerate(arr1)}
    print(mp)
    for i in range(len(arr2)):
        if arr2[i] not in mp:
            continue

        for j in range(i + 1, len(arr2)):
            if arr2[j] > arr2[i]:
                index = mp[arr2[i]]
                ans[index] = arr2[j]
                break

    return ans


def firstUniqChar(s: str) -> int:
    hs = {}
    for ch in s:
        hs[ch] = hs.get(ch, 0) + 1

    u_char = ""

    for key in hs:
        if hs[key] == 1:
            u_char = key
            break

    for i in range(len(s)):
        if s[i] == u_char:
            return i
    return -1


print(firstUniqChar("loveleetcode"))


# print(findUnion([2, 2, 3, 4, 5], [1, 1, 2, 3, 4]))
# print(findUnion([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]))
