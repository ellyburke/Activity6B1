def helloWorld(name):
    print("Hello " + name)

def addTax(price):
    TAX = 1.13
    return price*TAX

def main():
    name = input("Please enter your name: ")
    helloWorld(name)

    # Adding tax to price
    price = float(input("Enter item price: "))
    taxedPrice = addTax(price)
    print("The price with tax is: " + str(taxedPrice))

main()