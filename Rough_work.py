# # To remove all extra duplicate element form original list and create new list of that  duplicate element:
# l = [1, 2, 3, 4, 5, 6, 6, 2, 3, 8, 9, 5, 5, 2, 2, 1, 2, 3,1,1,1,1,2,3]
# copy = l
# l1 = []
# for i in copy:
#     if copy.count(i) > 1:
#         # print(copy.count(i),end=" ")
#         for x in range(copy.count(i)-1):
#             l.remove(i)
#             l1.append(i)
# print(l)
# print(l1)
# ======================================================================================================
# class VendingMachine:
#     def __init__(self):
#         self.items = {
#             "Coke": 1.50,
#             "Chips": 1.25,
#             "Candy": 0.75,
#             "Water": 1.00,
#         }
#         self.balance = 0.0
#
#     def display_items(self):
#         print("Available Items:")
#         for item, price in self.items.items():
#             print(f"{item} - ${price:.2f}")
#
#     def insert_coin(self, amount):
#         self.balance += amount
#
#     def purchase_item(self, item_name):
#         if item_name in self.items:
#             price = self.items[item_name]
#             if self.balance >= price:
#                 self.balance -= price
#                 print(f"Dispensing {item_name}. Enjoy!")
#             else:
#                 print("Insufficient balance. Please insert more coins.")
#         else:
#             print(f"Item '{item_name}' not available in the vending machine.")
#
#     def get_balance(self):
#         return self.balance
#
#
# def main():
#     vending_machine = VendingMachine()
#
#     while True:
#         print("\nWelcome to the Vending Machine!")
#         vending_machine.display_items()
#
#         try:
#             choice = int(input("\nInsert coins (1) or purchase item (2) or exit (3): "))
#         except ValueError:
#             print("Invalid choice. Please try again.")
#             continue
#
#         if choice == 1:
#             try:
#                 coins = float(input("Insert coins (e.g., 0.25, 0.5, 1, 2): "))
#                 if coins > 0:
#                     vending_machine.insert_coin(coins)
#                 else:
#                     print("Invalid coin amount. Please insert valid coins.")
#             except ValueError:
#                 print("Invalid coin amount. Please insert valid coins.")
#
#         elif choice == 2:
#             item = input("Enter the name of the item you want to purchase: ")
#             vending_machine.purchase_item(item)
#
#         elif choice == 3:
#             print("Thank you for using the Vending Machine. Have a great day!")
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()

# ====================
product_stock = [{'Product_id': 1, 'Product_name': 'Coke ', 'Price': 40},
                     {'Product_id': 2, 'Product_name': 'Pepsi', 'Price': 35},
                     {'Product_id': 3, 'Product_name': '7Up  ', 'Price': 36},
                     {'Product_id': 4, 'Product_name': 'Maaza', 'Price': 30},
                     {'Product_id': 5, 'Product_name': 'Coffee', 'Price': 25},
                     {'Product_id': 6, 'Product_name': 'Milk', 'Price': 20}]
for i in product_stock:
    print(i['Product_id'])