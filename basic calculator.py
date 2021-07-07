print("--------------------------BASIC CALCULATOR------------------------")


print("press 1 for add")
print("press 2 for substract")
print("press 3 for multiply")
print("press 4 for divide")

choice= int(input())

if choice in (1,2,3,4):
    num1 = int(input("enter the no 1:"))
    num2 = int(input("enter the no 2:"))


    if choice == 1:
        print("the sum is=",num1+num2)
    elif choice == 2:
        print("the substraction is=",num1-num2)
    elif choice == 3:
        print("the multiplication is=",num1*num2)
    else :
        print("the division is=",num1/num2)
else:
    print("entered option is unavailaible")
