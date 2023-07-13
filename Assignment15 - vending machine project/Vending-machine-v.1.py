class vending_machine:
    product_stock = [{'Product_id': 1, 'Product_name': 'Coke ', 'Price': 40},
                     {'Product_id': 2, 'Product_name': 'Pepsi', 'Price': 35},
                     {'Product_id': 3, 'Product_name': '7Up  ', 'Price': 36},
                     {'Product_id': 4, 'Product_name': 'Maaza', 'Price': 30},
                     {'Product_id': 5, 'Product_name': 'Coffee', 'Price': 25},
                     {'Product_id': 6, 'Product_name': 'Milk', 'Price': 20}]
    balance = 0
    cart = {}
    itemlist = []

    def display_menu(self):
        print("******************************")
        print("WELCOME TO THE VENDING MACHINE")
        print("******************************")
        for i in range(len(self.product_stock)):
            print(f"{self.product_stock[i]['Product_id']}\t{self.product_stock[i]['Product_name']}\t\t{self.product_stock[i]['Price']}")
            # print(f"No:{self.product_stock[0]}\tItem:{self.product_stock[1]}\t\tPrice:{self.product_stock[2]}")
        print("******************************")
        print()
        print()

    def display_coin_menu(self):
        print("Enter the required coins in vending machine\n1. 1-Rs Coin\n2. 2-Rs Coin\n3. 5-Rs Coin\n4. 10-Rs Coin")

    def input_money(self, input, no_of_coin):
        self.user_input = input
        self.no_of_coin = no_of_coin
        if self.user_input == 1:
            self.total_amt = self.no_of_coin * 1
        elif self.user_input == 2:
            self.total_amt = self.no_of_coin * 2
        elif self.user_input == 3:
            self.total_amt = self.no_of_coin * 5
        elif self.user_input == 4:
            self.total_amt = self.no_of_coin * 10
        self.balance += self.total_amt
        print(f"The amount of money entered in vending machine:{self.balance}Rs")
        print()

    def display_balance(self):
        print("******************************")
        print(f"The balance amount is {self.balance}")
        print("******************************")

    def display_choice(self):
        print("******************************")
        print("Choice_Menu")
        print("1.Insert coins in machine:\n2.Purchase item\n3.Show Balance\n4.Exit")
        print("******************************")

    def purchase_items(self, item_no):
        self.item_no = item_no
        for i in self.product_stock:
            self.itemlist.append(i['Product_id'])
        # print(self.itemlist)
        if self.item_no in range(1, len(self.itemlist) + 1):
            price = self.product_stock[self.item_no - 1]['Price']
            if self.balance >= price:
                self.balance -= price
                print(f"Dispensing {self.product_stock[self.item_no - 1]['Product_name']}\nEnjoy your Drink!!!")
            else:
                print("Insufficient balance. Please insert more coins.")
        else:
            print(f"Items_no {self.item_no} not available in machine")

    def return_amt(self):
        print(f"Returning the remaining balance:{self.balance}")


# =============================================================================
obj = vending_machine()
while True:
    obj.display_menu()
    obj.display_choice()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        obj.display_coin_menu()
        obj.input_money(int(input("Enter the coin type:")), int(input("Enter the no of coins:")))
        # print("Do you want to enter more coins:\n1.Yes\n2.No")
        # z = int(input())
        # if z == 1:
        #     continue
        # else:
        #     break
    elif choice == 2:
        item = int(input("Enter the choice of item from vending machine"))
        obj.purchase_items(item)
    elif choice == 3:
        obj.display_balance()
        print()
    elif choice == 4:
        print("Thankyou for using our Vending machine!!!\nDo Visit Next time!!!")
        obj.return_amt()
        break
