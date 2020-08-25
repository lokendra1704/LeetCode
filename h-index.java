/**
Speed:              40.45%
Memory:             21.29%
Time Complexity:    O(n)
*/
import java.util.Arrays;
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int count = 0;
        for (int i=n-1;i>=0;--i){
            if (citations[i]<n-i)
                break;
            else
                ++count;
        }
        return count;   
    }
}