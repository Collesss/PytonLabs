import math

def sum_primes(nums):
    
    def is_prime(num):
        result = True

        if num != 2:
            if num == 1 or num % 2 == 0:
                result = False
            else:
                sqrtNum = int(math.ceil(math.sqrt(num)))
            
                for i in range(3, sqrtNum+1, 2):
                    if num % i == 0:
                        result = False
                        break
                
        return result

    
    result = 0
    
    for i in nums:
        if is_prime(i):
            result += i
    
    return result


print(sum_primes([1, 2, 3, 1, 5, 1, 7, 1, 9, 10]))

print(sum_primes([2, 3, 4, 11, 20, 50, 71]))

print(sum_primes([]))

