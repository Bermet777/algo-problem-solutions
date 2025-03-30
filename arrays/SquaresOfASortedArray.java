// Solution from LC solutions section, time complexity O(n);

class Solution {
  public int[] sortedSquares(int[] nums) {
      int[] squares = new int[nums.length];
      int left = 0;
      int right = nums.length - 1;
      for (int i = nums.length - 1; i >= 0; i--) {
          if (Math.abs(nums[left]) > Math.abs(nums[right])) {
              squares[i] = nums[left] * nums[left];
              left++;
          }
          else {squares[i] = nums[right] * nums[right];
              right--;
              }
      }
      return squares;
  }
}

