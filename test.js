/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function (nums) {
    let max = -1;
    let secondMax = -1, ans = -1;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > max) {
            secondMax = max;
            max = nums[i];
        } else if (nums[i] < max && secondMax < nums[i]) {
            secondMax = nums[i]
        } else if (nums[i] < secondMax && ans < nums[i]) {
            ans = nums[i];
        }
    }
    console.log(secondMax, max, ans)
    return ans === -1 ? ans : max;
};

console.log(thirdMax([1, 2, 2, 5, 3, 5]))