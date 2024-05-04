#run.py

import timing

code = '[x**2 for x in range(1000)]'
print(code)

result = timing.timeit(code,100)
print(result)