class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" : return 0
        if haystack == "" : return -1
        
        return haystack.find(needle)