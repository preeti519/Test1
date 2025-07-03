def handle_transaction():
    try:
        # User selects product and quantity
        product_id = int(input("Enter product ID to buy: "))
        
        # Ensure the product exists
        if product_id not in product:
            print("Invalid Product ID! Please try again.")
            return
        
        # Ask for quantity with the updated prompt
        quantity = int(input("Enter the quantity you want to buy for " + product[product_id]['name'] + ": "))
        
        # Check if there is enough stock
        if product[product_id]["quantity"] < quantity:
            print("Sorry, not enough stock of " + product[product_id]['name'] + "!")
            return
        
        # Apply the 'buy 3 get 1 free' policy
        free_items = quantity // 3
        total_items = quantity + free_items
        
        # Update the stock in memory
        product[product_id]["quantity"] -= total_items
        
        # Calculate total price
        selling_price = product[product_id]["cost_price"] * 2
        total_price = total_items * selling_price
        
        print("\nTransaction Successful!\nYou bought " + str(total_items) + " items of " + product[product_id]['name'] + "!")
        print("Total Price: " + str(total_price))
        
        # Generate an invoice and save to a file
        with open("invoice.txt", "a") as invoice_file:
            invoice_file.write("Product: " + product[product_id]['name'] + ", Quantity: " + str(total_items) + ", Total Price: " + str(total_price) + "\n")
            invoice_file.write("-" * 40 + "\n")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Main logic to handle transactions
while True:
    display_products()  # Display available products
    handle_transaction()  # Handle the transaction
    another = input("Do you want to make another transaction? (yes/no): ")
    if another.lower() != "yes":
        break

# After all transactions, update the product file with the new stock levels
with open("product.txt", "w") as file:
    for pid, details in product.items():
        line = details['name'] + "," + details['brand'] + "," + str(details['cost_price']) + "," + \
               str(details['quantity']) + "," + details['country'] + "\n"
        file.write(line)

print("Stock updated and product data saved!")
