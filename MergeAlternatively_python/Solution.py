class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=""
        i=0;j=0
        while(i<len(word1) and j<len(word2) ):
            output+=word1[i]
            output+=word2[j]
            i+=1
            j+=1
        output+=word1[i:]
        output+=word2[j:]
        return output
        

        

if __name__=="__main__":
    print("Main man")
    sol = Solution()
    print(sol.mergeAlternately("111113333333333333","2222222222"))

