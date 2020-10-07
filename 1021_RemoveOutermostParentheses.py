class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        found=0
        for i in range(len(S)):
            if not found and S[i]=="(":
                found+=1
            elif found:
                if S[i]=="(":
                    found+=1
                    ans+=S[i]
                else:
                    if found==1:
                        found-=1
                        continue
                    found-=1
                    ans+=S[i]
        return ans