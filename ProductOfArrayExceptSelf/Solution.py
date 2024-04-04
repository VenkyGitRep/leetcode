from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        if(nums.count(0)>1):
            output = [0]*len(nums)
        elif(nums.count(0)==1):
            p=1
            for i in range(len(nums)):
                if(nums[i]!=0):
                    p=p*nums[i]
            output = [0]*len(nums)
            index_of_zero = nums.index(0)
            output[index_of_zero]=p
        else:
            p=1
            for i in range(len(nums)):
                p=p*nums[i]
            output = nums
            for i in range(len(output)):
                output[i]=int(p/output[i])
        return output


if __name__=="__main__":
    print("wassup dawg")
    sol = Solution()
    output = sol.productExceptSelf([-1,1,1,-3,3])

    print(type(output[0]))