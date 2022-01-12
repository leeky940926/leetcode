class Solution:
    def countBinarySubstrings(self, s: str) -> int: 
        cnt = 1
        consecutive_list = []
        result = 0
        
        if len(s) == 1 : return 0
        
        s += " "
        
        for i in range(len(s)-1) :
            if s[i] == s[i+1] :
                cnt += 1
            else :
                consecutive_list.append(cnt)
                cnt = 1

        if len(consecutive_list) == 1 : return 0
        
        for i in range(len(consecutive_list)-1):
            result += min(consecutive_list[i], consecutive_list[i+1])
        return result