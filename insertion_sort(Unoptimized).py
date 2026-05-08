#insertion_sort (Unoptimized)

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        for j in range(i-1, -1, -1):
            if key < arr[j]:
                arr[j+1] = arr[j]

                if j == 0:
                    arr[0] = key
            else:
                arr[j+1] = key
                break
        
        
    
    return arr
        
data = [5, 3, 4, 1, 2]
print("Input data : ", data)
print("Output data : ", insertion_sort(data))

