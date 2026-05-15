"""Name:Karti Gaikwad
Fourth Day Assignments
15/05/2025"""





#ascending order Bubblesort
"""
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__  == '__main__':
        arr=[6,23,2,4,1,8,56,3]
        bubblesort(arr)
        print(*arr)

        


#descending order Bubblesort
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__  == '__main__':
        arr=[6,23,2,4,1,8,56,3]
        bubblesort(arr)
        print(*arr)
"""





"""Insertion sort ascending order"""
"""
def insertion_sort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current
if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    insertion_sort(arr)
    print(arr)
"""



"""Insertion sort descending order"""
"""
def insertion_sort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current>arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current
if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    insertion_sort(arr)
    print(arr)
"""








#selection sort ascending order
"""
def selectionsort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if min>arr[j]:
                min=arr[j]
                loc=j
        arr[i],arr[loc]=arr[loc],arr[i]
    
if __name__ == '__main__':
    arr=[6,23,2,4,1,8,56,3]
    selectionsort(arr)
    print(*arr)
"""




#descending order
"""
def selectionsort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if min<arr[j]:
                min=arr[j]
                loc=j
        arr[i],arr[loc]=arr[loc],arr[i]
    
if __name__ == '__main__':
    arr=[6,23,2,4,1,8,56,3]
    selectionsort(arr)
    print(*arr)
"""




"""Classes and objects"""
"""
class Student:
    def show(self):
        print("This is a student class")

s=Student();
s.show();
"""




"""Constructor in python"""
"""
class Student:
    def __init__(self):
        print("Default constructor")

    def show(self):
        print("This is a student class")

s=Student();
s.show();
"""


"""STACK"""
"""
import sys
class Stacks:
    def push(self):
        pass
    def pop(self):
        pass
    def traverse(self):
        pass
    def peek(self):
        pass

if __name__ == '__main__':
    obj=Stacks()
    while True:
        print("1. push")
        print("2. pop")
        print("3. traverse")
        print("4. peek")
        print("5. exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
        ele=int(input("Enter data: "))
            obj.push(ele)
        elif ch==2:
            obj.pop()
        elif ch==3:
            obj.traverse()
        elif ch==4:
            obj.peek()
        elif ch==0:
            sys.exit()
"""





"""Stack using self.(this keyword) using capacity """
"""
import sys
class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
    def is_full(self):
        if self.top==self.CAPACITY-1:
            return True
        else:
            return False
    def push(self,ele):
        if self.is_full():
            print("Stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele,"is pushed")

    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele=self.stack[self.top]
            self.stack.pop()
            self.top=-1
            return ele
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]
        print("stack is full")
            
if __name__ == '__main__':
    obj=Stacks()
    while True:
        print("1. push")
        print("2. pop")
        print("3. traverse")
        print("4. peek")
        print("5. exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            ele=int(input("Enter data: "))
            obj.push(ele)
        elif ch==2:
        ele=int(input("Is popped: "))
            obj.pop()
        elif ch==3:
            obj.traverse()
        elif ch==4:
            obj.peek()
        elif ch==0:
            sys.exit()
"""










"""Stack using self.(this keyword) without using capacity"""
"""
import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):
        self.top = self.top + 1
        self.stack.append(ele)
        print(ele, "is pushed")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top = self.top - 1
            return ele

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

    def traverse(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])


if __name__ == '__main__':
    obj = Stacks()

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Traverse")
        print("4. Peek")
        print("5. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            ele = int(input("Enter data: "))
            obj.push(ele)

        elif ch == 2:
            ele = obj.pop()
            if ele is not None:
                print(ele, "is popped")

        elif ch == 3:
            obj.traverse()

        elif ch == 4:
            ele = obj.peek()
            if ele is not None:
                print("Top element is:", ele)

        elif ch == 5:
            sys.exit()
"""








"""reverse an array using stack"""
"""
import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 10
        
    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False
        
    def push(self, ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")
            
    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])
            
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return None
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

if __name__ == '__main__':
    obj = Stacks()
    arr = [234235, 235, 235, 235, 5]

    print("Original array:")
    print(arr)

    for i in range(len(arr)):
        obj.push(arr[i])
    rev = []
    for i in range(len(arr)):
        ele = obj.pop()
        rev.append(ele)

    print("Reversed array: ",rev)
    """