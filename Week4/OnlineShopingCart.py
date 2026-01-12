class ItemToPurchase: 
    #Constructor
    def __init__(self):
        self.name = "none"
        self.price = 0.0
        self.quantity = 0
    #Calculates and prints item cost
    def print_item_cost(self):
        total_cost = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total_cost:.2f}")   

def main():
    #Creates ItemToPurchase objects using the class constructor
    item1 = ItemToPurchase()
    item1.name = str(input("Please enter your item name: "))
    item1.price = float(input("Please enter the item price: "))
    item1.quantity = int(input("Please enter the item quantity: "))
        
    item2 = ItemToPurchase()
    item2.name = str(input("Please enter your item name: "))
    item2.price = float(input("Please enter the item price: "))
    item2.quantity = int(input("Please enter the item quantity: "))
        
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    #Calculates the total price 
    total = (item1.price * item1.quantity) + (item2.price * item2.quantity)
    print(f"Total: ${total:.2f}")
main()