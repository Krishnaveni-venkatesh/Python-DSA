
 

def findMaxElement(arr):
    maxElement = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>maxElement):
            maxElement = arr[i]
    print(f"the max element is :{maxElement}")

myarr = [3,6,20,12,32,8]
findMaxElement(myarr)


