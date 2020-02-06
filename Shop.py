item = {'hats': 25, 'shirts': 25, 'pants': 25, 'socks': 25, 'shoes': 25}
cost = {'hats': 10, 'shirts': 20, 'pants': 15, 'socks': 5, 'shoes': 50}
cart = {}
print("Welcome to the store")
def display():
    flag = True
    while flag:
        if all(value == 0 for value in item.keys()):
            print("No stock left")
            break
        print("Items in shop are")
        print("{0:12} {1}".format("Items", "Qty"))
        for i, j in item.items():
            if j > 0:
                print("{0:12} {1}".format(i, j))
        print('Enter the item you want to buy or enter "q" to exit to main menu')
        input_item = input().lower()
        if input_item == 'q':
            #flag = False
            #continue
            break
        if input_item not in item.keys():
            print("Item not available in the store")
            continue
        print("Enter the quantity of %s you want: " % input_item)
        input_qty = int(input())
        if input_qty > item[input_item]:
            print("We don't have enough in stock")
            continue
        if input_item not in cart.keys():
            cart[input_item] = input_qty
        else:
            cart[input_item] = cart[input_item] + input_qty
        #print(cart)
        item[input_item] = item[input_item] - input_qty
def displayCart():
    if cart == {}:
        print("The cart is empty")
        return
    print("The items in cart")
    print("{0:12} {1:3s} {2}".format("Items", "Qty", "Total"))
    finalTotal = 0
    for i, j in cart.items():
        total = cost[i] * j
        print("{0:12} {1:3d} {2}".format(i, j, total))
        finalTotal = finalTotal + total
    print("------------------------------")
    print("Total        %d" % finalTotal)
    print("------------------------------")
exit = True
while exit:
    print("1. Display the items in the shop and add to cart")
    print("2. Display the cart")
    print("3. Place order")
    print("4. Exit")
    var = int(input())
    if var == 1:
        display()
    elif var == 2:
        displayCart()
    elif var == 3:
        if cart == {}:
            print("Your cart is empty")
            continue
        print("Your order is placed")
        print("----- Thank you. Please visit again soon -----")
        break
    elif var == 4:
        exit = False