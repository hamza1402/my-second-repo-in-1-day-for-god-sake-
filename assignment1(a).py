# a) Basic Calculator

while True:
    print("1.sub")
    print("2.add")
    print("3.div")
    print("4.mul")
    print("5.Exit")
    ch = int(input("Enter Choice(1-5):"))
    if ch == 5:
        print("Exiting the Calculator")
        break
    num1=int(input("no1 is:"))
    num2=int(input("no2 is:"))
    if ch == 1:
        print("sub is",(num1-num2))
    elif ch == 2:        
        print("add is",(num1+num2))
    elif ch == 3:        
        print("div is",(num1/num2))
    elif ch == 4:        
        print("mul is",(num1*num2))
    else:
        print("wrong choice")
    cont = input("Do you want to continue?(yes/no)")
    if cont == "no":
        print("Exiting the calculator")
        break