# الگوریتم‌های مرتب‌سازی در پایتون | Sorting Algorithms in Python

این ریپازیتوری شامل پیاده‌سازی الگوریتم‌های رایج مرتب‌سازی به زبان پایتون است.

This repository contains Python implementations of common sorting algorithms.

---

## فهرست الگوریتم‌ها | List of Algorithms

| الگوریتم | Algorithm | پیچیدگی زمانی (میانگین) | Time Complexity (avg) | پیچیدگی فضایی | Space Complexity |
|---|---|---|---|---|---|
| مرتب‌سازی حبابی | Bubble Sort | O(n²) | O(n²) | O(1) | O(1) |
| مرتب‌سازی انتخابی | Selection Sort | O(n²) | O(n²) | O(1) | O(1) |
| مرتب‌سازی درجی | Insertion Sort | O(n²) | O(n²) | O(1) | O(1) |
| مرتب‌سازی ادغامی | Merge Sort | O(n log n) | O(n log n) | O(n) | O(n) |
| مرتب‌سازی سریع | Quick Sort | O(n log n) | O(n log n) | O(log n) | O(log n) |
| مرتب‌سازی هرمی | Heap Sort | O(n log n) | O(n log n) | O(1) | O(1) |
| مرتب‌سازی شمارشی | Counting Sort | O(n + k) | O(n + k) | O(k) | O(k) |
| مرتب‌سازی پایه‌ای | Radix Sort | O(nk) | O(nk) | O(n + k) | O(n + k) |

---

## توضیحات الگوریتم‌ها | Algorithm Descriptions

### ۱. مرتب‌سازی حبابی (Bubble Sort)

**توضیح فارسی:**
در این الگوریتم، در هر گذر از آرایه، عناصر مجاور با هم مقایسه می‌شوند و اگر ترتیب درستی نداشته باشند، جابجا می‌شوند. این عمل مانند بالا آمدن حباب در آب است. این الگوریتم برای آرایه‌های کوچک یا تقریباً مرتب مناسب است.

**English:**
In each pass through the array, adjacent elements are compared and swapped if they are in the wrong order. The largest unsorted element "bubbles up" to its correct position with each pass. Best suited for small or nearly sorted arrays.

```python
def bubble_sort(arr):
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
```

---

### ۲. مرتب‌سازی انتخابی (Selection Sort)

**توضیح فارسی:**
در هر مرحله، کوچک‌ترین عنصر باقیمانده در بخش مرتب‌نشده پیدا شده و با اولین عنصر آن بخش جابجا می‌شود. این الگوریتم تعداد جابجایی‌های کمی دارد اما مقایسه‌های زیادی انجام می‌دهد.

**English:**
In each step, the minimum element from the unsorted portion is found and placed at the beginning of the unsorted section. It minimizes the number of swaps but still performs O(n²) comparisons.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

---

### ۳. مرتب‌سازی درجی (Insertion Sort)

**توضیح فارسی:**
هر عنصر از آرایه برداشته می‌شود و در جایگاه صحیح خود در بخش مرتب‌شده قرار می‌گیرد، مانند مرتب کردن کارت‌های بازی در دست. برای آرایه‌های کوچک یا تقریباً مرتب بسیار کارآمد است.

**English:**
Each element is taken from the unsorted part and inserted into its correct position in the sorted portion — similar to sorting playing cards in hand. Very efficient for small or nearly sorted arrays.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

---

### ۴. مرتب‌سازی ادغامی (Merge Sort)

**توضیح فارسی:**
این الگوریتم از رویکرد «تقسیم و حل» استفاده می‌کند. آرایه به دو نیمه تقسیم می‌شود، هر نیمه به صورت بازگشتی مرتب می‌شود و سپس دو نیمه مرتب‌شده با هم ادغام می‌شوند. این الگوریتم پایدار و با پیچیدگی O(n log n) است.

**English:**
Uses a divide-and-conquer approach. The array is split in half, each half is recursively sorted, and then the two sorted halves are merged. It is a stable sort with guaranteed O(n log n) time complexity.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)
```

---

### ۵. مرتب‌سازی سریع (Quick Sort)

**توضیح فارسی:**
یک عنصر به عنوان pivot انتخاب می‌شود و آرایه به دو بخش تقسیم می‌شود: عناصر کوچک‌تر از pivot و عناصر بزرگ‌تر. سپس این عمل به صورت بازگشتی روی هر بخش تکرار می‌شود. در حالت میانگین بسیار سریع است.

**English:**
A pivot element is chosen, and the array is partitioned into elements less than and greater than the pivot. The process is recursively applied to both partitions. Very fast in the average case, but O(n²) in the worst case.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
```

---

### ۶. مرتب‌سازی هرمی (Heap Sort)

**توضیح فارسی:**
از ساختار داده heap (درخت دودویی کامل) استفاده می‌کند. ابتدا آرایه به یک max-heap تبدیل می‌شود، سپس بزرگ‌ترین عنصر (ریشه) با آخرین عنصر جابجا شده و heap مجدداً ساخته می‌شود. این الگوریتم in-place و با پیچیدگی O(n log n) است.

**English:**
Uses the heap data structure. The array is first turned into a max-heap, then the largest element (root) is swapped with the last element, and the heap is rebuilt. This is an in-place algorithm with O(n log n) time complexity.

```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr
```

---

### ۷. مرتب‌سازی شمارشی (Counting Sort)

**توضیح فارسی:**
برای اعداد صحیح غیر منفی با دامنه مشخص مناسب است. تعداد تکرار هر عدد شمرده می‌شود و بر اساس آن آرایه خروجی ساخته می‌شود. زمانی که دامنه اعداد کوچک باشد بسیار سریع است.

**English:**
Suitable for non-negative integers with a known range. Counts the occurrences of each number and builds the output array accordingly. Very fast when the range of values (k) is small relative to n.

```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)
    return result
```

---

### ۸. مرتب‌سازی پایه‌ای (Radix Sort)

**توضیح فارسی:**
اعداد را رقم به رقم (از کم‌ارزش‌ترین به پرارزش‌ترین) مرتب می‌کند. برای هر رقم، از مرتب‌سازی شمارشی استفاده می‌شود. برای اعداد صحیح بزرگ بسیار کارآمد است.

**English:**
Sorts numbers digit by digit, from the least significant to the most significant digit. Uses counting sort as a subroutine for each digit. Very efficient for large integers.

```python
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr
```

---

## نحوه استفاده | Usage

```python
from sorting_algorithms import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, heap_sort,
    counting_sort, radix_sort
)

arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))    # [11, 12, 22, 25, 34, 64, 90]
print(merge_sort(arr))     # [11, 12, 22, 25, 34, 64, 90]
print(quick_sort(arr))     # [11, 12, 22, 25, 34, 64, 90]
```

## اجرا | Run

```bash
python sorting_algorithms.py
```

---

## مقایسه الگوریتم‌ها | Algorithm Comparison

```
برای آرایه‌های کوچک:    Insertion Sort یا Bubble Sort
برای آرایه‌های بزرگ:    Merge Sort یا Quick Sort یا Heap Sort
برای اعداد صحیح:        Counting Sort یا Radix Sort (سریع‌ترین)
```

```
For small arrays:        Insertion Sort or Bubble Sort
For large arrays:        Merge Sort, Quick Sort, or Heap Sort
For integers:            Counting Sort or Radix Sort (fastest)
```
