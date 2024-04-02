package TwoSum;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> myMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            if (myMap.containsKey(target - nums[i])) {
                return new int[] { myMap.get(target - nums[i]), i };
            }
            myMap.put(nums[i], i);
        }
        return null;
    }
}