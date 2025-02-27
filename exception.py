
try:
    num=int(input("Enter Name:"))
    if(num==0):
        print("invalid")
        newdiv=100/num
    print("You enterred {num}") 
except ValueError:
    print("invalid number format")
    
else:
    print("no exceptions occured") 
finally:
    print("Execution completed")  