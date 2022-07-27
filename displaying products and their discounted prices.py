product_list = []
discount_list = []

for i in range(10):
    product = input("Enter a product: ")
    price = eval(input("Enter a price: "))
    discount = 11/100 * price
    product_list.append(product)
    discount_list.append(discount)

for i in range(len(product_list)):
    print('{:<10s}         ${:5.2f}'.format(product_list[i], discount_list[i]))
