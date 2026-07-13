# ---------------------------------- The CSV "Step-Count" Auto-Battler (Intermediate) ----------------------------------

# \\\\ Modules ////

import csv
import random
import time

# \\\\ Variables ////

character_progress = {
    "base_health" : 50,
    "base_attack" : 50,
    "current_level" : 0,
    "total_xp" : 0,
    "gold_earned": 0,
    "loot_inventory" : [],
    "wins" : 0,
    "deaths" : 0
}

monsters_list = [
{
    "name" : "Goblin",
    "base_health" : 30,
    "current_health" : 30,
    "attack" : 10,
    "difficulty" : "easy"
},
{
    "name" : "Orc",
    "base_health" : 50,
    "current_health" : 50,
    "attack" : 30,
    "difficulty" : "medium"

},
{
    "name" : "Dragon",
    "base_health" : 70,
    "current_health" : 70,
    "attack" : 50,
    "difficulty" : "hard"

},
{
    "name" : "Juggernaut",
    "base_health" : 100,
    "current_health" : 100,
    "attack" : 80,
    "difficulty" : "insane"

}]

Rare = ["Double XP", "Gold Chest", "Double HP"]

# \\\\ Functions ////


def boss_damage(index):

    DamageToPlayer =  random.randint(1, monsters_list[index]["attack"])

    global daily_health

    daily_health -= DamageToPlayer

    time.sleep(1)


def character_damage(index):

    global daily_attack

    DamageToBoss = random.randint(30, daily_attack)

    monsters_list[index]["current_health"] -= DamageToBoss

    time.sleep(1)


def WinOrLose(index):

    global daily_health

    if daily_health > 0 and monsters_list[index]["difficulty"] == "easy":

        print("Victory ! That was easy.")

        character_progress["wins"] += 1
        character_progress["total_xp"] += 250
        character_progress["gold_earned"] += 100

        LootEarned1 = "speed potion"

        if LootEarned1 not in character_progress["loot_inventory"]:

            character_progress["loot_inventory"].append(LootEarned1)
    
    elif daily_health > 0 and monsters_list[index]["difficulty"] == "medium":

        print("Victory ! That was good.")

        character_progress["wins"] += 1
        character_progress["total_xp"] += 500
        character_progress["gold_earned"] += 250

        LootEarned2 ="golden bow"

        if LootEarned2 not in character_progress["loot_inventory"]:

            character_progress["loot_inventory"].append(LootEarned2)
    
    elif daily_health > 0 and monsters_list[index]["difficulty"] == "hard":

        print("Victory ! That was hard")

        character_progress["wins"] += 1
        character_progress["total_xp"] += 750
        character_progress["gold_earned"] += 500

        LootEarned3 ="grenades"
    
        if LootEarned3 not in character_progress["loot_inventory"]:

            character_progress["loot_inventory"].append(LootEarned3)
    
    elif daily_health > 0 and monsters_list[index]["difficulty"] == "insane":

        print("Victory ! You killed the powerful boss in the game.")

        character_progress["wins"] += 1
        character_progress["total_xp"] += 2000
        character_progress["gold_earned"] += 1000

        LootEarned4 ="powered sword"

        if LootEarned4 not in character_progress["loot_inventory"]:

            character_progress["loot_inventory"].append(LootEarned4)

    else: 

        character_progress["deaths"] += 1
        character_progress["gold_earned"] -= 275

        print("275 coins felt from you bag. You gain 0 XP. Try harder")

    if daily_health > 0:
            
        print(f"You have {", ".join(character_progress['loot_inventory'])} in your inventory.")


def BattleStatus(index):
            
    global daily_health

    while daily_health > 0 and monsters_list[index]["current_health"] > 0:
                
        character_damage(index)
        
        if monsters_list[index]["current_health"] <= 0:

            print(f"You killed the {monsters_list[index]["name"]}")

            break
            
        boss_damage(index)

        if daily_health <= 0:

            print(f"The {monsters_list[index]["name"]} killed you")

            break

        time.sleep(2)

    WinOrLose(index)

    monsters_list[index]["current_health"] = monsters_list[index]["base_health"]

    

with open(r"health_data.csv", "r") as h:

    data = csv.DictReader(h)

    for row in data:
        
        date = row['Date']

        steps = int(row['Steps'])

        if steps >= 10000:

            print("<- You have earned a rare loot drop for walking more than 10,000 steps ! Available after upcoming battle ->")

        daily_health = character_progress["base_health"] + (steps // 1000)
        daily_attack = character_progress["base_attack"] + (steps // 2000)
        time.sleep(1)

# ----------------------- Start of the battle -----------------------

        print("-" * 50,"A new battle has started !", "-" * 50, sep="\n")

        if steps >= 0 and steps <= 3000 :

            BattleStatus(0)
        
        if steps > 3000 and steps <= 6000 :

            BattleStatus(1)

        if steps > 6000 and steps <= 9000 :

            BattleStatus(2)

        if steps > 9000 :

            BattleStatus(3)

            time.sleep(2)
            
            dots = "....."

            print("Opening the rare loot drop: ", end="")

            for dot in dots:

                print(dot, end="", flush=True)
            
                time.sleep(1)

            print(".")

            if len(Rare) > 0:
    
                random_loot = random.choice(Rare)

                print(f"Congrats ! You earned {random_loot}")

                character_progress["loot_inventory"].append(random_loot)

                Rare.remove(random_loot)

        time.sleep(3)

    CurrentXP = character_progress["total_xp"]

    character_progress["current_level"] = min( CurrentXP // 2000, 5)


h.close()

wins = character_progress["wins"]
deaths = character_progress["deaths"]


print("-" * 40, "Weekly Report", "-" * 40, sep=" "  )
print(f"Your current level is {character_progress['current_level']}")
print(f"You have gathered {character_progress['gold_earned']} coins for now")
print(f"You inventory has {", ".join(character_progress['loot_inventory'])}")
print(f"You made {wins} wins : {deaths} deaths for your fitness. ")