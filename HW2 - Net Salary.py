# We first ask the user to enter the correct values and check for incorrect or non-numerical values
while True:
    try:
        gross = float(input("Enter your gross salary: "))
        children = int(input("Enter the number of your children: "))
        if gross < 0 or children < 0:
            print("Invalid input! Please enter non-negative values.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number (children must be integers).")

# Here I am creating if loops to give a particular messages according to gross salary
if gross < 1000:
    tax_rate = 0.10
    print("Time to start making bank, no?")
elif gross < 2000:
    tax_rate = 0.12
    print("You could do better, man.")
elif gross < 4000:
    tax_rate = 0.14
    print("You're almooost making something out of your life...")
else:
    tax_rate = 0.18
    print("When are you cruising your Ferrari?")

# Defining the amount of tax paid according to children in the family
if gross < 2000:
    if children == 0:
        print("Get a life LOSER!")
    elif children > 0:
        tax_rate -= children * 0.01
elif gross > 2000:
    if children == 0:
        print("Are you sure you want to die alone without children?")
    elif children > 0:
        tax_rate -= children * 0.005
        print("Nice job with the fam!")

# Calculating gross and net salaries and printing final message
net = gross * (1 - tax_rate)
print("Your net salary is: $", net)