### **What is Time Complexity?**

*   Time complexity measures the amount of time an algorithm takes to run as a function of the input size (**n**).
    
*   It helps compare algorithms regardless of hardware/software differences.
    

### **Common Time Complexities**

1.  **O(1) – Constant time**
    
    *   Execution time does not depend on input size.
        
    *   Example: Accessing an array element by index.
        
2.  **O(log n) – Logarithmic time**
    
    *   Time grows slowly as input increases.
        
    *   Example: Binary Search.
        
3.  **O(n) – Linear time**
    
    *   Time grows proportionally with input size.
        
    *   Example: Traversing an array.
        
4.  **O(n log n) – Log-linear time**
    
    *   Common in efficient sorting algorithms.
        
    *   Example: Merge Sort, Quick Sort (average case).
        
5.  **O(n²) – Quadratic time**
    
    *   Time grows with square of input size.
        
    *   Example: Nested loops, Bubble Sort.
        
6.  **O(2^n) – Exponential time**
    
    *   Grows very fast; impractical for large inputs.
        
    *   Example: Solving recursive problems like subset generation.
        
7.  **O(n!) – Factorial time**
    
    *   Extremely slow, used in brute-force permutations.
        
    *   Example: Traveling Salesman (brute force).
        

### **Best, Average, Worst Case**

*   **Best case**: Minimum time (e.g., searching first element).
    
*   **Average case**: Expected/typical time.
    
*   **Worst case**: Maximum time taken for largest/most complex input.
    

### **How to Analyze?**

*   Focus on **number of operations** relative to input size.
    
*   Ignore constants and lower-order terms.
    
    *   Example: 3n + 5 → **O(n)**.
        
    *   Example: 2n² + 10n → **O(n²)**.