def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mult(a,b):
    return(a*b)
def div(a,b):
    return(a/b)


# * if we want to run a pyhthon file just like any simple python file even though it is a module inside the package you can run it only thing that changes is import name of the particular module
# * if we running it directly import name is **__main__**
# * else **__name__** is **math.simple(package_name.module_name)**

if __name__ == "__main__":
    print("Hello")
    a = int(input())
    b = int(input())

    print("If you run this module/file directly the output is :", add(a, b))