#Nested Loops
#1 rows and 2 columns
for a in range(1,2):
    for b in range(2):
        print(a, end=' ')

#3
rows = 3
#3rows and 2 columns
for m in range(1, rows + 1):
    #cols
    for n in range(2):
        print(m, end=' ')
    print()
    #print(f"----------{m+1}----------")

for i in range(1,4):
    for j in range(3):
        for k in range(2):
            print(f"i: {i}, j: {j}, k: {k}")
            #length -> 6

#7 rows and 12 columns
for c in range(1,8):
    for d in range(12):
        print(c, end=' ')
    print()

#write a nested loop to print the multiplication table of 2 and 3
for e in range(2,4):
    for f in range(1,4):
        ans = e*f
        print(f"{e} x {f} = {ans}")

#write a nested loop to print the multiplication table of 4 and 8
for g in range(4,9,4):
    for h in range(1,5):
        print(f"{g}x{h}={g*h}")

#print 123456789 using nested loops
s = 1
for o in range(1,4):
    for p in range(3):
        print(s, end=' ')
        s+=1
    print()

#print * 9 using nested loops
for o in range(3):
    for p in range(3):
        print('*', end=' ')
    print()