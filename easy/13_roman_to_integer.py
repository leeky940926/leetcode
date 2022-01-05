class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        sum = 0
        current_value = rom_dic[s[0]]
        
        for i in range(1,len(s)) :
            if current_value >= rom_dic[s[i]] :
                sum += current_value
            
            else : sum -= current_value
            
            current_value = rom_dic[s[i]]
            
        return sum + rom_dic[s[-1]]