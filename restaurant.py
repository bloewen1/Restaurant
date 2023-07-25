#name = input("Welcome to Joey's good sir. My name is Wilfred and I shall be your waiter for today. May I ask what your name is?\n")
#print("Welcome {}!".format(name))
#print("Allow me to show you the drink menu")
with open("desserts/dessert.txt", 'rb') as f:
    print (f.read().decode('utf-8'))
