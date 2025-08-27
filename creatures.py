# Creature Generator
from random import randint, choice

def generate_creature(player_level, nerf_opponent=False):
    creature_names = [
        "Flamix", "Aquaphoon", "Thornox", "Glimmowl", "Voltrake", "Pyrobit", "Frostail", "Lumifin", "Terrapod", "Mystwing",
        "Zaplume", "Leaflix", "Quillix", "Blazorb", "Shadune", "Pebblin", "Vynox", "Dracoon", "Squalix", "Plasmole",
        "Sparkfin", "Brambowl", "Cryonix", "Emberlyn", "Twilix", "Rubblet", "Vortexa", "Petalune", "Scalix", "Gustail",
        "Mosskit", "Flarrow", "Toxleaf", "Glacira", "Duskite", "Bouldash", "Wavern", "Plumite", "Cindrix", "Furrune",
        "Ravix", "Blossowl", "Stonix", "Vapowl", "Pyrolyn", "Thundune", "Frostrix", "Luminox", "Terrix", "Mystix",
        "Zapkit", "Leafowl", "Quillune", "Blazix", "Shadix", "Pebblix", "Vynix", "Dracix", "Squalune", "Plasmix",
        "Sparkowl", "Brambix", "Cryowl", "Emberix", "Twilune", "Rubblex", "Vortix", "Petalix", "Scalune", "Gustix",
        "Mossowl", "Flarix", "Toxix", "Glacix", "Duskit", "Bouldix", "Wavix", "Plumit", "Cindix", "Furrix",
        "Ravune", "Blossix", "Stonune", "Vapix", "Pyronix", "Thundix", "Frostrix", "Luminix", "Terrune", "Mystune",
        "Zapune", "Leafune", "Quillkit", "Blazune", "Shadkit", "Pebblune", "Vynkit", "Dracune", "Squalkit", "Plasmkit"
    ]
    opponent_attacks = [
        "Punch", "Kick", "Headbutt", "Magic", "Fireball", "Ice Blast", "Thunder Strike", "Poison", "Bite", "Scratch",
        "Claw", "Tail Whip", "Wing Attack", "Roar", "Scream", "Stomp", "Charge", "Ram", "Slash", "Pierce",
        "Venom Spit", "Acid Spray", "Shadow Sneak", "Dark Pulse", "Light Beam", "Water Jet", "Earthquake", "Sandstorm", "Wind Gust", "Blizzard",
        "Meteor", "Solar Flare", "Moonlight", "Starfall", "Gravity Crush", "Psychic", "Confuse", "Hypnosis", "Sleep", "Dream Eater",
        "Drain", "Leech", "Absorb", "Regenerate", "Heal", "Curse", "Bless", "Barrier", "Reflect", "Counter",
        "Double Hit", "Triple Strike", "Quad Slash", "Spin Attack", "Dive", "Surf", "Fly", "Teleport", "Blink", "Phase",
        "Explosion", "Implode", "Sonic Boom", "Echo", "Vibrate", "Pulse", "Shock", "Zap", "Spark", "Flash",
        "Growl", "Howl", "Snarl", "Bark", "Meow", "Pounce", "Ambush", "Sneak", "Steal", "Mug",
        "Throw", "Catch", "Trap", "Bind", "Wrap", "Squeeze", "Crush", "Smash", "Break", "Shatter"
    ]
    # Dicionário de dano fixo para cada ataque
    attack_damage = {
        "Punch": 8, "Kick": 10, "Headbutt": 12, "Magic": 15,
        "Fireball": 16, "Ice Blast": 14, "Thunder Strike": 17, "Poison": 13, "Bite": 11, "Scratch": 9,
        "Claw": 12, "Tail Whip": 10, "Wing Attack": 13, "Roar": 8, "Scream": 7, "Stomp": 14, "Charge": 15, "Ram": 13, "Slash": 12, "Pierce": 11,
        "Venom Spit": 13, "Acid Spray": 14, "Shadow Sneak": 15, "Dark Pulse": 16, "Light Beam": 15, "Water Jet": 13, "Earthquake": 18, "Sandstorm": 14, "Wind Gust": 12, "Blizzard": 17,
        "Meteor": 20, "Solar Flare": 19, "Moonlight": 10, "Starfall": 18, "Gravity Crush": 17, "Psychic": 16, "Confuse": 8, "Hypnosis": 7, "Sleep": 0, "Dream Eater": 15,
        "Drain": 10, "Leech": 9, "Absorb": 8, "Regenerate": -10, "Heal": -15, "Curse": 12, "Bless": 0, "Barrier": 0, "Reflect": 0, "Counter": 10,
        "Double Hit": 16, "Triple Strike": 24, "Quad Slash": 32, "Spin Attack": 14, "Dive": 13, "Surf": 15, "Fly": 12, "Teleport": 0, "Blink": 0, "Phase": 0,
        "Explosion": 25, "Implode": 22, "Sonic Boom": 18, "Echo": 8, "Vibrate": 7, "Pulse": 10, "Shock": 12, "Zap": 13, "Spark": 11, "Flash": 9,
        "Growl": 6, "Howl": 7, "Snarl": 8, "Bark": 6, "Meow": 5, "Pounce": 10, "Ambush": 12, "Sneak": 8, "Steal": 0, "Mug": 0,
        "Throw": 10, "Catch": 0, "Trap": 11, "Bind": 10, "Wrap": 9, "Squeeze": 12, "Crush": 15, "Smash": 14, "Break": 13, "Shatter": 16
    }
    attack1 = choice(opponent_attacks)
    attack2 = choice([atk for atk in opponent_attacks if atk != attack1])
    if nerf_opponent:
        nerf_factor = 0.8
        max_health = int((randint(50, 90) + (player_level * 5)) * nerf_factor)
        damage1 = int(attack_damage.get(attack1, 10) * nerf_factor)
        damage2 = int(attack_damage.get(attack2, 10) * nerf_factor)
    else:
        max_health = randint(50, 90) + (player_level * 5)
        damage1 = attack_damage.get(attack1, 10)
        damage2 = attack_damage.get(attack2, 10)
    generated_opponent = {
        "name": choice(creature_names),
        "health": max_health,
        "max_health": max_health,
        "attacks": [
            {"name": attack1, "damage": damage1},
            {"name": attack2, "damage": damage2}
        ],
        "level": player_level,
        "experience": 0
    }

    return generated_opponent