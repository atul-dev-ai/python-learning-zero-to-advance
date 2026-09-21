# 🎯 Python Sets: Comprehensive Learning Notes

## 📌 1. What is a Set?
A **Set** in Python is an **unordered collection** of **unique elements**. 
- It is mutable (you can change it).
- It does **not** allow duplicate values.
- Elements in a set must be immutable (like integers, strings, or tuples). You cannot put a list or a dictionary inside a set.

---

## 📌 2. How to Create a Set?
You can create a set using curly braces `{}` or the `set()` constructor.

```python
# Creating a set with values
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list (removes duplicates)
my_list = [1, 2, 2, 3, 3, 4]
unique_set = set(my_list) # Output: {1, 2, 3, 4}

# ⚠️ CAUTION: Creating an empty set
empty_set = set() # Correct way
empty_dict = {}   # This creates an empty Dictionary, NOT a set!
```

---

## 📌 3. Key Characteristics (Set vs List)
| Feature | List `[]` | Set `{}` |
| :--- | :--- | :--- |
| **Order** | Ordered (Maintains insertion order) | Unordered (Items appear randomly) |
| **Duplicates** | Allows duplicate elements | **Unique elements only** |
| **Indexing** | Supports indexing (e.g., `list[0]`) | **Does NOT support indexing** |

> [!NOTE] 
> Because sets are unordered, you cannot access items using index numbers like `my_set[0]`.

---

## 📌 4. Adding & Removing Elements

### Adding Elements
- `add(item)`: Adds a single item.
- `update(iterable)`: Adds multiple items (like a list or another set).

```python
nums = {1, 2, 3}
nums.add(4)             # {1, 2, 3, 4}
nums.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}
```

### Removing Elements (⚠️ Important Difference)
- `remove(item)`: Removes the item. **Raises a `KeyError` if the element is absent.**
- `discard(item)`: Removes the item. **Does NOT raise an error if the element is absent.**
- `pop()`: Removes and returns a random element (since sets are unordered).
- `clear()`: Empties the entire set.

```python
s = {10, 20, 30}
s.remove(20)   # Removes 20
# s.remove(100) # ❌ KeyError: 100

s.discard(100) # ✅ No error, simply does nothing if 100 is not found
```

---

## 📌 5. Mathematical Set Operations
Sets are extremely powerful for mathematical operations like Union and Intersection.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

**1. Union (Combined without duplicates)**
Combines all unique elements from both sets.
```python
# Operator: | 
print(A | B)           # Output: {1, 2, 3, 4, 5, 6}
print(A.union(B))      # Same output
```

**2. Intersection (Common elements)**
Gets only the elements that exist in BOTH sets.
```python
# Operator: & 
print(A & B)               # Output: {3, 4}
print(A.intersection(B))   # Same output
```

**3. Difference (Elements in A but not in B)**
Removes elements of B from A.
```python
# Operator: -
print(A - B)             # Output: {1, 2}
print(A.difference(B))   # Same output
```

**4. Symmetric Difference (Elements in either A or B, but not both)**
```python
# Operator: ^
print(A ^ B)                       # Output: {1, 2, 5, 6}
print(A.symmetric_difference(B))   # Same output
```

---

## 💡 Why use Sets? (Pro Tips)
1. **Removing Duplicates:** The fastest way to remove duplicates from a list is converting it to a set: `unique_list = list(set(my_list))`
2. **Fast Membership Testing:** Checking if an item exists (`if item in my_set:`) is much faster in a set than in a list, especially for large amounts of data.