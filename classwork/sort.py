array = [5,1,6,2,4,3]

array2 = [8,1,6,4,3,9]
def bubble(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) -i -1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

bubble(array)
print(bubble(array2))