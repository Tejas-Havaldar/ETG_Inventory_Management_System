import json

with open("stock.json", "r") as f:
    r = f.read()

stock = json.loads(r)

print("Welcome to the store")
Choice = True
while Choice:
    print("Product ID are in between 1001 to 1030 both including")
    prod_id = str(int(input("Enter the product ID ")))
    if prod_id in stock.keys():
        print(stock[prod_id])
    else:
        print("The given ID does not exist.\nPlease type again ")
    quan = int(input("Please enter the Quantity: "))

    if prod_id in stock.keys():
        if quan > int(stock[prod_id]['Quantity']):
            print("The entered Quantity exceeds the storage")
        else:
            print("Product: ", stock[prod_id]['Name'])
            print("Price: ", stock[prod_id]['Price'])
            print("Billing Amount: ", int(stock[prod_id]['Price']) * quan)
            num = int(input("Enter the transaction number:"))
            sales = {
                num: {'product': prod_id, 'quantity': quan, 'amount': int(stock[prod_id]['Price']) * quan}}
            sales = json.dumps(sales)
            with open("sales.json", 'a') as sj:
                sj.write(sales)
            stock[prod_id]['Quantity'] -= quan
            print("After Updation: ")
            print(stock[prod_id])
            json_object = json.dumps(stock)
            with open("stock.json", "w") as f:
                f.write(json_object)

    print("If you want to continue shopping please enter y or else n")
    x = input("Please enter your choice")

    if x == 'y' or x == 'Y':
        Choice = True
    elif x == 'n' or x == 'N':
        Choice = False

