# Python-LinkedList
Simple python implementation of a linked list

Examples:
```
from linked_list import LinkedList
l = LinkedList()
l.add_first(1)
l.add_last(2)
print l
```
->
```
[1,2]
```

```
from linked_list import LinkedList
l = LinkedList()
l.add_first(1)
l.add_last(2)
print l.remove_first()
print l
```
->
```
1
[2]
```
