# b) Temperature Conversion Tool

while True:
    print("1.farhenite to celcius")
    print("2.celcius to farhenite")
    print("3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        F =int(input("Enter temperature in farhenite:"))
        C = (F-32)*5/9
        print("temp in celcius is",C)
       
    if ch == 2:
        C = int(input("Enter temperature in Celsius:"))
        F = (9/5)*C+32
        print("temp in farhenite is",F)
        
    elif ch == 3:
        print("exiting the conversion")
        break
    else:
        print("Invalid Choice")
    continue_ch = input("Do you want to continue?(yes/no)")
    if continue_ch == "no":
        print("Exiting the Temperature Conversion")
        break
