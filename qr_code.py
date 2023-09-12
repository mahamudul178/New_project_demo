
def linear_search(arr , item):
    for i in range (len(arr)):
        if arr[i] == item:
            return i
    return -1
    

arr=[12,34,56,1,67,100,47,99]

res=linear_search(arr, 67)
print(res)


def binary_search(arr,low,high,item):
    if low<=high:
        print("low = " ,low , " high = ", high,end='')
       
        mid=(low+high)//2
        print(" mid value is ",arr[mid])
        if arr[mid]==item:
            
            return mid
        elif arr[mid]>item:
            return binary_search(arr,low,mid-1, item)
        else:
            return binary_search(arr,mid+1,high,item)
    else:
        mid=(low+high)//2
        if arr[mid]==item:
            return mid
        elif arr[mid]>item:
            return binary_search(arr,low,mid-1, item)
        else:
            return binary_search(arr,mid+1,high,item)
arr=[12,34,35,46,57,68,80,99,100]
res=binary_search(arr,0,len(arr)-1,100)
print(res)
res=[]

def bubble_sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            res.append(arr[i])
        else:
            res.append(arr[i])
arr=[12,34,35,11,57,68,62,99,100]
bubble_sort(arr)    
print(res)    

def merge_sort(arr):
    if len(arr)==1:
        return arr
    
    mid =len(arr)//2

    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge_sort(left,right)