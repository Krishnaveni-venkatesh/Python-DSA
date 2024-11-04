def numbers(a,b):
    return a+b
num=numbers(2,3)
print(num)

def sum_list(numbers):
    total = 0  
    for num in numbers:  
        total += num 
    return total  


print(sum_list([1, 2, 3, 4, 5]))  

def greet(a,b=2):
    return a*b
multiply=greet(5,3)
print(multiply)