#1
fruits = ["apples", "bananas", "oranges"]
for fruit in fruits:
    print(fruit)

#2 
fruits.append("peach")

#3
print(fruits[0])
print(fruits)

#5 print 1111 2222 4444 using nested loops
for i in range(1,4):
    for j in range(4):
        print(i, end=' ')
    print()

#6 calculate area of a rectangle
length = 6
breadth = 3

area = length * breadth
print(f"{area}cm\u00b2")

#
string = input("Enter a string: ")
if len(string) < 5:
        print("Short")
elif len(string) > 5:
        print("Long")
else:
        print("Medium")
 
#using a for loop
list1 = ["Hello", "I", "love" "Python","Coding"]

for a in list1:
    if len(a) < 5:
        print(f"{a}: Short")
    elif len(a) > 5:
        print(f"{a}: Long")
    else:
        print(f"{a}: Medium")
 
