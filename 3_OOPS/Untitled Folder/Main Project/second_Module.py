import first_Module
# Here even after importing firsT_Module things of first_Module 
# will not work because of the if... statement there which will 
# only let first_Module run when the programme is executed from 
# first_Module.py

print("Second Module's Name : {}".format(__name__))