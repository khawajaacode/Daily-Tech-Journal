### 💡 What is Big O?

Big O tells you **how fast or slow** an algorithm gets as the number of items (n) grows.\
Think of it as how your program's time increases when your list gets bigger.

* * * * *

### 🔢 Common Sorting Algorithms and Their Big O

| Algorithm | Best Case | Average Case | Worst Case | Notes |
| --- | --- | --- | --- | --- |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | Very slow; only fine for small lists |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | Always slow, no matter what |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | Good for nearly-sorted data |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | Fast and consistent; uses extra memory |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | Usually fastest, but can degrade on bad pivots |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | Fast and reliable; no extra memory needed |
| **Counting / Radix / Bucket Sort** | O(n) | O(n) | O(n) | Only works for special cases (like numbers within a range) |