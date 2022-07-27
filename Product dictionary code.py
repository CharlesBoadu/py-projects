product_dictionary = {}
for i in range(5):
    product = input("Enter a product: ")
    price = eval(input("Enter a price: "))
    product_dictionary[product] = price

print(product_dictionary)

dollar_amount = eval(input("Enter a dollar amount: "))
for product in product_dictionary:
    if product_dictionary[product] < dollar_amount:
        print("The price of", product, "is less than the dollar amount")

