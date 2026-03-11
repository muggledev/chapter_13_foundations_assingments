

def list_join(it_obj, separator):

    favorites = ""

    for faves in it_obj:
        favorites += str(faves)
        # favorites = favorites + str(faves) + separator (We do this so that as we run through the for loop
        # it won't just print one thing at a time and replace that one thing in the loop it will actually
        # ADD the items to the list. )
        if faves != it_obj[-1]:
            favorites += separator
    return favorites
    

print(list_join(["Cookies", "Dr.Pepper", 4, 7, 2.007, "Jogging", "Captain America", "Mountains"], " | | | "))



    
    
    
    
    
    
    
