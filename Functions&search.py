"""Name:Karti Gaikwad
Third Day Assignments
14/05/2025"""




"""Functions"""
"""
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    res=a+b
    print("Addition is",res)

if __name__ =='__main__':
    add()
"""








"""Functions with parameters"""
"""
def add(a,b):
    res=a+b
    print("Addition is",res)

if __name__ =='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    add(a,b)
"""







"""Functions with parameters with return"""
"""
def add(a,b):
    res=a+b
    return res

if __name__ =='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r=add(a,b)
    print("Addition is",r)
"""








"""Functions with parameters with return multiple values"""
"""
def add(a,b):
    res=a+b
    res2=a-b
    res3=a*b
    return res,res2,res3

if __name__ =='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r,r2,r3=add(a,b)
    print("Addition is",r)
    print("subtraction is",r2)
    print("Multiplication  is",r3)
"""








"""Linear Search"""
"""
def linearsearch(n,arr,target):
    flag = False

    for i in range(n):
        if target != arr[i]:
            pass
        else:
            flag=True
            loc=i

    if flag==True:
            print("Element found at index: ",loc)
    else:
            print("Element not found")

if __name__  == '__main__':
    n=int(input("Enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        target=int(input("Enter no which is to de searched: "))
        linearsearch(n,arr,target)
"""










"""Binary Search"""
"""
def binarysearch(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            break
        elif target<arr[mid]:
            high=mid-1
        elif target>arr[mid]:
            low=mid+1
    if flag==True:
        print("Element found at index: ",mid)
    else:
        print("Element not found")
    
if __name__  == '__main__':
    n=int(input("Enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    target=int(input("Enter no which is to de searched: "))
    binarysearch(n,arr,target)
"""