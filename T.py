for row in range(7):
    for col in range(5):
        if (col==2) or (row==0):
            print ("*",end="")
        else:
            print(end=" ")
    print() 
