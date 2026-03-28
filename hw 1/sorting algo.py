def sort_algo(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


for i in range(3):
    arr = list(map(int, input("Input array: ").split()))
    print("Sorting the array...")
    sort_algo(arr)
    print("Here is your sorted array: ", arr)