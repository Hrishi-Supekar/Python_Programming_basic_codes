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


def Display_product_list():
    print("==========Product List===========")
    print("Product_ID\tProduct_Name\tProduct_Stock\tIndividual_price")
    for x, y in Grocery_prod_dict.items():
        print(f"\t{x}\t\t\t{y['Product_Name']}\t\t\t{y['Stock']}\t\t\t{y['Individual_Price']}")
    print("=====================================================")


cart = {}
price_cart = {}
z = 1  # Initialization for while loop
while z in range(1, 4):  # If value enter other than 1-3 than loop runs again
    print("=======Main Menu=========\n"
          "Welcome to Grocery Store:\n"
          "1.Customer:\n2.Staff:\n3.Exit\n"
          "=========================")
    n = int(input("Enter the Application User:"))
    # =====================================Customer_Program===========================================================
    if n == 1:
        t = 1  # Initialization for while loop
        while t in range(1, 5):
            print("======Customer Menu======\n"
                  "1.Product list:\n2.Add Product to cart:\n3.Remove product from cart:\n4.Bill payment\n5.Exit from App:\n"
                  "=========================")
            x = int(input("Enter the choice of operation:"))
            if x == 1:  # Display Product list
                Display_product_list()
            elif x == 2:  # Add new Product to customer cart
                for p_id, stock in Grocery_prod_dict.items():
                    i = 'Y'
                    while i == 'Y' or i == 'y':
                        p_id = input("Enter the product id to add to cart:")
                        stock = int(input("Enter the quantity you want:"))
                        cart.update({p_id: stock})
                        i = input("Do you want to continue:\nPress Y=Yes or N=No")
                    else:
                        break
                for i, j in cart.items():
                    for x, y in Grocery_prod_dict.items():
                        if i == x:
                            price_cart.update({i: j * int(y['Individual_Price'])})
                for f in Grocery_prod_dict.values():
                    for l, m in f.items():
                        if l == 'Stock' and f == i:
                            Grocery_prod_dict.update({int(m) - stock})
                print(price_cart)
            elif x == 3:  # Remove specific product from cart
                P_id = input("Enter the product id to Remove from the cart:")
                cart.pop(P_id)
                for i, j in cart.items():  # To again print the cart value
                    for x, y in Grocery_prod_dict.items():
                        if i == x:
                            price_cart.update({i: j * int(y['Individual_Price'])})
                for f in Grocery_prod_dict.values():
                    for l, m in f.items():
                        if l == 'Stock' and f == i:
                            Grocery_prod_dict.update({int(m) - stock})
                print(price_cart)
            elif x == 4:  # Billing the cart
                if cart == {}:
                    print("The cart is empty!!!")
                    continue
                else:
                    sum = 0
                    for x in price_cart.values():
                        sum += x
                    print(f"Request you to pay the amount of Rs.{sum}")
                    bill_pay = int(input("Enter the amount to be paid:"))
                    if bill_pay == sum:
                        for key, val in Grocery_prod_dict.items():  # To update the grocery stock
                            for l, k in cart.items():
                                if key == l:
                                    for c, v in val.items():
                                        if c == 'Stock':
                                            val[c] = int(val[c]) - k
                        Display_product_list()
                        print("The correct amount received!!!\nThankyou for shopping!!!")
                    else:
                        print("Incorrect amount!!\nPlease try again!!")
            elif x == 5:  # Exit from App
                print("Thankyou for using the Application\nVisit Again!!")
                break
            else:  # Invalid input and continue the loop with customer menu
                print("Invalid input!!\nTry again")
                t = 1  # For continues looping of customer menu
    # ====================================Staff_Program========================================================
    elif n == 2:
        f = 1
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
                Display_product_list()
            elif x == 3:  # Update specific product details
                key = input("Enter the Specific Product key for which you want to update data:")
                for j, k in Grocery_prod_dict.items():
                    if key == j:
                        i_key = input("Enter the inner key:")
                        i_val = input("Enter the inner value:")
                        for l, m in k.items():
                            if i_key == l:
                                k.update({i_key: i_val})
            elif x == 4:  # Remove specific product from product list
                copy_dic = Grocery_prod_dict.copy()
                key = input("Enter the product_id which you want to remove:")
                for i in copy_dic.keys():
                    if i == key:
                        Grocery_prod_dict.pop(key)
                Display_product_list()
            elif x == 5:  # Exit from App
                print("Thankyou for using the Application\nVisit Again!!")
                break
            else:  # Invalid input and continue the loop with Staff menu
                print("Invalid input!!\nTry again")
                f = 1  # For continues looping of customer menu
    # ======================================================================================================
    elif n == 3:  # Exit from App from main menu
        print("Thankyou for using the Application\nVisit Again!!")
        break
    else:  # Invalid input and continue the loop with main menu
        print("Invalid input!!\nTry again")
        z = 1  # For continues looping
