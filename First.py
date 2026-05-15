"""Name:Karti Gaikwad
First Day Assignments
12/05/2025"""


""" Find last digit number"""
"""
no = int(input("Enter no:  "))
res = no%10
print(res)
"""







"""sum of 2 digit"""
"""
no = int(input("Enter no= "))
n1=no%10
n2=no//10
res=n1+n2
print(res)
"""





"""sum of 3 digit"""
"""
no = int(input("Enter no: "))
n1 = no%10
no= no//10 
n2 = no%10
no = no//10
n3= no%10
res=n1+n2+n3
print(res)
"""







"""sum of 5 digit"""
"""
no = int(input("Enter no: "))
n1 = no%10
no = no//10
n2 = no%10
no = no//10
n3 = no%10
no = no//10
n4 = no%10
no = no//10
n5 = no%10
res = n1+n2+n3+n4+n5
print(res)
"""







"""Reverse of 3 digit number"""
"""
no = int(input("Enter no: "))
n1= no%10
no= no//10
n2= no%10
no= no//10
n3= no%10
rev = n1*100+n2*10+n3*1
print(rev)
"""








"""rev any no"""
"""
no = int(input("Enter no: "))
rev = 0
while no >0:
    rem = no%10
    rev = rev*10+rem
    no = no//10

    print(rev)
    """







"""count of numbers"""
"""
no = int(input("Enter no: "))
count = 0
while no>0:
    no= no//10
    count = count+1
    print(count)
    """






"""sum of digiits"""
"""
no= int(input("Enter no: "))
sum = 0
while no>0:
    rem = no%10
    sum = sum + rem
    no = no//10
    print(sum)
    """







"""factorial of number"""
"""
no = int(input("Enter no: "))
fact = 1
while no>0:
    fact = fact*no
    no = no-1
    print(fact)
    """









"""plaindrome"""
"""
no = int(input("Enter no: "))
rev = 0
save = no
while no >0:
    rem = no%10
    rev = rev*10+rem
    no = no//10

if rev == save:
    print("plaindrome")
else:
    print("not palindrome")
    """









"""Armstrong normal"""
"""
no = int(input("Enter no: "))
sum = 0
count = 0

save = no

# count digits
while no > 0:
    no = no // 10
    count = count + 1

no = save

# armstrong calculation
while no > 0:
    rem = no % 10
    sum = sum + (rem ** count)
    no = no // 10

# final check
if sum == save:
    print("armstrong")
else:
    print("not armstrong")
    """








"""Armstrong number for loop"""
"""
for i in range(1, 10001):

    no = i
    sum = 0
    count = 0

    save = no

    # count digits
    while no > 0:
        no = no // 10
        count = count + 1

    no = save   

    # armstrong calculation
    while no > 0:
        rem = no % 10
        sum = sum + (rem ** count)
        no = no // 10

    # final check
    if sum == save:
        print("armstrong", i)
        """



"""peterson  number"""
"""
no = int(input("Enter no: "))

sum = 0
save = no
fact = 1

while no > 0:
    rem = no % 10

    while rem > 0:
        fact = fact * rem
        rem = rem - 1
    sum = sum + fact
    no = no // 10

if sum == save:
    print("Peterson number")
else:
    print("Not Peterson number")
    """








"""max using conditional statement"""
"""
n1 = 10
n2 = 20
n3 = 30
max=n1
if max <n2:
    max=n2
if max <n3:
    max=n3
print(max)
"""





"""even and odd if and else"""
"""
no = int(input("Enter no: "))
if no%2==0:
    print(no,"is even")
else:
    print(no,"is odd")
    """







"""elif(else if) ladder"""
"""
per= int(input("Enter no: "))
if per>=40 and per<=60:
    print("Take addmission in ABC college")
elif per>=61 and per<=80:
    print("Take addmission in xyz college")
elif per>=81 and per<=100:
    print("taek addmission in pqr college")
    """






"""Questions using conditional statemnet"""
"""
cp= int(input("Enter cost price: "))
st= (input("Are you student: "))
if st=="yes":
    if cp>500:
        ds=cp *0.10
    else:
        ds=cp* 0.5
else:
    if cp>500:
        ds = cp *0.8
    else:
        ds= cp *0.2
fd= cp-ds
print("Netamount: ",fd)
"""






"""for loop using arr"""
"""
arr=[1,2,3,4,5,5]
for i in range(len(arr)):
    print(arr[i])
for x in arr:
    print(x)
    """








""" Patters using conditional statement"""
"""
i =1
j=10
while i<j:
    if i ==3:
        i = i+1
        j = j-1
        continue 
    print(i,"\t",j)
    i = i+1
    j = j-1
"""






"""list"""
"""
ls=[]
print(type(ls))
ls=list()
arr=[1,2,3,34,77,88]
print(ls)
for i in range(len(arr)):
    print(arr[i],end=" ")

print()

for x in arr:
    print(x,end=" ")
    """







"""array"""
"""
arr=[11,22,33,44,55,66,77,88]
print(arr[3])
print(arr[0:5])
print(arr[:6])
print(arr[4:])
print(arr[:])
print(arr[::])
print(arr[::1])
print(arr[::2])
print(arr[::-1])
print(arr[::-2])
"""






"""array min max"""
"""
arr=[5,3,9,2,8]
max = arr[0]
min = arr[0]
for i in range(1,len(arr)):
    if max < arr[i]:
        max = arr[i]
    if min > arr[i]:
        min = arr[i]

print("Max:", max)
print("Min:", min)
"""




"""Remove duplicates from unsorted array"""
"""
arr=[5,3,9,2,3,5]
newarray=[]
for i in arr:
    if i not in newarray:
        newarray.append(i)
print(newarray)
"""
