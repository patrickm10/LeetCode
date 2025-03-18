class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Remove leading and trailing spaces
        if not s:
            return False
        
        has_digit = has_dot = has_exponent = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                has_digit = True 
            
            elif c == '.':
                if has_dot or has_exponent:
                    return False
                has_dot = True
            
            elif c in 'eE':
                if has_exponent or not has_digit:
                    return False
                has_exponent = True
                has_digit = False  
                
            elif c in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            
            else:
                return False 
        
        return has_digit 

