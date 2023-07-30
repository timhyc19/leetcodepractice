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
- initializing l, r = 0, len(lists) - 1, then shifting based on conditionals, tricks, etc...


# Sliding Window
- shifting left and right pointer while in a loop

# Stack
- stack is linear data structure, following LIFO (Last in First Out) --> stack of plates, only top plates are processed, meaning everything underneath has to wait

- different from queue(), which is FIFO (First in First Out) --> ticket counter, first person in line is first person served, and everyone else follows in the order
```
Operation (stack)   |  Time Complexity | 
stack.pop()         |       O(1)       |     
stack.append()      |       O(1)       |   
stack[-1] (top)     |       O(1)       |
```

- Good System Design Question:
```
Min Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(val if (not self.minStack or val < self.minStack[-1]) else self.minStack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

# Binary Search
- Binary Search is basically traversing through sorted array in halves (finding the midpoint), rather than linear search
- Hence, runtime is O(log n)
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
```

- Good System Design Questions for Binary Search:
```
Time Based Key Value Store
class TimeMap:

    # O(n) memory
    def __init__(self):
        self.store = {} # key: list of [val, timestamp]

    # O(1) operation
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


    # O(log n) operation
    def get(self, key: str, timestamp: int) -> str:
        s = self.store.get(key, [])
        l, r = 0, len(s) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if s[m][1] <= timestamp:
                res = s[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

# Linked List
- Linked list are blocks (nodes) that have pointers that point to other nodes
```
- Traversing Linked List is O(n) 
- Finding a specific element requires traversal (since there is no index)
- Inserting and deleting in linked list with a reference is efficient --> achieve O(1) time (updating pointers)
- Linked list can get complicated to implement, and also takes up a good amount of memory (has to store pointer data)
```

- Good system design question for linked lists:
```
LRU Cache (Really Popular)
class Node():
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # map key to node
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left


    # remove node from linked list of size capacity
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node to back of linked list (most recently used)
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key])
    
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```


# Trees
### Level Order Traversal
- Traversing through each level of the tree. 
- Main way is to create a stack of the results, and a deque() with the root, and continously popleft() each level through the range. 
- All traversal algorithms below require O(n) time complexity and O(n) space complexity
```
class Solution:
    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res
```


### In Order Traversal
- In order traversal is traversing through each element of the tree, smallest to largest (ascending order)
- Basically left subtree, then root, then right subtree

```
Recursive solution:
class Solution:
    def traverse(self, root, res):
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)
    
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        traverse(root, res)
        return res
```

```
Iterative Solution:
# traverse as far left as possible (adding to stack), then pop and append value, then traverse right

class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = Node
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            res.append(node.val)
            curr = curr.right

        return res
```


### Post Order Traversal
- Traverse through from left subtree, right subtree, then root
```
Recursive Solution:
class Solution:
    def traverse(self, root, res):
        if not root:
            return None
        self.traverse(root.left, res)
        self.traverse(root.right, res)
        res.append(root.val)

    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        traverse(root, res)
        return res
```

```
Iterative Solution:
class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]
```

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









