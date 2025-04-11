# Program QuickSort dan Binary Search
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Contoh penggunaan
arr_angka = [12, 4, 7, 9, 3, 15, 8, 6]
print("Array sebelum diurutkan:", arr_angka)
arr_terurut = quicksort(arr_angka)
print("Array setelah diurutkan:", arr_terurut)

target_angka = 9
hasil = binary_search(arr_terurut, target_angka)
if hasil != -1:
    print(f"Elemen {target_angka} ditemukan pada indeks {hasil}")
else:
    print(f"Elemen {target_angka} tidak ditemukan.")
