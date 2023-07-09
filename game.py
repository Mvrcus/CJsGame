import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 0
        self.contributing_attributes = []

    def generate_hunger_level(self):
        base_hunger_level = random.randint(0, 10)

        # Adjust hunger level based on attributes
        if self.has_high_metabolism():
            base_hunger_level -= random.randint(0, 2)
            self.contributing_attributes.append("a high metabolism")

        if self.has_nutritional_deficiency():
            base_hunger_level += random.randint(0, 2)
            self.contributing_attributes.append("nutritional deficiency")

        # Limit the hunger level between 0 and 10
        self.hunger_level = max(0, min(base_hunger_level, 10))

    # Helper functions to simulate attributes (replace with appropriate logic)
    def has_high_metabolism(self):
        return random.choice([True, False])

    def has_nutritional_deficiency(self):
        return random.choice([True, False])

    def generate_reasoning(self):
        reasoning = ""
        if "a high metabolism" in self.contributing_attributes:
            reasoning += f"{self.name}'s high metabolism results in a lower hunger level. "

        if "nutritional deficiency" in self.contributing_attributes:
            reasoning += f"{self.name} has a nutritional deficiency, leading to increased hunger as the body craves more food. "

        if reasoning == "":
            reasoning = f"No specific factors contributing to {self.name}'s hunger were identified."

        return reasoning

    def decide_to_eat(self):
        if self.hunger_level >= 5:
            if random.random() < 0.7:
                return True
        return False

def main():
    # Game setup
    characters = []
    num_characters = int(input("Enter the number of characters: "))

    # Add characters
    for i in range(num_characters):
        name = input(f"Enter name for Character {i+1}: ")
        character = Character(name)
        characters.append(character)

    # Play the game for three days
    for day in range(1, 4):
        input(f"\nPress Enter to start Day {day}...")
        print(f"\n=== Day {day} Start ===")
        for character in characters:
            character.generate_hunger_level()
            print(f"\n{character.name}'s initial hunger level: {character.hunger_level}")

            if character.hunger_level >= 5:
                print(f"{character.name} is feeling hungry.")

                reasoning = character.generate_reasoning()
                print("\nReasoning behind", character.name + "'s hunger:")
                print(reasoning)

                if character.decide_to_eat():
                    print(f"\n{character.name} has decided to eat.")
                    character.hunger_level -= random.randint(1, 3)  # Decrease hunger level by a random value between 1 and 3 after eating
                    if character.hunger_level <= 0:
                        character.hunger_level = 0
                    print(f"{character.name}'s hunger level after eating: {character.hunger_level}")
                    character.generate_hunger_level()  # Regenerate attributes if character eats
                else:
                    print(f"\n{character.name} has decided not to eat because they don't feel the need to at the moment.")
            else:
                print(f"{character.name} is not feeling hungry.")

        if day < 3:
            input("\nPress Enter to continue to the next day...")

    play_again = input("\nWould you like to continue playing? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("\nGame Over. Thank you for playing!")

if __name__ == "__main__":
    main()
