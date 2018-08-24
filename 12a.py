a=3
if a<4:
    try:
        b=a/(a-3)
        print(b)
        
    except ZeroDivisionError:
        print("Exception in Program is",ZeroDivisionError)
    
