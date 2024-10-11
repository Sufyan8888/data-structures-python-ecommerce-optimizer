# Quick Sort implementation in Python

def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1  # Pointer for greater element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Move pointer for smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition index

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example: Sort product ratings
product_ratings = [4.5, 2.8, 4.9, 3.7, 1.2, 4.1]

print("Original product ratings:", product_ratings)

# Sorting the ratings using quick sort
quick_sort(product_ratings, 0, len(product_ratings) - 1)

print("Sorted product ratings:", product_ratings)
