"""
Sorting Algorithms in Python
الگوریتم‌های مرتب‌سازی در پایتون
"""


def bubble_sort(arr):
    """
    Bubble Sort - مرتب‌سازی حبابی
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Selection Sort - مرتب‌سازی انتخابی
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Insertion Sort - مرتب‌سازی درجی
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Merge Sort - مرتب‌سازی ادغامی
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Quick Sort - مرتب‌سازی سریع
    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n)
    """
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr, low, high):
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pivot_idx - 1)
        _quick_sort_helper(arr, pivot_idx + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr):
    """
    Heap Sort - مرتب‌سازی هرمی
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

    return arr


def _heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


def counting_sort(arr):
    """
    Counting Sort - مرتب‌سازی شمارشی
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k)
    Note: Works only for non-negative integers.
    """
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)
    return result


def radix_sort(arr):
    """
    Radix Sort - مرتب‌سازی پایه‌ای
    Time Complexity: O(nk) where k is the number of digits
    Space Complexity: O(n + k)
    Note: Works only for non-negative integers.
    """
    if not arr:
        return []
    arr = arr.copy()
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample)
    print("Bubble Sort:   ", bubble_sort(sample))
    print("Selection Sort:", selection_sort(sample))
    print("Insertion Sort:", insertion_sort(sample))
    print("Merge Sort:    ", merge_sort(sample))
    print("Quick Sort:    ", quick_sort(sample))
    print("Heap Sort:     ", heap_sort(sample))
    print("Counting Sort: ", counting_sort(sample))
    print("Radix Sort:    ", radix_sort(sample))
