class ItemToPurchase: 
    #Constructor
    def __init__(self):
        self.name = "none"
        self.description = "none"
        self.price = 0.0
        self.quantity = 0

    #Calculates and prints item cost
    def print_item_cost(self):
        total_cost = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total_cost:.2f}")   

    #Prints item description
    def print_item_description(self):
        print(f"{self.name}: {self.description}")


class ShoppingCart: 
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].name == item_name:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.name == item_to_purchase.name:
                # Only modify if not default values
                if item_to_purchase.description != "none":
                    item.description = item_to_purchase.description
                if item_to_purchase.price != 0.0:
                    item.price = item_to_purchase.price
                if item_to_purchase.quantity != 0:
                    item.quantity = item_to_purchase.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            print()
            return

        for item in self.cart_items:
            item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():.2f}")
        print()

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
        print()


def print_menu(cart):
    choice = ""

    while choice != "q":
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n").strip().lower()

        while choice not in ["a", "r", "c", "i", "o", "q"]:
            choice = input("Choose an option:\n").strip().lower()

        if choice == "a":
            print("ADD ITEM TO CART")
            item = ItemToPurchase()
            item.name = input("Enter the item name:\n")
            item.description = input("Enter the item description:\n")
            item.price = float(input("Enter the item price:\n"))
            item.quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(item)
            print()

        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
            print()

        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            temp_item = ItemToPurchase()
            temp_item.name = name
            temp_item.quantity = qty
            cart.modify_item(temp_item)
            print()

        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


main()
