# Define a class named Pet to represent your digital pet
class Pet:
    # Constructor method: sets up the pet's initial state when the object is created
    def __init__(self, name):
        self.name = name          # Store the pet's name
        self.hunger = 5           # Hunger starts at 5 (0 = full, 10 = very hungry)
        self.energy = 5           # Energy starts at 5 (0 = tired, 10 = fully rested)
        self.happiness = 5        # Happiness starts at 5 (0 = sad, 10 = very happy)
        self.tricks = []          # Create an empty list to store tricks the pet learns

    # Method for feeding the pet
    def eat(self):
        # Decrease hunger by 3, but not below 0
        self.hunger = max(0, self.hunger - 3)
        # Increase happiness by 1, but not above 10
        self.happiness = min(10, self.happiness + 1)
        # Print a message showing the result
        print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    # Method for sleeping/resting
    def sleep(self):
        # Increase energy by 5, but cap at 10
        self.energy = min(10, self.energy + 5)
        # Print a message showing the result
        print(f"{self.name} slept. Energy: {self.energy}")

    # Method for playing with the pet
    def play(self):
        # Only allow playing if the pet has enough energy
        if self.energy >= 2:
            self.energy -= 2  # Playing uses 2 energy
            self.happiness = min(10, self.happiness + 2)  # Increase happiness
            self.hunger = min(10, self.hunger + 1)        # Playing increases hunger
            print(f"{self.name} played. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            # If too tired, the pet can't play
            print(f"{self.name} is too tired to play.")

    # Method to print the current status of the pet
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")       # Show hunger level
        print(f"Energy: {self.energy}")       # Show energy level
        print(f"Happiness: {self.happiness}") # Show happiness level

    # Bonus: Method to teach the pet a new trick
    def train(self, trick):
        self.tricks.append(trick)  # Add the trick to the tricks list
        print(f"{self.name} learned a new trick: {trick}!")  # Show confirmation

    # Bonus: Method to show all the tricks the pet has learned
    def show_tricks(self):
        if self.tricks:
            # If there are tricks, print them
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            # If no tricks learned yet
            print(f"{self.name} hasn't learned any tricks yet.")
