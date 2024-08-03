# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:27:17 2024

@author: mk9di
"""

#ReverseString

word = input("Input String to reverse: ")

rev =""

#1 - loop
for i in word:
    rev = i + rev
       
print("original: ",word)
print("reversed: ",rev)


#3 - slice
def reverse(st):
    st = st[::-1]
    return "".join(st)
    
pc = "computer"

print("Original: ",pc, )
print("Reversed: ",reverse(pc))

#2 - recurssion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
    
s = "Licence"

print("Original: ",s)
print("Reversed: ",reverse(s))

#4 - list comprehension
def reverse(st2):
    st2 = [st2[i] for i in range(len(st2)-1, -1, -1)]
    return "".join(st2)
    
ss = "automatic"

print("Original: ",ss, )
print("Reversed: ",reverse(ss))
