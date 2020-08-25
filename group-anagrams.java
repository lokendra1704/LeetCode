/**
Speed: 79.70%
Memory:
Time Complexity: O(n*m + n*logn) (where n is size of the String array and m is size of the largest word)
*/
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs==null){
            return new ArrayList<>();
        }
        HashMap<String,List<String>> ans = new HashMap<String,List<String>>();
        for (String s: strs){
            char[] temp = new char[26];
            for(int i=0;i<s.length();i++)
                temp[s.charAt(i)-'a']++;
            String keystr = String.valueOf(temp);
            if (!ans.containsKey(keystr))
                ans.put(keystr,new ArrayList<String>());
            ans.get(keystr).add(s);
        }
        return new ArrayList<>(ans.values());
    }
}