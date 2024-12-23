from typing import List


def bubble_sort_1(nums: List[int]) -> List[int]:
    """
    TC -> O(n^2) (average , wrost) n is lenght of nums list
    SC -> O(1) In place sorting
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n - i):
            if nums[j] <= nums[i]:
                [nums[i], nums[j]] = [nums[j], nums[i]]

    return nums


def bubble_sort_2(nums: List[int]) -> List[int]:
    """
    This algorithm for where array is nearly sorted
    TC -> Best O(n) , Worst, Average - O(n^2)
    SC -> O(1)
    """
    n = len(nums)
    step = 0
    for i in range(n, 0, -1):
        did_swap = False
        for j in range(0, i - 1):
            step += 1
            if nums[j] >= nums[j + 1]:
                [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]]
                did_swap = True

        if did_swap == False:
            break

    print(f"Did bubble sort in {step} step")
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    """
    TC -> O(n^2)
    SC -> O(1)
    """
    n = len(nums)
    for i in range(0, n - 1):
        assumeMin = i
        # For finding Minimum index
        for j in range(i + 1, n):
            if nums[j] < nums[assumeMin]:
                assumeMin = j

        [nums[i], nums[assumeMin]] = [nums[assumeMin], nums[i]]

    return nums


def insertion_sort(nums: List[int]) -> List[int]:
    """
    TC -> O(n^2)
    SC -> O(1)
    """
    n = len(nums)

    for i in range(0, n):
        j = i

        while j > 0 and nums[j - 1] > nums[j]:
            [nums[j - 1], nums[j]] = [nums[j], nums[j - 1]]
            j -= 1

    return nums


def main():
    print(insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
