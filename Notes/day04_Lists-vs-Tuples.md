# 📌 Lists vs Tuples in Python

## 🔑 Key Differences

| Feature              | **List** (`[]`) | **Tuple** (`()`) |
|----------------------|-----------------|------------------|
| **Mutability**       | ✅ Mutable (can be changed: add, remove, update elements) | ❌ Immutable (cannot be changed after creation) |
| **Syntax**           | Square brackets: `[1, 2, 3]` | Parentheses: `(1, 2, 3)` |
| **Performance**      | Slower (because of mutability overhead) | Faster (lighter weight, fixed size) |
| **Use Cases**        | When data may change (e.g., dynamic collections) | When data should remain constant (e.g., fixed config, dictionary keys) |
| **Methods Available**| Many (e.g., `.append()`, `.remove()`, `.sort()`) | Few (mainly `.count()`, `.index()`) |
| **Memory Usage**     | Higher | Lower |
| **Hashable**         | ❌ Not hashable (can’t be used as dict keys) | ✅ Hashable (if all elements are immutable) |

---

## 🧑‍💻 Examples

### 1. List Example
```python
# List: Mutable
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")   # Add element
fruits[1] = "blueberry"  # Modify element
print(fruits)  # ['apple', 'blueberry', 'cherry', 'mango']
```


### 2. Tuple Example

```python
# Tuple: Immutable
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # ❌ Error: 'tuple' object does not support item assignment
print(colors)  # ('red', 'green', 'blue')
```


