# Chapter 8
# Project: Sandwich maker


# prices of sandwich elements
prices = {
    "wheat": 1.5,
    "white": 1,
    "sourdough": 1.75,
    "chicken": 2,
    "turkey": 1.2,
    "ham": 1.45,
    "tofu": 1.7,
    "cheddar": 1,
    "Swiss": 1,
    "mozzarella": 1,
    "mustard": 0.5,
    "mayo": 0.5,
    "tomato": 0.7,
    "lettuce": 0.7
}


readySandwich = []
readySandwich.append(pyip.inputMenu(choices=["wheat", "white",  "sourdough"]))
readySandwich.append(pyip.inputMenu(
    choices=["chicken", "turkey", "ham", "tofu"]))
cheese = pyip.inputYesNo("Do you want cheese? (yes/no) ")
if cheese == "yes":
    readySandwich.append(pyip.inputMenu(
        choices=["cheddar", "Swiss",  "mozzarella"]))
mustard = pyip.inputYesNo("Do you want musstard? (yes/no) ")
if mustard == "yes":
    readySandwich.append('mustard')
mayo = pyip.inputYesNo("Do you want mayo? (yes/no) ")
if mayo == "yes":
    readySandwich.append('mayo')

tomato = pyip.inputYesNo("Do you want tomato? (yes/no) ")
if tomato == "yes":
    readySandwich.append('tomato')
lettuce = pyip.inputYesNo("Do you want lettuce? (yes/no) ")
if lettuce == "yes":
    readySandwich.append('lettuce')
numberOfSandwiches = pyip.inputInt("How many sandwiches do you want? ", min=1)

cost = 0
for elements in readySandwich:
    cost += prices[elements]
print("It will cost {}$".format(cost*numberOfSandwiches))
