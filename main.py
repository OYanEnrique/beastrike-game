# Main Game Function
from random import choice, randint
from creatures import generate_creature
from ui import show_status, show_menu
from battle import attack_turn, process_victory, process_defeat

def main():
    user_name = str(input("Enter your character's name: "))
    level = 1
    creature = generate_creature(level)
    while True:
        opponent = generate_creature(level, nerf_opponent=True)
        while creature['health'] > 0 and opponent['health'] > 0:
            show_status(user_name, creature, opponent, level)
            choice_action = show_menu(creature)
            if choice_action == "1":
                creature, opponent = attack_turn(creature, opponent, 0)
                if opponent['health'] <= 0:
                    creature, level = process_victory(creature, opponent, level)
                    break
                if creature['health'] <= 0:
                    if process_defeat(creature):
                        level = 1
                        creature = generate_creature(level)
                        break
            elif choice_action == "2":
                creature, opponent = attack_turn(creature, opponent, 1)
                if opponent['health'] <= 0:
                    creature, level = process_victory(creature, opponent, level)
                    break
                if creature['health'] <= 0:
                    if process_defeat(creature):
                        level = 1
                        creature = generate_creature(level)
                        break
            elif choice_action == "3":
                print("Opening inventory...")
            elif choice_action == "4":
                print("Game saved.")
            else:
                print("Invalid choice. Please try again.")
        if creature['health'] <= 0:
            continue

if __name__ == "__main__":
    main()
