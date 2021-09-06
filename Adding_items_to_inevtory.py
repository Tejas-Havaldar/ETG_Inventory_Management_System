import json

with open("stock.json", "r") as f:
    r = f.read()

stock = json.loads(r)

choice = True

while (choice):
    product_id = int(input("Enter the Product ID: "))
    if (str(product_id) in stock.keys()):
        print("This id and the product already exits in the inventory")
        print(stock[str(product_id)])
    prod_name = input("Enter the name of the product: ")
    price = int(input('Enter the Price: '))
    quantity = int(input('Enter the quantity: '))
    mfd = input("Enter the Date of Manufacture: ")


    if (str(product_id) in stock.keys()):

        stock[str(product_id)]['quantity'] += quantity
        stock[str(product_id)]['mfd'] = mfd
        print("-----------------------------------------")
        print("After Updation: ")
        print(stock[str(product_id)])
        print("-----------------------------------------")

    else:
        stock[product_id] = {'name': prod_name, 'price': price, 'quantity': quantity, 'mfd': mfd}

    json_object = json.dumps(stock)
    with open("stock.json", "w") as f:
        f.write(json_object)

    print("Do you want to add product to the inventory again? ")
    print("Type Y/y for YES and N/n for NO ")
    ch = input("Enter Y/y or N/n: ")
    if (ch == "Y" or ch == "y"):
        choice = True
    elif (ch == "N" or ch == "n"):
        choice = False