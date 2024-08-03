#############################################BE
#1
print("Hello, World")

#2
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(f"Sum: {num1+num2}")
print(f"Difference: {num1-num2}")
print(f"Product: {num1*num2}")
print(f"Quotient: {num1/num2}")

#3
userNum = int(input("Enter a number to check Odd/Even?: "))
if userNum % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#4
list = [4, 6, 3, 10, 27]
print(list)
print(len(list))
print(max(list))
print(min(list))
print(sum(list))

#5
n = int(input("Enter n numbers to be printed in fibonacci: "))
i = 0
j = 1
fib = i+j
for k in range(n):
    print(f"{i}, {j}, {fib}, end=' '")
    fib+=k

#6
numb = int(input("Enter a number for factoril!:"))
fact = numb
for l in range(numb,0,-1):
    print(f"{fact*(l-1)}, end=' '")

#############################################IE
#1
userString = input("Enter a string to check palindrome:")
rev = [userString]

if rev.reverse() == userString or userString == rev:
    print("String is palindrome:")
else:
    print("String is not palindrome: ")

#2
user_number = int(input("Enter a number to check prime: "))

def prime(num):
    if num % 2:
        print(True)
        prime 

#5
dicti = {"Sma":24, "Sue":18, "Sli":26}
print(dicti.keys())
print(dicti.values())
dicti.update({"Halala":19})
dicti.pop('Sma')
print(dicti.keys())

#############################################AE