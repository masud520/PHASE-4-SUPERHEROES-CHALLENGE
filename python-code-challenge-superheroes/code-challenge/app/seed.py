from models import db, Power, Hero, HeroPower
import random

def seed_powers():
    print("🦸‍♀️ Seeding powers...")
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]
    powers = Power.create_all(powers_data)
    print("🦸‍♀️ Done seeding powers!")

def seed_heroes():
    print("🦸‍♀️ Seeding heroes...")
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]
    heroes = Hero.create_all(heroes_data)
    print("🦸‍♀️ Done seeding heroes!")

def add_powers_to_heroes():
    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()
    
    for hero in heroes:
        for _ in range(random.randint(1, 3)):
            power = Power.query.get(random.choice(Power.query.with_entities(Power.id).all()))
            HeroPower.create(hero=hero, power=power, strength=random.choice(strengths))
    print("🦸‍♀️ Done adding powers to heroes!")

def seed_database():
    seed_powers()
    seed_heroes()
    add_powers_to_heroes()
    print("🦸‍♀️ Done seeding!")

if __name__ == "__main__":
    seed_database()

