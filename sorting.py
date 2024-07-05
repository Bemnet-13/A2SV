def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j]  < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
 
def insertion_sort(arr):
    for i in range(len(arr) - 1):
        j = i
        while j >= 0:
            if arr[j + 1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
            else:
                break
            j -= 1        

def counting_sort(arr):
    max_val = max(arr)
    freq_arr = [0] * (max_val + 1)
    for i in arr:
        freq_arr[i] += 1
    
    
    i = 0
    while i < len(arr):
        for j in range(len(freq_arr)):
            k = freq_arr[j]
            if freq_arr[j] != 0:
                while k > 0:
                    arr[i] = j
                    i += 1
                    k -= 1
    


arr = [10,5,4,3,2,1,4,2,3,4,2,2,3,1,1,2,1,9]
counting_sort(arr)
print(arr)
