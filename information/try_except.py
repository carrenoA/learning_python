try:
    number = 10 / 0
except ZeroDivisionError: #zerodivisionerror is the error name that will appear if we don't use try and except
    print("something went wrong")
finally: #this will execute no matter what
    print("testing")
