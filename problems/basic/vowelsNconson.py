def vowelsNconson(arr):
    even=[]
    odd=[]

    for index in range(0,len(arr)):
        element =arr[index]
        if(element%2 ==0):
            even.append(element)
        else:
            odd.append(element)
    print(even)
    print(odd)            
     
a=[1,2,3,4,5]
vowelsNconson(a)
