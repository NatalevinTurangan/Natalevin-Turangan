def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # pertukaran
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Tukar elemen 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # tidak ada pertukaran
        if not swapped:
            break
    return arr

# penggunaan
angka = [4, 7, 10, 8, 3, 5, 1, 6, 9, 2]
print("angka sebelum diurutkan:", angka)
print("angka setelah diurutkan:", bubble_sort(angka))

