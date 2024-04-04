class Solution:
    def reverseWords(self, s: str) -> str:
        i=len(s)-1
        j=len(s)-1
        output=""
        while(i>=0):
            if(s[i]==' '):
                if j>i:
                    output+=s[i+1:j+1]
                while(s[i]==' '):
                   i=i-1
                #Add space only if not traling or leading space
                if(output!="" and i>=0):
                        output+=" "
                j=i
            elif i==0:#i reaches 0
                if(j>=i):
                    output+=s[i:j+1]
                i=i-1

            else:#character encountered
                i=i-1
   
        return output


if __name__=="__main__":
    sol = Solution()
    output = sol.reverseWords(" Hellow world ")
    print(f"start{output}end")
