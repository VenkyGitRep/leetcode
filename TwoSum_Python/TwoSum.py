from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    myMap = {}

    for i in range(len(nums)):
        if target - nums[i] in myMap:
            return [myMap[target - nums[i]], i]
        myMap[nums[i]] = i

    return []        
        
if __name__=="__main__":
    print('Yo, wassup')
    print(twoSum([1,2,3,4,5,6,7,8],4))

print('Yo, wassupg')