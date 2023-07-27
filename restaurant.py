order = []
name = input("\nWelcome to The Restaurant™ my name is Wilfred and I will be your waiter.\n\nWhat is your name?: ")
print("\nWelcome {}! Let's get started!".format(name))

def choices(max):
    while True:
        try:
            choice = int(input("\nType the number of the item you would like to order.\nTo order nothing, type 0: "))
            if 0 <= choice <= max:
                return choice
        except:
            pass

def binary(msg, opt1, opt2):
    while True:
        ans = input(msg)
        if ans.upper() == opt1.upper():
            return True
        elif ans.upper() == opt2.upper():
            return False

def dessert():
    ordered = []
    desserts = [{"name": "Apple Pie", "Price": 11.50, "image": "desserts/applepie.txt"},
                {"name": "Cherry Pie", "Price": 11.50, "image": "desserts/cherrypie.txt"},
                {"name": "Chocolate Cake", "Price": 9.00, "image": "desserts/cake.txt"},
                {"name": "Ice Cream Cone", "Price": 5.00, "image": "desserts/icecream.txt"},
                {"name": "Choc. Chip Cookie", "Price": 6.00, "image": "desserts/cookie.txt"}]
    with open("desserts/dessert.txt", 'rb') as f:
        print("\nHere is the dessert menu {}:\n{}".format(name, f.read().decode()))
    more = True
    while more:
        num = choices(5)
        order.append(desserts[num-1])
        ordered.append(desserts[num-1]["image"])
        more = binary("\nDo you want to order anything else? (yes/no): ", "yes", "no")
    return ordered
    

