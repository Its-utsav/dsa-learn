from typing import List


class Searching:
    def linear_search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True

        return False

    def binary_search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        while mid <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid + 1
            mid = (start + end) // 2

        return -1


def main():
    s = Searching()
    print(s.binary_search([-1, 0, 3, 5, 9, 12], 9))


if __name__ == "__main__":
    main()
