# 🎮 The CSV "Step-Count" Auto-Battler

A Python text-based script that links real-world fitness data with automated RPG game mechanics.

## 📝 About the Project

Your character's **Health** and **Attack** scale dynamically based on the step counts retrieved from your personal fitness log. The more active you are in real life, the stronger your character becomes to face increasingly difficult monsters. Maintain a high step count to survive the arena and earn rare rewards!

## 🚀 How It Works

1. **Load Fitness Data:** The game reads your daily data sequentially from a local `health_data.csv` file.


2. **Stat Scaling:** For every day recorded, your stats are calculated based on your activity:


* **Daily Health:** Base Health (50) + 1 HP for every 1,000 steps walked.


* **Daily Attack:** Base Attack (50) + 1 Attack Point for every 2,000 steps walked.




3. **Automated Matchmaking:** The script automatically matches you against a monster based on your milestone tiers:


* **0 – 3,000 steps:** Goblin (Easy)


* **3,001 – 6,000 steps:** Orc (Medium)


* **6,001 – 9,000 steps:** Dragon (Hard)


* **9,001+ steps:** Juggernaut (Insane)




4. **The Battle System:** Turn-based combat loops until someone drops to $0$ HP. Winning grants gold, XP, and unique gear, while losing drops 275 gold pieces.


5. **Rare Drops & Reports:** Exceeding 10,000 steps unlocks an extra chance at a limited pool of rare loot (like Double XP or Gold Chests). At the end of the data file, a full report displays your final level, gold, inventory, and win/loss ratio.