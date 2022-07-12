import firstModule

# When ever we import a file it runs that code
# Now you see the change in __name__ from __main__ to firstModule as that file has been imported from first module

print("This is first module's name {}".format(__name__))