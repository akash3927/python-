#lists
companies=["mahindra","swarajya","rucha","papl"]
#1
print(companies)
#2
print(companies[0])
#3
print(companies[1])
#4
print(companies[1].title())
#replacing
companies[0]="force"
print(companies)
#adding or appending
companies.append("mahindra")
print(companies)
#removing
del companies[0]
print(companies)
#sort
companies.sort()
print(companies)
######
print("Here is the original list:")
print(companies)
print("\nHere is the sorted list:")
print(sorted(companies))
print("\
nHere is the original list again:")
print(companies)
#reverse function
companies.reverse()
print(companies)
#length
print(len(companies))
####working with the lists
industries=["mahindra","swarajya","rucha","papl"]
for industry in industries:
    print(industry)
    print(industry.title()+",is good company for learning")
    print("it s giving chance to freshers to built thier carrier")
##########or loop for numbers
for value in range(1,5):
    print(value)
#######    
numbers=list(range(1,6))
print(numbers)
#even numbers
evennos=list(range(2,40,2))
print(evennos)
####oddnos
oddnos=list(range(1,30,2))
print(oddnos)
####
nos=[1,2,3,4,5,6,7,8,9]
print(min(nos))
print(max(nos))
print(sum(nos))
####
squares=[square**2 for square in range(10,16)]
print(squares)
#####
family=["mother","father","brother","sister","me"]
print(family[1:4])        
print(family[:4])
myfamily=family[:]
print(myfamily)
