# way 1 - import module_name
import calculator

result = calculator.add(19, 3)
print(result)

# way 2 - from module import function
from calculator import add
result = add(100, 199)
print(result)

# multiple function import
from calculator import multiply, subtract, add

print(add(10, 5))
print(multiply(29, 18))
print(subtract(29, 18))

# way 3 - use of Alias (as)
import calculator as calc
print(calc.add(10, 20))

# alias of function
from calculator import multiply as mul
print(mul(4, 5))