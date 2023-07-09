
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 0
        self.contributing_attributes = []

    def generate_hunger_level(self):
        base_hunger_level = random.randint(0, 10)
        self.contributing_attributes = []

        # Adjust hunger level based on attributes
        if self.has_high_metabolism():
            base_hunger_level -= random.randint(0, 2)
            self.contributing_attributes.append("a high metabolism")
        
        if self.has_nutritional_deficiency():
            base_hunger_level += random.randint(0, 2)
            self.contributing_attributes.append("nutritional deficiency")
        
        if self.has_fluctuating_blood_sugar():
            base_hunger_level += random.randint(0, 2)
            self.contributing_attributes.append("fluctuating blood sugar levels")
        
        if self.has_elevated_ghrelin():
            base_hunger_level += random.randint(1, 3)
            self.contributing_attributes.append("elevated ghrelin levels")
        
        if self.has_elevated_stress():
            base_hunger_level += random.randint(0, 2)
            self.contributing_attributes.append("elevated stress levels")
        
        if self.has_lack_of_sleep():
            base_hunger_level += random.randint(0, 1)
            self.contributing_attributes.append("lack of sleep")
        
        if self.has_illness_or_medical_condition():
            base_hunger_level += random.randint(0, 2)
            self.contributing_attributes.append("an illness or medical condition")
        
        if self.has_stimulating_environmental_cues():
            base_hunger_level += random.randint(0, 1)
            self.contributing_attributes.append("stimulating environmental cues")
        
        if self.has_unbalanced_diet():
            base_hunger_level += random.randint(0, 1)

        # Limit the hunger level between 0 and 10
        self.hunger_level = max(0, min(base_hunger_level, 10))

    # Helper functions to simulate attributes (replace with appropriate logic)
    def has_high_metabolism(self):
        return random.choice([True, False])

    def has_nutritional_deficiency(self):
        return random.choice([True, False])

    def has_fluctuating_blood_sugar(self):
        return random.choice([True, False])

    def has_elevated_ghrelin(self):
        return random.choice([True, False])

    def has_elevated_stress(self):
        return random.choice([True, False])

    def has_lack_of_sleep(self):
        return random.choice([True, False])

    def has_illness_or_medical_condition(self):
        return random.choice([True, False])

    def has_stimulating_environmental_cues(self):
        return random.choice([True, False])

    def has_unbalanced_diet(self):
        return random.choice([True, False])

    def generate_reasoning(self):
        reasoning = ""
        if "a high metabolism" in self.contributing_attributes:
            reasoning += f"{self.name}'s high metabolism results in a lower hunger level. "
        
        if "nutritional deficiency" in self.contributing_attributes:
            reasoning += f"{self.name} has a nutritional deficiency, leading to increased hunger as the body craves more food to fulfill its nutrient requirements. "
        
        if "fluctuating blood sugar levels" in self.contributing_attributes:
            reasoning += f"{self.name} experiences fluctuations in blood sugar levels, causing changes in hunger sensations. "
        
        if "elevated ghrelin levels" in self.contributing_attributes:
            reasoning += f"{self.name} has elevated ghrelin levels, also known as the hunger hormone, which increases appetite. "
        
        if "elevated stress levels" in self.contributing_attributes:
            reasoning += f"{self.name} experiences elevated stress levels, triggering the release of cortisol and affecting hunger and appetite. "
        
        if "lack of sleep" in self.contributing_attributes:
            reasoning += f"{self.name} experiences a lack of sleep, which disrupts hunger-regulating hormones and leads to increased hunger. "
        
        if "an illness or medical condition" in self.contributing_attributes:
            reasoning += f"{self.name} has an illness or medical condition that affects metabolism and appetite. "
        
        if "stimulating environmental cues" in self.contributing_attributes:
            reasoning += f"{self.name} is surrounded by stimulating environmental cues like the smell or sight of food, which can increase hunger. "
        
        if "an unbalanced diet" in self.contributing_attributes:
            reasoning += f"{self.name}'s unbalanced diet lacking essential nutrients can lead to increased hunger as the body craves the missing nutrients. "
        
        if reasoning == "":
            reasoning = f"No specific factors contributing to {self.name}'s hunger were identified."

        return reasoning

    def decide_to_eat(self):
        if self.hunger_level >= 5:
            if random.random() < 0.7:
                return True
        return False

# Game setup
characters = []
character_names = []

# Add characters
num_characters = int(input("Enter the number of characters: "))
for i in range(num_characters):
    name = input(f"Enter name for Character {i+1}: ")
    character = Character(name)
    characters.append(character)
    character_names.append(name)

# Play the game
while True:
    print("\n=== Game Start ===")
    for character in characters:
        character.generate_hunger_level()
        print(f"\n{character.name}'s initial hunger level: {character.hunger_level}")

        if character.hunger_level >= 5:
            print(f"{character.name} is feeling hungry. The following factors contribute to their hunger:")
            for attribute in character.contributing_attributes:
                print("- " + attribute)

            reasoning = character.generate_reasoning()
            print("\nReasoning behind", character.name + "'s hunger:")
            print(reasoning)

            if character.decide_to_eat():
                print(f"\n{character.name} has decided to eat.")
                character.hunger_level -= random.randint(1, 3)  # Decrease hunger level by a random value between 1 and 3 after eating
                if character.hunger_level <= 0:
                    character.hunger_level = 0
                print(f"{character.name}'s hunger level after eating: {character.hunger_level}")
            else:
                print(f"\n{character.name} has decided not to eat because they don't feel the need to at the moment.")
        else:
            print(f"{character.name} is not feeling hungry.")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("\nGame Over. Thank you for playing!")