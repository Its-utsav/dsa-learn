from typing import List


def merge_arr(nums: List[int], start: int, mid: int, end: int) -> None:
    """
    TC -> O(n)
    SC -> O(n)
    """
    temp = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= end:
        temp.append(nums[right])
        right += 1

    # store in orignal
    nums[start : end + 1] = temp


def merge_sort(nums: List[int], start: int, end: int) -> None:
    """
    TC -> O(log n)
    merge array -> O(n)
    overall -> O(n log n)

    SC  -> O(n)
    Auxilary SC -> O(n)

    """
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort(nums, start, mid)  # left part of the array
    merge_sort(nums, mid + 1, end)  # right part of the array
    # print(nums, mid)
    merge_arr(nums, start, mid, end)
    return nums


def place_pivot_at_right(nums: List, start: int, end: int) -> int:
    pivot = nums[start]
    i, j = start, end

    while i < j:
        # find index of bigest element from pivot from left side

        while nums[i] <= pivot and i <= end - 1:
            i += 1

        # find index of element that smaller than pivot from right side

        while nums[j] > pivot and j >= start + 1:
            j -= 1

        # reach at place where we found smaller and larger element so swap it and still i is smaller than j
        if i < j:
            [nums[i], nums[j]] = [nums[j], nums[i]]

    # set piovt at right place

    [nums[start], nums[j]] = [nums[j], nums[start]]

    return j


def quick_sort(nums: List[int], start: int, end: int) -> None:
    if start < end:
        print(nums)
        partition_index = place_pivot_at_right(nums, start, end)
        quick_sort(nums, start, partition_index - 1)
        quick_sort(nums, partition_index + 1, end)


a = [38, 27, 43, 3, 9, 82, 10]


quick_sort(a, 0, len(a) - 1)
print(a)
