import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def gerar_caso_teste(size):
    return [random.randint(0, 10000) for _ in range(size)]

def main():
    test_sizes = [100, 1000, 5000]
    
    for size in test_sizes:
        arr = gerar_caso_teste(size)
        
        arr_copy = arr.copy()
        start = time.time()
        selection_sort(arr_copy)
        end = time.time()
        selection_time = end - start
        
        arr_copy = arr.copy()
        start = time.time()
        insertion_sort(arr_copy)
        end = time.time()
        insertion_time = end - start
        
        print(f"Tamanho do array: {size}")
        print(f"SelectionSort: {selection_time:.6f} segundos")
        print(f"InsertionSort: {insertion_time:.6f} segundos")
        print("---")

if __name__ == "__main__":
    main()