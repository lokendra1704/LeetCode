class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            temp = ""
            for j in i:
                temp+=l[ord(j)-ord('a')]
            ans.add(temp)
        return len(ans)