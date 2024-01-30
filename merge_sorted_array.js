/*
 * PROBLEM DESCRIPTION:
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 * and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 * Merge nums1 and nums2 into a single array sorted in non-decreasing order.
 *
 * PROBLEM EXAMPLE:
 * Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
 * Output: [1,2,2,3,5,6]
 * Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
 * The result of the merge is [1,2,2,3,5,6]
 * with the underlined elements coming from nums1.
 */

let merge = function(nums1, m, nums2, n) {
  let j = 0
  let val = true
  for(let i = 0; i < nums1.length && j < n; i++){
    if (nums1[i] === 0 && nums1){
      nums1[i] = nums2[j]
      j++
    } else if (nums1[i] !== 0){
      val = false
    }
  }
  nums1.sort((a,b) => a - b)
  return nums1
};
