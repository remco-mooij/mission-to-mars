# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])

while allowance > 0:
    candy_choice = int(input("Make your selection: "))
    candyCart.append(candyList[candy_choice])

    print(candyCart)

    allowance = allowance - 1


