products = {
    "R01": 32.95,
    "G01": 24.95,
    "B01": 7.95
}

cart = []


def add(code):
    if code in products:
        cart.append(code)
        print(f"Item {code} added to cart.")
    else:
        print("Item not found. Please check the product code.")


def remove(code):
    if code in cart:
        cart.remove(code)
        print(f"Item {code} removed from cart.")
    else:
        print("Item not found in cart.")


def calculate_total():
    item_counts = {code: cart.count(code) for code in set(cart)}
    subtotal = 0.0

    if "R01" in item_counts:
        r01_count = item_counts["R01"]
        half_price_units = r01_count // 2
        full_price_units = r01_count - half_price_units
        subtotal += (full_price_units * products["R01"]) + (half_price_units * (products["R01"] / 2))
    else:
        r01_count = 0

    for code, count in item_counts.items():
        if code != "R01":
            subtotal += count * products[code]

    if subtotal < 50:
        delivery = 4.95
    elif subtotal < 90:
        delivery = 2.95
    else:
        delivery = 0.0

    total_cost = subtotal + delivery
    return round(total_cost, 2)


def ui():
    while True:
        action = input("\n1. Add item\n2. Remove item\n3. View cart\n4. See total cost\n5. Exit\nChoose an option: ")

        if action == "1":
            code = input("Enter item code: ").strip().upper()
            add(code)

        elif action == "2":
            code = input("Enter item code: ").strip().upper()
            remove(code)

        elif action == "3":
            print("Current cart:", cart)

        elif action == "4":
            print("Total cost:", calculate_total())

        elif action == "5":
            print("Exiting...")
            break

        else:
            print("Invalid input, please choose from the options.")


ui()
