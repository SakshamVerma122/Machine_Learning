from maths import *
print(simple.add(1,2))
# name 'simple' is not defined --> ERROR
# We will continue on getting the same error till we declare __all__ = ["simple"]

print(complex.square(2))
# name 'complex' is not defined --> ERROR
# We will continue on getting the same error till we declare __all__ = ["complex"]

# To get rid of both the above we need to declare __all__ = ["complex","simple"]

