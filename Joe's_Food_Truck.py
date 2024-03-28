#Joe's Food Truck
# Empty list to store customers order
order_list = []
# Menu section
menu_categories = {
    1:  ("pizza"),
    2:  {"pasta"},
    3:  {"burrito"},
    4:  {"smoothie"},
    5:  {"beverage"}
}
print(menu_categories)
# Sub-menus
pizza_menu = {
    1: {"item name": "cheese", "price": 7.99},
    2: {"item name": "pepperoni", "price": 8.99},
    3: {"item name": "vegan", "price": 5.99},
    4: {"item name": "Hawaiian", "price": 10.99}
}
print(pizza_menu)

pasta_menu = {
    1: {"item name": "spaghetti", "price": 6.99},
    2: {"item name": "gnocchi", "price": 6.99},
    3: {"item name": "penne", "price": 5.99}
}
print(pasta_menu)

burrito_menu = {
    1: {"item name": "chicken", "price": 8.99},
    2: {"item name": "beef", "price": 6.99},
    3: {"item name": "bean and cheese", "price": 4.99}
}
print(burrito_menu)

smoothie_menu = {
    1: {"item name": "strawberry", "price": 4.99},
    2: {"item name": "chocolate", "price": 3.99},
    3: {"item name": "vanilla", "price": 2.99}
}
print(smoothie_menu)

beverage_menu = {
    1: {"item name": "soda", "price": 1.89},
    2: {"item name": "water", "price": 1.25},
    3: {"item name": "juice", "price": 2.99}
}
print(beverage_menu)

menu_items= {
    "pizza": pizza_menu,
    "pasta": pasta_menu,
    "burrito": burrito_menu,
    "smoothie": smoothie_menu,
    "beverage": beverage_menu
}
print(menu_items)

pizza_items = list(pizza_menu.keys())
pasta_items = list(pasta_menu.keys())
burrito_items = list(burrito_menu.keys())
smoothie_items = list(smoothie_menu.keys())
beverage_items = list(beverage_menu.keys())

# Combine all the keys into a single list
item_name = pizza_items + pasta_items + burrito_items + smoothie_items + beverage_items

print("Item Names:", item_name)

if menu_categories == 1:
    print(pizza_menu)
    for index, item in enumerate(menu_items["pizza"], start=1):
        print(f"{index}: {item}")
elif menu_categories == 2:
    print(pasta_menu)
    for index, item in enumerate(menu_items["pasta"], start=1):
        print(f"{index}: {item}")
elif menu_categories == 3:
    print(burrito_menu)
    for index, item in enumerate(menu_items["burrito"], start=1):
        print(f"{index}: {item}")
elif menu_categories == 4:
    print(smoothie_menu)
    for index, item in enumerate(menu_items["smoothie"], start=1):
        print(f"{index}: {item}")
elif menu_categories == 5:
    print(beverage_menu)
    for index, item in enumerate(menu_items["beverage"], start=1):
        print(f"{index}: {item}")

print("Welcome to Joe\'s Food Truck!")

menu_dashes = "-" * 42

menu_selection = input("Choose an option", menu_categories ,  "to get started")
# Prompting a customer to enter a selection from menu
print("You selected", menu_categories)
if not menu_categories.isdigit():
    print("Error: Please enter a valid number.")
else:
    # Convert the input to an integer
    menu_categories = int(menu_categories)
    
    # Check if the menu selection is in the keys of menu_items
    if menu_selection not in menu_categories.keys():
        print("Error: Please enter a valid menu item number.")
    else:
        # Process the selected menu item
        selected_item = menu_categories[menu_selection]
        print("You selected:", selected_item)
while True:
    # ask the customer which menu they'd like to view
    print("Which menu would you like to view?")
    i = 1
    menu_categories = {}

    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu_items.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for key, value in menu_items[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
            
            print(menu_dashes)
            input("Press enter to return to the main menu.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
    while True:
        user_input = input("Would you like place another order, (y/n)").lower
        if user_input == 'y': 
            menu_categories
            break  # Exit the loop
        elif user_input == 'n':
            print("Thank you for your order.")
            break  # Exit the loop
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while True:
    quantity_input = input(f"How many {item_name} would you like to order? (default is 1): ")

    # Check if the input is empty or non-numeric, or less than 1
    if not quantity_input or not quantity_input.isdigit() or int(quantity_input) < 1:
        print("Invalid input. Quantity must be 1 or greater. Quantity set to default (1).")
        break
    else:
        # Convert the input to an integer
        quantity = int(quantity_input)
        break

print("Quantity selected:", quantity)

price = selected_item["price"]
# Create a dictionary for the order
order = {
    "Item name": item_name,
    "Price": price,
    "Quantity": quantity
}

# Append the order to the order list
order_list.append(order)

# Order Receipt
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    
    print(f"Item name: {item_name}, Price: {price}, Quantity: {quantity}")       

item_name_space = " " * 25
price_space = " " * 8
quantity_space = " " * 9

# Print the header line for the receipt
print(f"Item name{item_name_space}| Price{price_space}| Quantity")
print("-" * 51)  

# Iterate through the order list and print each item
total_price = sum(item["Price"] * item["Quantity"] for item in order_list)
for item in order_list:
    # Extract item details
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    
    # Print item details with proper spacing
    print(f"{item_name.ljust(25)}| ${price:.2f}".ljust(33) + f"| {quantity}".ljust(10))

# Display total price to the customer
print("-" * 51) 
print(f"Total Price: ${total_price:.2f}")
