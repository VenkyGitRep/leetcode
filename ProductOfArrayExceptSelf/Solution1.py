#Turns out, no division was allowed.
from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        output = [1]*count
        answer=[1]*count
        suffix_product=[1]*count
        p=1
        for i in range(count):
            answer[i]=p
            p=p*nums[i]

        p=1
        for i in range(count-1,-1,-1):
            answer[i]=p*answer[i]
            p=p*nums[i]
    

        return answer


if __name__=="__main__":
    print("wassup dawg")
    sol = Solution1()
    output = sol.productExceptSelf([1,2,3,4])

    print(output)