# Bubble Sort implementation in Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example: Sort product prices
product_prices = [45, 23, 67, 12, 89, 34]

print("Original product prices:", product_prices)

# Sorting the prices using bubble sort
sorted_prices = bubble_sort(product_prices)

print("Sorted product prices:", sorted_prices)
