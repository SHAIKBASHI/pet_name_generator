import random
adjectives = ["Velvet", "Luna", "Royal", "Coco", "Pearl", "Silky", "Sunny", "Mocha"]
animals = ["Panda", "Lizard", "Unicorn", "Goat", "Chicken", "Penguin", "Snail", "Frog"]
suffixes = ["Belle", "Dior", "Aurora", "Chanel", "Luxe", "Nova", "Beau", "Milo"]

print("✨ Your 10 Fancy Pet Names Are:\n")

pet_name=random.choice(adjectives)+" "+random.choice(animals)+" "+random.choice(suffixes)
for i in range(10):
    pet_name = random.choice(adjectives) + " " + random.choice(animals) + " " + random.choice(suffixes)
    print(f"{i + 1}. {pet_name}")

  
