# Cumulation of Notes for Neetcode 150

# Arrays and Hashing
- Lists are useful for values mapping to index
- Python lists have the following time complexities:
```
Operation (list)    |  Time Complexity | 
Copy                |       O(n)       |     
Append              |       O(1)       |     
Pop (Last)          |       O(1)       |     
Pop (Intermediate)  |       O(n)       |     
Insert              |       O(n)       |    
Get Item            |       O(1)       |   
Set Item            |       O(1)       |   
Delete              |       O(n)       |     
x in s              |       O(n)       |     
min(s), max(s)      |       O(n)       |
length              |       O(1)       |    
```
----------------------------------------------------

- set() function is list with no duplicates in python; useful for unique elements, and no index is stored, making it use less memory and less computationally expensive
- set() also uses hashing so average case lookup of element is O(1), whereas list requires O(n)
- Python sets have the following time complexities:
```
Operation (set)     |  Time Complexity | 
Copy                |       O(n)       |     
Append              |       O(1)       |     
appendleft          |       O(1)       |     
pop                 |       O(1)       |     
popleft             |       O(1)       |    
Remove              |       O(n)       |     
length              |       O(1)       |    
```
----------------------------------------------------
- dictionaries {} store key and value (use hashing --> cs240)
```
Operation (dict)    |  Time Complexity | 
k in d              |       O(1)       |     
get item            |       O(1)       |     
set item            |       O(1)       |     
delete item         |       O(1)       |     
```
----------------------------------------------------
#### Tricks:
- Common patterns:
```
1. Using d = Counter(s) to make a dictionary of counts of inp
2. When using dictionary, you can make value a list 
```

# Two Pointers


# Sliding WIndow


# Stack


# Binary Search


# Linked List


# Trees


# Tries


# Heap / Priority Queue


# Backtracking


# Graphs


# Advanced Graphs


# 1-D Dynamic Programming


# 2-D Dynamic Programming


# Greedy


# Intervals


# Math and Geometry


# Bit Manipulation









