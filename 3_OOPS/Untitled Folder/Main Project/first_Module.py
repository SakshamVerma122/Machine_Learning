def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == "__main__":
    main()


# ******** Main usage of if __name__ == "__main__" ***********
# You can segregate functionalities and variable based on whether
# the file has been imported or it is the main source/ start of
# programme

# if __name__ == "__main__":
#     print("Ran directly")
# else:
#     print("Ran indirectly")