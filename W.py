for row in range(4):
     for col in range(7):
          if (col==0 or col==6) or (row==0 and col==3) or ((row==1) and (col==2 or col==4)) or ((row==2) and (col==1 or col==5)):
              print("*",end="")
          else:
              print(end=" ")
     print()         
