"""Three clients harry ,rohan,hamad we have to log their food and excercises detail"""
def logd():
    """This function log the details of food and excercise"""
    choose = int(input("Choose:\n1.Food\
n2.Excercise"))
    if choose==1:
        usr=int(input("Select the user:\n1.Harry\n2.Rohan\n3.Hamad"))
        if usr==1:
            f=open("Harryfood.txt","a")
        elif usr==2:
            f=open("Rohanfood.txt","a")
        else:
            f=open("Hamadfood.txt","a")
    else:
        usr = int(input("Select the user:\n1.Harry\n2.Rohan\n3.Hamad"))
        if usr == 1:
            f = open("Harryexr.txt", "a")
        elif usr == 2:
            f = open("Rohanexr.txt", "a")
        else:
            f = open("Hamadexr.txt", "a")

    data=input("Enter Your details")
    time=getdate()
    f.write(f"{time}:: {data}\n")
    return
def retrived():
    """This function is used to retrive data of the user"""
    choose = int(input("Choose:\n1.Food\
n2.Excercise"))
    if choose == 1:
        usr = int(input("Select the user:\n1.Harry\n2.Rohan\n3.Hamad"))
        if usr == 1:
            f = open("Harryfood.txt")
        elif usr == 2:
            f = open("Rohanfood.txt")
        else:
            f = open("Hamadfood.txt")
    else:
        usr = int(input("Select the user:\n1.Harry\n2.Rohan\n3.Hamad"))
        if usr == 1:
            f = open("Harryexr.txt")
        elif usr == 2:
            f = open("Rohanexr.txt")
        else:
            f = open("Hamadexr.txt")
    print(f.read())
    return
def getdate():
    import datetime
    return datetime.datetime.now()

choice=int(input("HEALTH MANAGEMENT SYSTEM:Enter your choice\n"
            "1.log the data\n 2.retrive the data"))
if(choice==1):
    logd()
else:
    retrived()
