from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1 : return strs[0]
        
        if "" in strs : return ""
        
        strs.sort(key=len)
        
        for i in range(len(strs[0])) :
            for j in range(1, len(strs)) :
                if strs[0][i] != strs[j][i] :
                    return strs[0][:i]
        return strs[0]