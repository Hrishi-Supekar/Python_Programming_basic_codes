Grocery_prod_dict = {'1': {'Product_Name': 'Milk   ', 'Stock': '100  ', 'Individual_Price': '72'},
                     '2': {'Product_Name': 'Bread  ', 'Stock': '100  ', 'Individual_Price': '40'},
                     '3': {'Product_Name': 'Eggs   ', 'Stock': '1000 ', 'Individual_Price': '60'},
                     '4': {'Product_Name': 'Biscuit', 'Stock': '100  ', 'Individual_Price': '10'},
                     '5': {'Product_Name': 'Maggi  ', 'Stock': '1000 ', 'Individual_Price': '15'},
                     '6': {'Product_Name': 'Wheat  ', 'Stock': '50000', 'Individual_Price': '32'},
                     '7': {'Product_Name': 'Rice   ', 'Stock': '40000', 'Individual_Price': '50'},
                     '8': {'Product_Name': 'Dal    ', 'Stock': '13000', 'Individual_Price': '40'},
                     '9': {'Product_Name': 'Papad  ', 'Stock': '5000 ', 'Individual_Price': '70'},
                     '10': {'Product_Name': 'Oil   ', 'Stock': '30000', 'Individual_Price': '120'}
                     }  # Hard coded Dictionary with products
cart = {}
price_cart = {}


def main_menu():
    z = 1  # Initialization for while loop
    while z in range(1, 4):  # If value enter other than 1-3 than loop runs again
        print("=======Main Menu=========\n"
              "Welcome to Grocery Store:\n"
              "1.Customer:\n2.Staff:\n3.Exit\n"
              "=========================")
        n = int(input("Enter the Application User:"))
        if n == 1:
            customer(price_cart, cart)
        elif n == 2:
            staff()
        elif n == 3:  # Exit from App from main menu
            print("Thankyou for using the Application\nVisit Again!!")
            break
        else:  # Invalid input and continue the loop with main menu
            print("Invalid input!!\nTry again")
    z = 1  # For continues looping


def display_product_list():  # This function is used for display of products
    print("==========Product List===========")
    # print("Product_ID\tProduct_Name\tProduct_Stock\tIndividual_Price")
    for x, y in Grocery_prod_dict.items():
        print(f"Product_ID:{x}\nProduct_Name:{y['Product_Name']}\nProduct_Stock:{y['Stock']}\nIndividual_Price:{y['Individual_Price']}")
        print("--------------------------------------------------")


def display_product_id():
    for x, y in Grocery_prod_dict.items():
        print(f"Id:{x}::{y['Product_Name']}")


def display_prod_qty(p_id):
    for x, y in Grocery_prod_dict.items():
        if x == p_id:
            print(f"Id:{y['Product_Name']}::{y['Stock']}")


def display_price_cart(x):
    for i, j in x.items():
        for x, y in Grocery_prod_dict.items():
            if i == x:
                price_cart.update(
                    {i: j * int(y['Individual_Price'])})  # Used for adding key and individual price x qty in price_dict
    print(price_cart)


def add_cart_items():
    display_product_id()
    p_id = input("Enter the product id to add to cart:")
    display_prod_qty(p_id)
    stock = int(input("Enter the quantity you want:"))
    cart.update({p_id: stock})


def bill_cart(cart):
    price_cart.clear()
    for i, j in cart.items():
        price_cart.update({i: j * int(Grocery_prod_dict[i]['Individual_Price'])})  # Used for adding key and individual price x qty in price_dict
    print(price_cart)


def remove_cart_items(P_id):
    cart.pop(P_id)
    print(cart)


def billing_the_cart():
    pass


def customer(price_cart, cart):
    t = 1  # Initialization for while loop
    while t in range(1, 5):
        print("======Customer Menu======\n"
              "1.Product list:\n2.Add Product to cart:\n3:Display cart\n4.Remove product from cart:\n"
              "5.Bill payment\n6.Exit from App:\n"
              "=========================")
        x = int(input("Enter the choice of operation:"))
        if x == 1:  # Display Product list
            display_product_list()
        elif x == 2:  # Add new Product to customer cart
            for p_id, stock in Grocery_prod_dict.items():
                i = 'Y'
                while i == 'Y' or i == 'y':
                    add_cart_items()
                    i = input("Do you want to continue:\nPress Y=Yes or N=No")
                else:
                    break
            display_price_cart(cart)
        elif x == 3:
            display_price_cart(cart)
        elif x == 4:  # Remove specific product from cart
            P_id = input("Enter the product id to Remove from the cart:")
            remove_cart_items(P_id)
            bill_cart(cart)
        elif x == 5:  # Billing the cart
            if cart == {}:
                print("The cart is empty!!!")
                continue
            else:
                sum = 0
                for x in price_cart.values():
                    sum += x  # Adding the values from price_cart1(means the amount of cart is totaled)
                print(f"Request you to pay the amount of Rs.{sum}")
                bill_pay = int(input("Enter the amount to be paid:"))
                if bill_pay == sum:
                    for key, val in Grocery_prod_dict.items():  # To update the grocery stock
                        for l, k in cart.items():
                            if key == l:
                                for c, v in val.items():
                                    if c == 'Stock':
                                        val[c] = int(val[c]) - k
                    # display_product_list()
                    print("The correct amount received!!!\nThankyou for shopping!!!")
                    price_cart.clear()
                    cart.clear()
                    # break
                else:
                    print("Incorrect amount!!\nPlease try again!!")
        elif x == 6:  # Exit from App
            print("Do yo want to continue to main menu:")
            h = int(input("Enter the choice:\n1.Yes\n2.No\n"))
            if h == 1:
                z = 1  # for looping the main menu
                t = 8  # for stopping the loop of customer menu
            else:
                print("Thankyou for using the Application\nVisit Again!!")
                z = 5  # For stopping the loop of main menu
                break
        else:  # Invalid input and continue the loop with customer menu
            print("Invalid input!!\nTry again")


def staff():
    f = 1  # Initialization for while loop
    while f in range(1, 5):
        print("======Staff Menu======\n"
              "1.Add new Product:\n2.Display Product Stock:\n3.Update specific Product:\n"
              "4.Delete specific product from list:\n5.Exit from App\n"
              "=========================")
        x = int(input("Enter the choice of operation:"))
        if x == 1:  # Add new product in stock
            for x, y in Grocery_prod_dict.items():
                print(f"{x}:{y}")
            key = input("Enter the product_id:")
            val = {}
            # num = int(input("Enter the number of elements to add:"))
            for x in range(3):
                k = input("Enter the key:")
                v = input("Enter the value:")
                val.update({k: v})
            Grocery_prod_dict.update({key: val})
        elif x == 2:  # Display Product stock
            display_product_list()
        elif x == 3:  # Update specific product details
            q1 = input("Enter the Key:")
            a2 = input("Enter the inner key:")
            b3 = input("Enter the change of value:")
            for key1, val1 in Grocery_prod_dict.items():  # to update the stock
                if key1 == q1:
                    for k1 in val1.keys():
                        if k1 == a2:
                            val1[k1] = b3
                            # print(val1[k1])
            display_product_list()
        elif x == 4:  # Remove specific product from product list
            copy_dic = Grocery_prod_dict.copy()
            key = input("Enter the product_id which you want to remove:")
            for i in copy_dic.keys():
                if i == key:
                    Grocery_prod_dict.pop(key)
            display_product_list()
        elif x == 5:  # Exit from App
            print("Do yo want to continue to main menu:")
            h = int(input("Enter the choice:\n1.Yes\n2.No\n"))
            if h == 1:
                z = 1
                f = 8
            else:
                print("Thankyou for using the Application\nVisit Again!!")
                z = 5
                break
        else:  # Invalid input and continue the loop with Staff menu
            print("Invalid input!!\nTry again")


main_menu()
