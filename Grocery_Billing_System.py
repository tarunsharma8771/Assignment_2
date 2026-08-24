# --------------------------------------------------
# GROCERY BILLING SYSTEM
# --------------------------------------------------

# Dictionary to store available stock
# Key   -> Item Name
# Value -> Available Quantity
stock = {
    "Rice": 10,
    "Milk": 20,
    "Bread": 15,
    "Sugar": 8
}

# Dictionary to store price of each item
# Key   -> Item Name
# Value -> Price per unit
price = {
    "Rice": 60,
    "Milk": 30,
    "Bread": 40,
    "Sugar": 50
}

# Empty list to store all purchased items
# Each item added to bill will be stored as a tuple:
# (item_name, quantity, price_per_unit)
bill = []


# Infinite loop - keeps accepting items
# until the user enters "done"
while True:

    print("\n--- Available Items ---")

    # Traverse all item names in the stock dictionary
    for item in stock:

        print(
            item,
            "- Price:",
            price[item],       # Get price using dictionary key
            "- Stock:",
            stock[item]        # Get available quantity
        )


    item_name = input("\nEnter Item Name or 'done' to finish: ")


    # Stop taking items when user enters "done"
    if item_name == "done":
        break


    # Check whether the entered item exists
    # as a key in the stock dictionary
    if item_name in stock:

        quantity = int(input("Enter Quantity: "))


        # Check whether enough stock is available
        if quantity <= stock[item_name]:

            # Get price of selected item
            # using the item name as dictionary key
            price_per_unit = price[item_name]


            # Create a tuple for one bill entry
            # Tuple contains:
            # (Item Name, Quantity, Price per Unit)
            bill_entry = (
                item_name,
                quantity,
                price_per_unit
            )


            # Add the tuple to the bill list
            bill.append(bill_entry)


            # Reduce purchased quantity from available stock
            stock[item_name] = stock[item_name] - quantity

            print("Item added to bill.")

        else:
            print("Insufficient stock.")

    else:
        print("Item not available.")


# --------------------------------------------------
# CALCULATE FINAL BILL
# --------------------------------------------------

# Variable to store total amount of all purchased items
total_bill = 0

print("\n--- Final Bill ---")


# Traverse each tuple stored inside the bill list
for entry in bill:

    # entry is a tuple:
    # (item_name, quantity, price_per_unit)

    # Index 0 contains Item Name
    item_name = entry[0]

    # Index 1 contains Quantity
    quantity = entry[1]

    # Index 2 contains Price per Unit
    price_per_unit = entry[2]


    # Calculate amount for one item
    item_total = quantity * price_per_unit


    # Add item amount to the final bill
    total_bill = total_bill + item_total


    print(
        item_name,
        quantity,
        "x",
        price_per_unit,
        "=",
        item_total
    )


print("---------------------")
print("Total Bill =", total_bill)