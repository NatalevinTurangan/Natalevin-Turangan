def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Pindahkan elemen 
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# penggunaan
angka = [7, 3, 6, 2, 1, 5, 4]
print("angka sebelum diurutkan:", angka)
print("angka setelah diurutkan:", insertion_sort(angka))
