#### create a restaurant Management System #####
menu = {"pizza": 300, "cold drink": 100, "pasta": 150, "sandwich": 140, "coffee": 120}
print("***** Welcome to Golden Globe Restarunt *****")
print("\nHere is our Menu :\n")
bill = 0
cart = []
for i in menu:
    print(i,": ₹"+str(menu[i]))

while True:
    order = input("\What would you like to have:")
    if order == 'stop':
        print("Your bill is :₹"+str(bill))
        print("Your order are")
        for i in cart:
            print(i)
        break
    elif order in menu:
        quantity = int(input(f"\nHow many{order}'s you want:"))
        bill = bill+menu[order]*quantity
        cart.append(order)
    else:
        print("Sorry, We don't serve out of menu")



    
