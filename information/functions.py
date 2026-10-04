def function(name, last_name = "calik"): 
    """
    A parameter with = "" has a default value, making it optional. If you don't provide a value when calling the function, 
    it will NOT throw an error; instead, it will use the default value. Errors only occur if you omit a required parameter 
    (one without a default value).
    """
    print("Hello", name, last_name)
    
function("hai") # this will print "Hello hai calik" 
function("caki", "hasan") # this will print "Hello caki hasan"

def function1():
    pass