# way 1 - import module_name
import calculator

result = calculator.add(19, 3)
print(result)

# way 2 - from module import function
from calculator import add
result = add(100, 199)
print(result)