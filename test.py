from typing import Annotated,get_type_hints
def double(x: Annotated[int,(0,100)]) -> int:
    type_hints = get_type_hints(double,include_extras=True)
    print(type_hints)  # Output: {'x': <class 'int'>, 'return': <class 'int'>}
    return x * 2

result = double(4)
print(result)  # Output: 8``