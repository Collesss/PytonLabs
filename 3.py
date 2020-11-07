def encrypt(string):
    
    def convertChar(char):
        char_to_num = {'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'}
        result = char

        if char in char_to_num:
            result = char_to_num[char]
        
        return result
    
    strArr = [convertChar(c) for c in reversed(string)]
    strArr.append('aca')
    
    result = ''.join(strArr)

    return result


print(encrypt("banana"))

print(encrypt("karaca"))

print(encrypt("burak"))

print(encrypt("alpaca"))
