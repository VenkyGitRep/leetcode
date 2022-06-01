package Day1;

class Solution {
    public int[] runningSum(int[] nums) {
        int[] runningSum = new int[nums.length];
        int currentSum = 0;

        for(int i=0;i<nums.length;i++){
            currentSum=currentSum+nums[i];
            runningSum[i]=currentSum;
        }

        return runningSum;
    }
    public static void main(String[] args){
        int[] nums = {1,2,3,4,5};
        int[] runningSum = new Solution().runningSum(nums);
        for(int num : runningSum){
            System.out.print(num+" ");
        }
        System.out.println();
    }
}