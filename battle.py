# Battle Functions
from random import choice, randint

def attack_turn(creature, opponent, attack_index):
    attack = creature['attacks'][attack_index]
    if attack['damage'] < 0:
        heal_amount = abs(attack['damage'])
        old_health = creature['health']
        creature['health'] = min(creature['health'] + heal_amount, creature['max_health'])
        print(f"{creature['name']} used {attack['name']} and healed {creature['health'] - old_health} HP!")
    else:
        print(f'{creature["name"]} used {attack["name"]} causing {attack["damage"]} damage!')
        opponent['health'] -= attack['damage']
        opponent['health'] = max(opponent['health'], 0)
    if opponent['health'] > 0:
        opp_attack = choice(opponent['attacks'])
        if opp_attack['damage'] < 0:
            heal_amount = abs(opp_attack['damage'])
            old_health = opponent['health']
            opponent['health'] = min(opponent['health'] + heal_amount, opponent['max_health'])
            print(f"{opponent['name']} used {opp_attack['name']} and healed {opponent['health'] - old_health} HP!")
        else:
            print(f'{opponent["name"]} used {opp_attack["name"]} causing {opp_attack["damage"]} damage!')
            creature['health'] -= opp_attack['damage']
            creature['health'] = max(creature['health'], 0)
    return creature, opponent

def process_victory(creature, opponent, level):
    print(f'{opponent["name"]} has been defeated!')
    if randint(1, 100) <= 30:
        heal = randint(10, 100)
        creature['health'] = min(creature['health'] + heal, creature['max_health'])
        print(f'You found a healing item! {creature["name"]} recovers {heal} health.')
    if randint(1, 100) <= 20:
        print(f'{opponent["name"]} wants to join your team!')
        creature = opponent.copy()
        creature['health'] = creature['max_health']
        print(f'Your new creature is now {creature["name"]}!')
    level += 1
    return creature, level

def process_defeat(creature):
    print(f'{creature["name"]} has been defeated!')
    print("Game Over")
    restart = input("Do you want to restart? (y/n): ").strip().lower()[0]
    if restart == "y":
        return True
    else:
        print("Thanks for playing!")
        exit()
