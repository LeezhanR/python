'''
collections:

The collection Module in Python provides different types of containers. A Container
is an object that is used to store different objects and provide a way to access the
contained objects and iterate over them. Some of the built-in containers are Tuple,
List, Dictionary, etc. In this article, we will discuss the different containers 
provided by the collections module
'''
from collections import *
# 1 . Counter
A = [1,1,1,1,1,2,2,2,2,4,4,4,3,3,3,3,10,10,10,10]
Count = Counter(A)
print(Count)
# 2 . OrderedDict
O = OrderedDict()
O['a']=1
O['b']=2
O['c']=3
O['d']=4
O['e']=5
print(O)
O.pop('e')
print(O)
O['e']=6
print(O)
# 3 . DefaultDict
defaultdict(int)
O['e']-=1
print(O)
# 4 . ChainMap 
D1={'f':6,'g':7,'h':8,'i':9,'j':10}
CM=ChainMap(O,D1)
print(CM)
# 5 . NamedTuple
N = namedtuple('Full_Name',['fname','lname','Alais'])
Name1 = ['Leezhan','R','Lee']
Name2 = N('Samuel','Mervin','Sam')
print(N._make(Name1))
print(Name2._asdict())
# 6. Deque
List = deque([1,2,3,4,5,6,7,8,9,10])
List.pop()
List.popleft()
print(List)
List.append(10)
List.appendleft(1)
print(List)





