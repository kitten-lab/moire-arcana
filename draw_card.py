import json
import random

with open("major_arcana.json") as f:
    cards = json.load(f)

card = random.choice(cards)

print(card["number"])
print(card["name"])
print(card["definition"])
print(card["symbols"])
