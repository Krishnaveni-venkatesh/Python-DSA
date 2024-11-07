def largest_num(numbers):
    largest=numbers[0]
    for num in numbers:
        if(num>largest):
            largest=num
    return largest
num=input("enter the list:")
numbers=list(map(int,num.split()))#map function converts each input to integer
print(largest_num(numbers))
            

        

