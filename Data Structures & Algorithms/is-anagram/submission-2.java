class Solution {
    public boolean isAnagram(String s, String t) {
        int[] maskS = new int[26];
        int[] maskT = new int[26];


        for(char c:s.toCharArray()){

            maskS[c - 'a']++;

        }

        for(char c:t.toCharArray()){

            maskT[c - 'a']++;

        }

        return Arrays.equals(maskT,maskS);
    }
}
