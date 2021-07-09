items={"apple":100,
       "banana":200,
       "mango":300,}
print("----------welcome to shop----------")
bill=0
for i in items:
    
    print(i,"\tRs",items [i])



try:
    while True:
        order=input("enter your order:")
        if order=="cancel":
            break

        else:
            quantity=int(input("enter quantity:"))
            bill=bill+items[order]*quantity
except:
    print("order not valid")
print("thank you for your purchase,\n your bill is",bill)
