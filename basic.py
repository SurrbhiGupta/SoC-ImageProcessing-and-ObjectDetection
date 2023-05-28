# x = input()
# n=int(x)
# sum_even=0
# sum_odd=0
# for i in x:
#     if int(i)%2==0:
#         sum_even+=int(i)
#     else:
#         sum_odd+= int(i)

# print(sum_even, sum_odd)


#  fibonacci series
# s=[1,1]
# for i in range(n):
#     s.append(s[i]+s[i+1])
# print(s)    
# print(s[n-1])

# shape of array
# import numpy as np
# x=np.array([[2,3,4,5],[1,2,3,1],[5,4,3,4]])
# y=np.array([6,5,4])
# print(x.shape[0])

# patterns
# for i in range(n):
#     print('*'*n)
# for i in range(1,n+1):
#     print(f'{i}'*n) 
    



# n = int(input())

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i, end = '')
#     print()
    
# for i in range (1,n+1):
#     for j in range(1,n+1):
#         print(j, end='')
#     print()

# for i in range (1,n+1):
#     for j in range(1,n+1):
#         print(n+1-j,end='')
#     print()
    

# 1 12 123 1234
# s=''
# for j in range(1,n+1):
#     s+=(f'{j}')
#     print(s, end=' ')
    
# 1 23 345 4567
# s=''
# for i in range(1,n+1):
#     for j in range(i,i+i):
#         print(j, end='')        
#     print()

# 1 23 456 78910
# p=1
# for i in range(1,n+1):
#     j=1
#     while j<=i:
#         print(p, end='')       
#         p=p+1 
#         j=j+1
#     print()

# ABCD ABCD ABCD ABCD
# for i in range(1, n+1):
#     for j in range(n):
#         print(chr(65+j), end='')
#     print()

# ABCD BCDE CDEF DEFG
# for i in range(n):
#     for j in range(n):
#         print(chr(65+j+i), end='')
#     print()

# 1 11 111 1111
# for i in range(1,n+1):
#     print(f'1'*i)
# for i in range(1,n+1):
#     for j in range(i):
#         print(1, end='')
#     print()
    
# 1 11 202 3003 40004 500005
# for i in range (0, n):
#     if i==0:
#         print(1)
#     else:
#         s=i*10**i+i
#         print(s)


# 1 11 121 1221 12221
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         if i==1 and j==i:
#             print(1, end = '')
#         elif j == 1 or j == i:
#             print(1, end = '')
#         else:
#             print(2, end = '')
#         j = j + 1
#     print()
#     i = i + 1
    
    
    
#     *
#    **
#   ***
#  ****
# *****
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)
    
#     1
#    12
#   123
#  1234
# 12345
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print(f'{j}', end='')
#     print()
    
    
#     1
#    121
#   12321
#  1234321
# # 123454321
# for i in range(1, n+1):
#     for s in range(n-i):
#         print(' ', end='')
#     p=1
#     for j in range(1,i+1):
#        print(j, end='')
#        p+=1
#     for k in range(p-2,0,-1):
#         print(k, end='')
#     print()

# ****
# ***
# **
# *
# for i in range(0, n):
#     print('*'*(n-i))

# for i in range(n):
#     for j in range(n-i):
#         print('*', end='')
#     print()


# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
# for i in range(1,n+1,1):
#     for j in range (1,i+1,1):
#         print(j,end="")
#     for s in range(0,(2*n-2*i)):
#         print(" ",end="")
#     for n2 in range (i,0,-1):
#         print(n2,end="")

#     print()

# 11111
# 0000
# 111
# 00
# 1
# for i in range(n):
#     for j in range(n-i):
#         if i%2==0:
#             print(1, end='')
#         else:
#             print(0, end='')           
#     print()

# 1234
#  234
#   34
#    4
#   34
#  234
# 1234
# for i in range(1,2*n):
#     for j in range(i,n-i):
#         print(j, end='')
#     for s in range(i):
#         print(' ', end='')
#     for k in range(n-i,0,-1):
#         print(k, end='')
#     print()



# factorial NCR
# r=2
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n_fact = fact(n)
# r_fact = fact(r)
# r_n_fact = fact(n-r)
# print(n_fact/(r_fact*r_n_fact))



# is prime
# def isprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         return True
#     return False
# # if isprime(n):
# #     print(f"{n} is a prime number")
# # else:
# #     print(f"{n} is not a prime number")    

# for k in range(2,n+1):
#     if isprime(k):
#         print(k)   
  
  
        
# global variable
# a=3
# def gar():
#     global a
#     a=4
#     print(a)
# print(a) #3
# gar()  #4
# print(a) #4



# Armstrong number 153, 3digits, if 1^3+5^3+3^3 = 153        
# def arm(n):
#     for i in range(1,n+1):
#         sum=0
#         num = i
#         l=len(str(i))
#         for j in range(1,l+1):
#             c = num%10  
#             sum += c**l
#             num = num//10
#         if i==sum:
#             print(i)       
# arm(n)

# fibonacci
# def fib(n):
#     s=[1,1]
#     for i in range(n):
#         s.append(s[i]+s[i+1])
#     return s
# s=fib(n)
# print(n in s )


# pallindrome
# def pallin(n):
#     sum=0
#     while n>0:
#        c =n%10
#        sum = sum*10+c  
#        n = n//10
#     return sum
# print(n==pallin(n))

# print(n==int((str(n))[::-1])) #easy

# for errors    
# try:
#     x=int(input())
#     print(x)
# except ValueError:
#     print("invalid value")

# emoji   win+; keys
# z={":)":"😊"}
# print(z[":)"])


# for swapping items in list
# def swap():
#     x = int(input())
#     for i in range(x):
#         n = int(input())
#         a = [int(i) for i in input().split()]
#         for i in range(n):
#             if i%2==0:
#                 c = a[i]
#                 a.remove(a[i])
#                 a.insert(i+1, c)
#         print(a)
# swap() 
    
# find no repeating values
# import numpy as np
# x = int(input())
# for i in range(x):
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     b = sorted(a)
#     unique=[]
#     for j in range(n):
#         if a[j] not in unique:
#             unique.append(a[j])
#     print(unique)
#     print(np.unique(a))
#     print(np.sort(a))
#     print(a)

# pair=x    
# x = int(input())
# l = [int(i) for i in input().split()]
# c = 0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==x:
#             c += 1
# print("no. of pairs: ",c)

# triplets = sum
# t=int(input())
# for g in range(t):
#     n = int(input())
#     l = [int(i) for i in input().split()]
#     x = int(input())
#     c = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1, n):
#                 if l[i]+l[j]+l[k]==x:
#                     c += 1
#     print("no. of triplets : ", c)   


# sorting 0 1 array
# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split(' ')))
#     a.sort()
#     print(a)

# find unique element in a list
# n = int(input())
# l = [int(i) for i in input().split()]
# def unique(n, l):
#     l.sort()
#     k=0
#     for i in range(len(l)):
#         i=k
#         if l[i]==l[i+1]:
#             l.remove(l[i])
#             l.remove(l[i])
#             if len(l)==1:
#                 break
#         else:
#             k=k+1
#     for i in l:
#         print(i)
# unique(n,l)   

# linear search
# def search(n,l,t):
#     for j in range(t):
#         x = int(input())
#         for i in range(n):
#             if l[i]==x:
#                 print(i) 
#         if x not in l:
#                 print(-1)  


# binary search
# n = int(input())
# l = [int(i) for i in input().split()]
# t = int(input())
# search(n,l,t)   
# for j in range(t):
#     x = int(input())    
#     start = 0
#     end = n-1
#     while start<=end:
#         mid=(start+end)//2
#         if l[start]==x:
#             print(start)
#             break
#         elif l[end]==x:
#             print(end)  
#             break
#         elif l[mid]==x:
#             print(mid) 
#             break
#         elif  x<l[mid] :
#             end=mid-1 
#             start=start
#         elif x>l[mid]:
#             start=mid+1   
#             end=end  
#     else:
#         print(-1)        
    
# unique    
# l.sort()
# j=0
# for i in range(len(l)):
#     i=j
#     if l[i]==l[i+1]:
#         l.remove(l[i]) 
#         l.remove(l[i])
#         if len(l)==1:
#             break    
#     else:
#         j+=1
# for i in l:
#     print(i)

# maximum value
# def maxx(li):
#     l=li.copy()
#     k=0
#     for i in range(len(l)):
#         i=k
#         if l[i]>l[i+1] or l[i]==l[i+1]:
#             l.remove(l[i+1])
#             if len(l)==1:
#                 break
#         elif l[i]<l[i+1]:
#             l.remove(l[i])
#             if len(l)==1:
#                 break
#     return l[0]
    
# minimum value
# def minn(li):
#     l=li.copy()
#     k=0
#     n=len(l)
#     for i in range(n-1):
#         i=k
#         if l[i]>=l[i+1]:
#             l.remove(l[i])
#             if len(l)==1:
#                 break
#         elif l[i]<l[i+1]:
#             l.remove(l[i+1])
#             if len(l)==1:
#                 break
#     return l[0]
            

# # sorting of list
# n = int(input())
# li = [int(i) for i in input().split()]
# sorted=[]
# for i in range(n):
#     sorted.append(minn(li))
#     li.remove(min(li))
# print(sorted)


# rotate array
# n = int(input())
# l = list(int(i) for i in input().split())
# r=int(input())
# for i in range(r):
#     p=l.pop()
#     l.insert(0,p)
# for i in l:
#     print(i, end=' ')

# check array rotation
# li=l.copy()
# li.sort()
# i=0
# k=0
# while l!=li:
#     d = l[0]
#     l.remove(l[0])
#     l.append(d)
#     k+=1
# print(k)
# print(l)
# import random
# class Dice:
#     def roll(self):
#         print((random.randint(1,6), random.randint(1,6)))
        
            
# Dice().roll()
# import openpyxl as xl

# d = xl.load_workbook("P:\DSA practice\Python Tutorial Supplementary Materials\transactions.xlsx")

import cv2 as cv
img = cv.imread("P:\\DSA practice\\images\\cat.jpg")
cv.imshow('cat', img)
cv.waitkey(0)