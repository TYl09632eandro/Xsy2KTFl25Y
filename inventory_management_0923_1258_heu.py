# 代码生成时间: 2025-09-23 12:58:27
import numpy as np

"""
Inventory Management System

This system provides functionality to manage an inventory of items, including
adding, removing, updating, and querying inventory items.
"""

class InventoryItem:
    """Represents a single item in the inventory."""
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}"

class InventoryManager:
    """Manages a collection of inventory items."""
    def __init__(self):
        self.items = {}  # Use a dictionary to store items by their ID

    def add_item(self, item_id, name, quantity):
        """Add a new item to the inventory."""
        if item_id in self.items:
            raise ValueError(f"Item with ID {item_id} already exists.")
        self.items[item_id] = InventoryItem(item_id, name, quantity)

    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist.")
        del self.items[item_id]

    def update_item(self, item_id, quantity):
        """Update the quantity of an existing item in the inventory."""
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist.")
        self.items[item_id].quantity = quantity

    def get_item(self, item_id):
        """Retrieve an item's details from the inventory."""
        return self.items.get(item_id, None)

    def list_items(self):
        """List all items in the inventory."""
        for item in self.items.values():
            print(item)

    def total_inventory(self):
        """Calculate the total number of items in the inventory."""
        total = 0
        for item in self.items.values():
            total += item.quantity
        return total

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    try:
        manager.add_item(1, "Widget", 100)
        manager.add_item(2, "Gadget", 50)
        manager.add_item(3, "Thingamajig", 75)
        print("Total inventory:", manager.total_inventory())
        manager.update_item(2, 60)
        print("Item 2 after update:", manager.get_item(2))
        manager.remove_item(3)
        print("Total inventory after removal:", manager.total_inventory())
        manager.list_items()
    except ValueError as ve:
        print(ve)
    except KeyError as ke:
        print(ke)