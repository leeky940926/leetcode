class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1] : return True
        
        idx = 0
        
        while idx < len(s)/2 and s[idx] == s[-idx-1] :
            idx +=1
        
        s = s[idx:len(s)-idx]
        
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]