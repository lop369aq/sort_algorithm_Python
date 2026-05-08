#selection_sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        change = False
        for j in range(i+1, n):
            
            if arr[min_index] > arr[j]:
                min_index = j
                change = True
            
        if change:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr  

data = [29, 10, 14, 37, 13]
print("Input data :", data)
print("Output data :", selection_sort(data))