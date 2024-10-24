
rooms = {
    "STAIRWELL": {"West": "STORAGE ROOM", "North": "KITCHEN"},
    "STORAGE ROOM": {"East": "STAIRWELL"},
    "KITCHEN": {"East": "DINING ROOM", "South": "STAIRWELL", "North": "WAITING ROOM"},
    "ARMORY": {"East": "WAITING ROOM"},
    "DINING ROOM": {"West": "KITCHEN"},
    "WAITING ROOM": {"West": "ARMORY", "South": "KITCHEN", "North": "RECEPTION ROOM"},
    "RECEPTION ROOM": {"South": "WAITING ROOM", "East": "KNIGHT BEDROOM"},
    "POTION CENTER": {"West": "KNIGHT BEDROOM"},
    "THRONE ROOM": {"South": "RECEPTION ROOM"}
}

# Define items in each room
items = {
    "STORAGE ROOM": "Enchanted shield",
    "KITCHEN": "Mythical Mint",
    "DINING ROOM": "Cedrick's Katana",
    "WAITING ROOM": "Knight's Helmet",
    "ARMORY": "Silver Gauntlet",
    "RECEPTION ROOM": "Knight's Leggings",
    "KNIGHT BEDROOM": "Knight's Chestplate",
    "POTION CENTER": "Grizzly's Potion"
}

# Initialize player inventory
inventory = []

# Function to show instructions
def show_instructions():
    print("Medieval Warrior Adventure Game")
    print("Collect 8 items to win the game, or be slaughtered by Krats the Hellhound.")
    print("To add to inventory: get 'item name'")
    print()

# Main game loop
current_room = "STAIRWELL"
show_instructions()

while True:
    print("You are in the", current_room)
    print("Items in the room:", items.get(current_room, "None"))

    # Check if player wants to pick up item in current room
    if current_room in items:
        choice = input("Do you want to pick up the {}? (yes/no): ".format(items[current_room])).lower()
        if choice == "yes":
            inventory.append(items[current_room])
            print("You picked up the", items[current_room], "and added it to your inventory.")

    # Check if player has all items
    if len(inventory) == len(items):
        print("Congratulations! You have collected all the items and defeated Krats the Hellhound. You win!")
        break

    direction = input("Enter a direction (North, South, East, West) or 'exit' to quit: ").capitalize()
    if direction == "Exit":
        print("Thank you for playing! Exiting the game.")
        break
    elif direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("Invalid direction! Please choose a valid direction.")