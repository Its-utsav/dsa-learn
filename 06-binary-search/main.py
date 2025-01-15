from typing import List


class Binary_Search_Solution:
    """
    effecient searching algorithm , by reducing search range
    """

    def bs_iterative(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            # print(nums[low:high])
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                # go right
                low = mid + 1

            # elif nums[mid] > target:
            #     high = mid - 1
            else:
                high = mid - 1

        return -1

    def bs_recursive(self, nums: List[int], target: int, low: int, high: int) -> int:
        # base case
        if low > high:
            return -1
        # recurive case
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.bs_recursive(nums, target, mid + 1, high)
        else:
            return self.bs_recursive(nums, target, low, mid - 1)

    def lower_bound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def upper_bound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Return an index of target element from DS
        If element not found in DS than it return the ideal position for element in DS so that DS remain in sorted order
        """
        return self.lower_bound(nums, target)

    def find_floor_and(self, nums: List[int], target: int) -> List[int]:
        """ """
        return []

    def searching_rotated_sorted(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        print(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:

                high = mid - 1

        return -1


def main():
    s = Binary_Search_Solution()
    arr = [4, 5, 6, 7, 0, 1, 2]
    ans = s.searching_rotated_sorted(arr, 0)
    print(ans)


if __name__ == "__main__":
    main()
