'''
- Recursion holo emon ekti process ekhane
ekti function nijekei abar call kore.
- Recursion obosshoi kono ek somoy theme jabe.
- je condition Recursion thamay take bole Base Case.
'''
# Simple example
def countdown(n):
    if n == 0:
        return
    print(n)

    countdown (n - 1)

countdown(5)