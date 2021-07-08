random=6
option=int(input("enter some number:"))

while option != random:
    print("incorret")
    option=int(input("guess again or press or 0 to stop:"))
    if option==0:
       break
if option==0:
   print("game over")
elif option==random:
   print("yeah won the game!!")
