#функция кодирования строки
def encrypt(string):
    
    #функция замены символа, алгоритм её работы следующий если символ переданный в аргументе есть в ключах словаря то функция возвращает символ из словаря по ключу аргумента, иначе возвращается сам аргумент
    def convertChar(char):
        char_to_num = {'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'}
        result = char

        if char in char_to_num:
            result = char_to_num[char]
        
        return result
    
    #создание списка символов с их заменой функцией "ConvertChar" в обратной последовательности с помощью генератора списка и функции "reversed" для изменения порядка следования элементов в списке 
    strArr = [convertChar(c) for c in reversed(string)]
    #добавление строки 'aca' в конец списка "strArr"
    strArr.append('aca')
    #объединение списка в единую строку с разделителем '' с помощью метода "join" класса "String"
    result = ''.join(strArr)

    return result


print(encrypt("banana"))

print(encrypt("karaca"))

print(encrypt("burak"))

print(encrypt("alpaca"))
