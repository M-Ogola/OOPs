class Character:
    """
    Base Class: Think of this as the OG blueprint. 
    Every character (normal or superhero) gets their sauce from here. 
    """
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
        self.is_retired = False
        print(f"✨ A wild character appears! {self.name} is officially in the game. 🎮") 

    def display_info(self): 
        """Spills the tea on who this character really is.""" 
        status = "🛋️ Retired" if self.is_retired else "⚡ Active"
        print(f"\n--- {self.name} ---")
        print(f"🔥 Power: {self.power}")
        print(f"❤️ Health: {self.health}")
        print(f"📊 Status: {status}")

    def take_damage(self, amount: int):
        """Ouch. Life bar goes down when this is called."""
        if self.health > 0:
            self.health -= amount
            print(f"💥 {self.name} just took {amount} damage. Remaining HP: {self.health}")
        if self.health <= 0:
            self.health = 0
            self.is_retired = True
            print(f"💀 RIP {self.name}, retired from the streets.")


class Superhero(Character):
    """
    Subclass: Extends Character. Adds that cape-drip + unique moves. 
    Basically, the glow-up version of Character.
    """
    def __init__(self, name: str, power: str, health: int, cape_color: str):
        super().__init__(name, power, health)
        self.cape_color = cape_color

    def display_info(self):
        """Same tea, but now we flex the cape too. ✨"""
        super().display_info()
        print(f"🦸 Cape Drip: {self.cape_color}")

    def perform_heroic_act(self, location: str):
        """Hero moment. Unless... you’re retired sipping chai."""
        if not self.is_retired:
            print(f"🌟 {self.name} zooms off to {location} like ‘hold up fam, I got this!’")
        else:
            print(f"☕ {self.name} is done saving lives. Currently chilling.")


# --- Assignment 1 Demo ---
print("\n--- [Assignment 1: Superhero Class Demo ✨] ---")
marvelous_man = Superhero(
    name="Marvelous Man",
    power="Super Speed",
    health=150,
    cape_color="Crimson Red"
)

marvelous_man.display_info()
marvelous_man.perform_heroic_act("The City Center")
marvelous_man.take_damage(50)
marvelous_man.perform_heroic_act("The North Bridge")


# ----------------------------------------------------------------------
# Activity 2: Polymorphism Challenge (aka the 'move' drip test 🚗✈️⛵)
# ----------------------------------------------------------------------

class Vehicle:
    """Base vibe. Forces subclasses to tell us: how do YOU move?"""
    def move(self):
        raise NotImplementedError("Bruh, every ride gotta explain its vibe. 🚦")


class Car(Vehicle):
    """Car = streets edition."""
    def move(self):
        return "🚗 Skrrr skrrr! Cruising the streets with that 4-wheel drip."


class Plane(Vehicle):
    """Plane = sky edition."""
    def move(self):
        return "✈️ Up, up, and away! Cloud-surfing like a boss."


class Boat(Vehicle):
    """Boat = ocean edition."""
    def move(self):
        return "⛵ Smooth waves only. Captain vibes unlocked."


def run_polymorphism_challenge(vehicles_list):
    """
    Polymorphism in action: Same call, different vibes. 
    No questions asked, just *move()*.
    """
    print("\n--- [Activity 2: Polymorphism Demo 🌍] ---")
    for vehicle in vehicles_list:
        print(f"🚦 {vehicle.__class__.__name__} says: {vehicle.move()}")


# --- Activity 2 Demo ---
vehicles_for_the_day = [Car(), Plane(), Boat()]
run_polymorphism_challenge(vehicles_for_the_day)
