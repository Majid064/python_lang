# from typing import Callable

# add : Callable[[int,int],int] = lambda x,y : x + y

# result = add(10,20)
# print(result)


from collections.abc import Iterator    # abc stands for abstract base classes

def my_range(start:int , end:int , step: int=1)->Iterator[int]:     # -> indicate return type
    for i in range(start,end+1,step):
        yield i # Generator fucntion


a : Iterator[int] = my_range(1,10)

print(next(a))
print(next(a))

print(type(a)) 