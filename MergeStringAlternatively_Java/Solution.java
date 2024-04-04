package MergeStringAlternatively_Java;


class Solution{
    public String mergeAlternately(String word1, String word2) {
        StringBuffer a = new StringBuffer();
        int w1 = word1.length();
        int w2 = word2.length();
        int i=0,j=0;
        for(;i<w1 && j<w2; i++,j++){
            a.append(word1.charAt(i));
            a.append(word2.charAt(j));
        }
        
        a.append(word1.substring(i));
        a.append(word2.substring(j));

        return a.toString();
    }

    public static void main(String[] args){
        System.out.println("Yolo");
        Solution sol = new Solution();
        System.out.println(sol.mergeAlternately("aceg","bdf"));
    }
}
