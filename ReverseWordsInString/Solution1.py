class Solution1:
    def reverseWords(self, s: str) -> str:
        output_array = s.split()
        num_of_words = len(output_array)
        output=""
        for i in range(num_of_words-1,-1,-1):
            output+=output_array[i]
            if(i>0):
                output+=" "
        return output


if __name__=="__main__":
    sol = Solution1()
    output = sol.reverseWords(" Hellow   world ")
    print(f"start{output}end")
