"""Inventory Management System."""

import ast

stock_data = {}


def add_item(item, qty=None):
    """Add a new item to the stock."""
    if qty is None:
        qty = []
    stock_data[item] = qty
    print(f"Added {item} with quantity {qty}")


def remove_item(item):
    """Remove an item from the stock if it exists."""
    try:
        del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")


def get_qty(item):
    """Get quantity of an item."""
    return stock_data.get(item, "Item not found")


def load_data(filename):
    """Load stock data from a file safely."""
    global stock_data
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            stock_data = ast.literal_eval(data)  # safe alternative to eval
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except (ValueError, SyntaxError):
        print("Invalid data format in file.")


def save_data(filename):
    """Save stock data to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(stock_data))


def print_data():
    """Print all items and their quantities."""
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def check_low_items(threshold):
    """Check for items below the given quantity threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if low_items:
        print("Low stock items:", ", ".join(low_items))
    else:
        print("All items are sufficiently stocked.")


if __name__ == "__main__":
    add_item("Apples", 50)
    add_item("Oranges", 20)
    remove_item("Bananas")
    print_data()
    # safer alternative to eval
    ast.literal_eval("{'msg': 'safe test'}")
