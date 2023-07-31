from time import sleep

#Defining a couple global variables. Order is a list that will contain everything the customer ordered in the order they ordered it.
order = []
#Message is the default message to be displayed with choices. It's used often so it was easiest to make it a variable.
message = "\nType the number of the item you would like to order.\nTo order nothing, type 0: "
print("\nWelcome to The Restaurant™ my name is Wilfred and I will be your waiter.")
#The sleeps throughout the program are just to make the pacing look nicer and give the user a better experience
sleep(1)
#Use an input to get the customer's name that will be used throughout the program
name = input("\nWhat is your name?: ")
print("\nWelcome {}! Let's get started!".format(name))

#This function takes an input, verifies that it's an integer, and checks if it's in a given range.
#If the function is not both of those things the input prompt will be given to the user until a valid input is given.
def choices(max, min = 0, msg = message):
    while True:
        try:
            choice = int(input(msg))
            if min <= choice <= max:
                return choice
        except:
            pass

#This is to choose between two options. The default options are yes and no. 
#The program will give the user the same prompt until their input matches one of the two choices
def binary(msg, opt1 = "yes", opt2 = "no"):
    while True:
        ans = input(msg)
        if ans.upper() == opt1.upper():
            return True
        elif ans.upper() == opt2.upper():
            return False

def drinks():
    #Create a list of dictionaries for all the options
    items = [{"name": "Water", "price": 0.00, "image": "drinks/water.txt"},
            {"name": "Coffee", "price": 6.50, "image": "drinks/coffee.txt"},
            {"name": "Tea", "price": 5.00, "image": "drinks/tea.txt"},
            {"name": "Juice", "price": 1.50, "image": "drinks/juice.txt"},
            {"name": "Coca Cola", "price": 2.50, "image": "drinks/can.txt"},
            {"name": "Pepsi", "price": 2.50, "image": "drinks/can.txt"},
            {"name": "Orange Crush", "price": 2.50, "image": "drinks/can.txt"},
            {"name": "Dr. Pepper", "price": 2.50, "image": "drinks/can.txt"}]
    #Print the drinks menu
    with open("drinks/drinks.txt", 'rb') as f:
        print("\nHere is the drinks menu {}:\n{}".format(name, f.read().decode()))
    #Make the user select a drink, or 0 for nothing
    num = choices(8)
    #If they select juice, ask them what type then change the name of the juice dictionary
    if num == 4:
        if binary("\nApple or Orange?: ", "apple", "orange"):
            items[num-1]["name"] = "Apple Juice"
        else:
            items[num-1]["name"] = "Orange Juice"
    #If they don't select nothing, add the selected drink's dictionary to the order list then print out the drink's text file
    if num != 0:
        order.append(items[num-1])
        with open(items[num-1]["image"], 'rb') as f:
            sleep(1)
            print("\nHere is your drink")
            print(f.read().decode())
        #Return the dictionary of the chosen drink
        return items[num-1]
    else:
        return None

def appetizers():
    #Create a list that will contain the selected appetizers' text file paths so they can be printed out later
    ordered = []
    items = [{"name": "Caesar Salad", "price": 4.50, "image": "appys/salad.txt"},
            {"name": "Soup", "price": 5.50, "image": "appys/soup.txt"},
            {"name": "Nachos", "price": 6.00, "image": "appys/nachos.txt"},
            {"name": "Pretzel", "price": 4.00, "image": "appys/pretzel.txt"},
            {"name": "Wings", "price": 7.50, "image": "appys/wings.txt"}]
    
    with open("appys/appetizers.txt", 'rb') as f:
        print("\nHere is the appetizer menu {}:\n{}".format(name, f.read().decode()))
    '''
    Create a variable called more. While more is true, the user will be asked to make another selection
    The user will be asked if they want to order another appetizer. Saying no will set more to false and end the loop
    This way, the user can select as much food as they want before continuing on
    '''
    more = True
    while more:
        num = choices(5)
        #For each item selected, give the user the additional options and change the name and price of the item accordingly
        match num:
            case 0:
                return ordered
            
            case 1:
                if binary("\nDo you want to add bacon for no charge? (yes/no): "):
                    items[num-1]["name"] = "Caesar Salad + Bacon"

            case 2:
                if binary("\nTomato or French Onion?: ", "tomato", "french onion"):
                    items[num-1]["name"] = "Tomato Soup"
                else:
                    items[num-1]["name"] = "French Onion Soup"

            case 3:
                if binary("\nWould you like to add queso? (yes/no): "):
                    items[num-1]["name"] = "Nachos + queso"
                    items[num-1]["price"] = 6.50

            case 4:
                if binary("\nWould you like to add a cheese dip? (yes/no): "):
                    items[num-1]["name"] = "Pretzel + cheese dip"
                    items[num-1]["price"] = 4.50
                
            case 5:
                option = choices(3, 1, "\n1. Honey Garlic\n2. Salt and Pepper\n3. Spicy Buffalo\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Honey Garlic Wings"
                elif option == 2:
                    items[num-1]["name"] = "Salt and Pepper Wings"
                else:
                    items[num-1]["name"] = "Spicy Buffalo Wings"
        
        #Add the selected item to order and the image path to ordered, then return ordered
        order.append(items[num-1])
        ordered.append(items[num-1]["image"])
        more = binary("\nDo you want to order another appetizer? (yes/no): ")
    return ordered

#Same format as appetizers just with different options
def entrees():
    ordered = []
    items = [{"name": "Personal Pizza", "price": 14.50, "image": "mains/pizza.txt"},
            {"name": "Chicken Sandwich", "price": 10.00, "image": "mains/sandwich.txt"},
            {"name": "Burger", "price": 16.00, "image": "mains/burger.txt"},
            {"name": "Steak", "price": 27.00, "image": "mains/steak.txt"},
            {"name": "Tacos", "price": 13.00, "image": "mains/taco.txt"}]
    with open("mains/entrees.txt", 'rb') as f:
        print("\nHere is the entree menu {}:\n{}".format(name, f.read().decode()))
    more = True
    while more:
        num = choices(5)
        match num:
            case 0:
                return ordered
            
            case 1:
                option = choices(3, 1, "\n1. Pepperoni\n2. Cheese\n3. Hawaiian\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Pepperoni Pizza"
                elif option == 2:
                    items[num-1]["name"] = "Cheese Pizza"
                else:
                    items[num-1]["name"] = "Hawaiian Pizza"

            case 2:
                items[num-1]["name"] = "Chicken Sandwich"
                items[num-1]["price"] = 10.00
                if binary("\nWould you like to add the spicy sauce? (yes/no): "):
                    items[num-1]["name"] = items[num-1]["name"] + " + Sauce"
                    items[num-1]["price"] = items[num-1]["price"] + 0.5

                if binary("\nWould you like to add extra meat? (yes/no): "):
                    items[num-1]["name"] = items[num-1]["name"] + " + Meat"
                    items[num-1]["price"] = items[num-1]["price"] + 1.00

            case 3:
                option = choices(2, 0, "\n0. No Side\n1. Fries\n2. Onion Rings\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Burger + Fries"
                elif option == 2:
                    items[num-1]["name"] = "Burger + Onion Rings"
                    items[num-1]["price"] = 16.50
               
            case 4:
                option = choices(3, 0, "\n0. No Side\n1. Mashed Potatoes\n2. Baked Potato\n3. Cole Slaw\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Steak + Mashed Potatoes"
                elif option == 2:
                    items[num-1]["name"] = "Steak + Baked Potato"
                elif option == 3:
                    items[num-1]["name"] = "Steak + Cole Slaw"
                
            case 5:
                option = choices(3, 1, "\n1. Al Pastor\n2. De Carnitas\n3. De Pescado\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Tacos al Pastor"
                elif option == 2:
                    items[num-1]["name"] = "Tacos de Carnitas"
                else:
                    items[num-1]["name"] = "Tacos de Pescado"
        
        order.append(items[num-1])
        ordered.append(items[num-1]["image"])
        more = binary("\nDo you want to order another entree? (yes/no): ")
    return ordered

#Same format as appetizers and entrees but desserts don't have extra options so the code is a lot simpler
def dessert():
    ordered = []
    items = [{"name": "Apple Pie", "price": 11.50, "image": "desserts/applepie.txt"},
            {"name": "Cherry Pie", "price": 11.50, "image": "desserts/cherrypie.txt"},
            {"name": "Chocolate Cake", "price": 9.00, "image": "desserts/cake.txt"},
            {"name": "Ice Cream Cone", "price": 5.00, "image": "desserts/icecream.txt"},
            {"name": "Choc. Chip Cookie", "price": 6.00, "image": "desserts/cookie.txt"}]
    with open("desserts/dessert.txt", 'rb') as f:
        print("\nHere is the dessert menu {}:\n{}".format(name, f.read().decode()))
    more = True
    while more:
        num = choices(5)
        if num == 0:
            return ordered
        order.append(items[num-1])
        ordered.append(items[num-1]["image"])
        more = binary("\nDo you want to order another dessert? (yes/no): ")
    return ordered

#This function will take a list of paths to text files of ASCII art and then print all of them out to the screen.
def giveCourse(course):
    for i in course:
        with open(i, 'rb') as f:
            print(f.read().decode())
            sleep(2)

#This function will give the user a refill or new drink if they want it.
#Take in a path to ASCII art of the user's current drink
def refill(drink):
    #Ensure there is a drink to refill
    if drink != None:
        #If the user wants a refill, print their current drink. Otherwise, if they want a new drink, call the drinks function
        if binary("\nWould you like your drink refilled? (yes/no): "):
            with open(drink["image"], 'rb') as f:
                print(f.read().decode())
        else:
            if binary("\nWould you like a new drink? (yes/no): "):
                drink = drinks()
    else:
        if binary("\nWould you like a new drink? (yes/no): "):
            drink = drinks()
    return drink

#This will create a receipt for the user in the same style as the menus.
#The width of the receipt is hard coded to be just longer than the longest menu item.
def receipt(order):
    #Make a subtotal variable that will be added to 
    subtotal = 0.00
    #Open receipt.txt in write mode
    f = open("receipt.txt", 'w')
    #Create the header in receipt.txt
    f.write("+" + "-" * 41 + "+")
    f.write("\n|" + " " * 17 + "Receipt" + " " * 17 + "|\n")
    f.write("|" + "-" * 41 + "|")
    #For every item ordered, add the price to the subtotal
    for i in order:
        subtotal += i["price"]
        #Convert the price rounded to two decimals to a string and concatenate it with the item's name
        line = i["name"] + "   $" + str("{:.2f}".format(round(i["price"], 2))) + "  "
        #Write a line with enough spaces to make inbetween the sides 41 characters long
        f.write("\n|" + " " * (41 - len(line)) + line + "|")
    f.write("\n|" + " " * 41 + "|")
    #Ask for a percentage to be tipped
    while True:
        try:
            grat = float(input("\nWhat percent would you like to give as a tip?: "))
            if 0 <= grat <= 100:
                break
        except:
            pass
    #Calculate subtotal, tax(5%), and the tip
    sub = "Subtotal   $" + str("{:.2f}".format(round(subtotal, 2))) + "  "
    tax = "Tax    $" + str("{:.2f}".format(round(subtotal*0.05, 2))) + "  "
    tip = "Tip    $" + str("{:.2f}".format(round(subtotal*(grat/100), 2))) + "  "
    #Write a line for each of the subtotal, tax, and tip
    for i in [sub, tax, tip]:
        f.write("\n|" + " " * (41-len(i)) + i + "|")
    f.write("\n|" + " " * 41 + "|")
    #Calculate the final total be multiplying the subtotal by 1.05 + whatever percent the tip is
    total = "Total   $" + str("{:.2f}".format(round(subtotal*(1.05 + (grat/100)), 2))) + "  "
    f.write("\n|" + " " * (41-len(total)) + total + "|")
    f.write("\n+" + "-" * 41 + "+")
    f.close()
    #Print out the completed receipt
    f = open("receipt.txt")
    print(f.read())


sleep(1)
#Give the drinks menu. The drinks function will print out the drink's text file
drink = drinks()
print("\nI will get you the meal menus in a moment")
sleep(1)
input("\nPress enter when you are ready to see the appetizers")
#Give the appetizer menu
appys = appetizers()
print("\nI'll bring the entree menu right away")
sleep(1)
#Give the entree menu
mains = entrees()
sleep(1)
print("\nExcellent. We will get you your food right away.")
sleep(1)
input("\nPress enter to recieve your food.")
#Print out the appetizers and offer a refill
if len(appys) > 0:
    giveCourse(appys)
    drink = refill(drink)
    sleep(1)
    input("\nPress enter to recieve your entrees")
#Print out the entrees and offer a refill
if len(mains) > 0:
    giveCourse(mains)
    drink = refill(drink)
sleep(1)
print("\nI will bring the dessert menu now")
sleep(1)
#Give the dessert menu, print out the desserts, then offer one final refill
desserts = dessert()
sleep(1)
giveCourse(desserts)
refill(drink)
sleep(1)
print("\nI will bring you the bill now {}".format(name))
sleep(2)
#Give the receipt
receipt(order)
sleep(1)
print("\nHave a great day {}!".format(name))