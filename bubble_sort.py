#Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j+1]:
                arr [j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False:
            break
    
data = [5, 3, 2, 6, 1]
bubble_sort(data)

print("Input data :", data)
print("Output data :", data)
