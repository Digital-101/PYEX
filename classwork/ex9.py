#1
for i in range(1,5):
    for j in range(1):
        print()
        print(i, end=' ')
    print()

print('-----------------------------')

#2 pattern
for k in range(1,5):
    for l in range(k):
        print(k, end=' ')
        l-=1
    print()

for q in range(1, 5):
     print(' '.join([str(q)] * q))


