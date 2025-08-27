# UI Functions

def show_status(user_name, creature, opponent, level):
    print(f"{user_name.capitalize()}: Creature name: {creature['name']}, Health: {creature['health']}/{creature['max_health']}")
    print(f"--- Level {level} ---")
    print(f"You are facing {opponent['name']}!")
    print(f"Your creature {creature['name']} has {creature['health']} health remaining.")
    print(f"Your opponent {opponent['name']} has {opponent['health']} health remaining.")

def show_menu(creature):
    print(f"""
    What will you do?
    1. Attack 1: {creature['attacks'][0]['name']} (Damage: {creature['attacks'][0]['damage']})
    2. Attack 2: {creature['attacks'][1]['name']} (Damage: {creature['attacks'][1]['damage']})
    3. Inventory
    4. Save
    """)
    return input("Choose an action: ").strip()[0]
