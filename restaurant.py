from time import sleep

order = []
message = "\nType the number of the item you would like to order.\nTo order nothing, type 0: "
name = input("\nWelcome to The Restaurant™ my name is Wilfred and I will be your waiter.\n\nWhat is your name?: ")
print("\nWelcome {}! Let's get started!".format(name))

def choices(max, min = 0, msg = message):
    while True:
        try:
            choice = int(input(msg))
            if min <= choice <= max:
                return choice
        except:
            pass

def binary(msg, opt1 = "yes", opt2 = "no"):
    while True:
        ans = input(msg)
        if ans.upper() == opt1.upper():
            return True
        elif ans.upper() == opt2.upper():
            return False

def drinks():
    items = [{"name": "Water", "price": 0.00, "image": "drinks/water.txt"},
            {"name": "Coffee", "price": 6.50, "image": "drinks/coffee.txt"},
            {"name": "Tea", "price": 5.00, "image": "drinks/tea.txt"},
            {"name": "Juice", "price": 1.50, "image": "drinks/juice.txt"},
            {"name": "Coca Cola", "price": 2.50, "image": "drinks/can.txt"},
            {"name": "Pepsi", "price": 2.50, "image": "drinks/can.txt"},
            {"name": "Orange Crush", "price": 2.50, "image": "drinks/can.txt"},
            {"name": "Dr. Pepper", "price": 2.50, "image": "drinks/can.txt"}]
    with open("drinks/drinks.txt", 'rb') as f:
        print("\nHere is the drinks menu {}:\n{}".format(name, f.read().decode()))
    num = choices(8)
    if num == 4:
        if binary("\nApple or Orange?: ", "apple", "orange"):
            items[num-1]["name"] = "Apple Juice"
        else:
            items[num-1]["name"] = "Orange Juice"
        order.append(items[num-1])
        return items[num-1]
    elif num != 0:
        order.append(items[num-1])
        return items[num-1]
    else:
        return None


def appetizers():
    ordered = []
    items = [{"name": "Caesar Salad", "price": 4.50, "image": "appys/salad.txt"},
            {"name": "Soup", "price": 5.50, "image": "appys/soup.txt"},
            {"name": "Nachos", "price": 6.00, "image": "appys/nachos.txt"},
            {"name": "Pretzel", "price": 4.00, "image": "appys/pretzel.txt"},
            {"name": "Wings", "price": 7.50, "image": "appys/wings.txt"}]
    
    with open("appys/appetizers.txt", 'rb') as f:
        print("\nHere is the appetizer menu {}:\n{}".format(name, f.read().decode()))
    more = True
    while more:
        num = choices(5)
        match num:
            case 0:
                return ordered
            
            case 1:
                if binary("\nDo you want to add bacon for no charge? (yes/no): "):
                    items[num-1]["name"] = "Caesar Salad + Bacon"
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 2:
                if binary("\nTomato or French Onion?: ", "tomato", "french onion"):
                    items[num-1]["name"] = "Tomato Soup"
                else:
                    items[num-1]["name"] = "French Onion Soup"
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 3:
                if binary("\nWould you like to add queso? (yes/no): "):
                    items[num-1]["name"] = "Nachos + queso"
                    items[num-1]["price"] = 6.50
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 4:
                if binary("\nWould you like to add a cheese dip? (yes/no): "):
                    items[num-1]["name"] = "Pretzel + cheese dip"
                    items[num-1]["price"] = 4.50
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 5:
                option = choices(3, 1, "\n1. Honey Garlic\n2. Salt and Pepper\n3. Spicy Buffalo\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Honey Garlic Wings"
                elif option == 2:
                    items[num-1]["name"] = "Salt and Pepper Wings"
                else:
                    items[num-1]["name"] = "Spicy Buffalo Wings"
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

        more = binary("\nDo you want to order another appetizer? (yes/no): ")
    return ordered


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
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 2:
                items[num-1]["name"] = "Chicken Sandwich"
                items[num-1]["price"] = 10.00
                if binary("\nWould you like to add the spicy sauce? (yes/no): "):
                    items[num-1]["name"] = items[num-1]["name"] + " + Sauce"
                    items[num-1]["price"] = items[num-1]["price"] + 0.5

                if binary("\nWould you like to add extra meat? (yes/no): "):
                    items[num-1]["name"] = items[num-1]["name"] + " + Meat"
                    items[num-1]["price"] = items[num-1]["price"] + 1.00

                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 3:
                option = choices(2, 0, "\n0. No Side\n1. Fries\n2. Onion Rings\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Burger + Fries"
                elif option == 2:
                    items[num-1]["name"] = "Burger + Onion Rings"
                    items[num-1]["price"] = 16.50
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

            case 4:
                option = choices(3, 0, "\n0. No Side\n1. Mashed Potatoes\n2. Baked Potato\n3. Cole Slaw\nChoose one: ")
                if option == 1:
                    items[num-1]["name"] = "Steak + Mashed Potatoes"
                elif option == 2:
                    items[num-1]["name"] = "Steak + Baked Potato"
                elif option == 3:
                    items[num-1]["name"] = "Steak + Cole Slaw"
                order.append(items[num-1])
                ordered.append(items[num-1]["image"])

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

for i in entrees():
    with open(i, 'rb') as f:
        print(f.read().decode())
print(order)