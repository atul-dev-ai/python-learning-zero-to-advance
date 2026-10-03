# return holo Function er result firiye deya
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# None mane holo function jodi kono value return na kore tahole default vabe None return kore.
def greet():
    print("Hello")

result = greet()
print(result) # none

def test():
    print("A")
    return 
    print("B")
test()
# B print hobe na karon return pawar por function sekhanei sesh hoye jay.

def example():
    return 100
    print("Hello")
    