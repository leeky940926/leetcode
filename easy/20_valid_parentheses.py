class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1 : return False
        if len(s)==0 : return False
        
        str_dic = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        v_list = []  

        for i in s :
            if i in str_dic.values() :
                v_list.append(i)
            
            else :
                if v_list and v_list[-1] == str_dic[i] :
                    v_list.pop()
                    
                else : return False
        
        if v_list : return False
        
        return True 