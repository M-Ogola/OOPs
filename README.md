# OOPs
# 🦸 Superhero & Polymorphism Demo

## 📌 Description
This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, split into two parts:

1. **Assignment 1: Superhero Class**
   - Create your own class with attributes and methods.
   - Add inheritance by extending the base `Character` class into a `Superhero` subclass.
   - Demonstrate polymorphism by overriding a method (`display_info`).

2. **Activity 2: Polymorphism Challenge**
   - Define a base class (`Vehicle`) with a method `move()`.
   - Create multiple subclasses (`Car`, `Plane`, `Boat`) that each implement `move()` differently.
   - Run them together to show polymorphism in action.

---

## 🧩 Assignment 1: Superhero Class

### Classes
- **`Character`**
  - Attributes: `name`, `power`, `health`, `is_retired`.
  - Methods: `display_info()`, `take_damage()`.
- **`Superhero`** (inherits from `Character`)
  - Extra attribute: `cape_color`.
  - Overridden method: `display_info()`.
  - Unique method: `perform_heroic_act(location)`.

### Demo Flow
1. Create a `Superhero` object called **Marvelous Man**.
2. Display its info.
3. Perform a heroic act in a location.
4. Take damage and update health.
5. Perform another heroic act.

---

## 🎭 Activity 2: Polymorphism Challenge

### Classes
- **`Vehicle`** (base class, defines `move()` contract).
- **`Car`** → `"🚗 Driving on four wheels, Vroom Vroom!"`
- **`Plane`** → `"✈️ Flying high above the clouds, Weeeeee!"`
- **`Boat`** → `"⛵ Cruising smoothly across the water. Ahoy!"`

### Demo Flow
- Put all vehicles (`Car`, `Plane`, `Boat`) into a list.
- Loop through them and call `move()`.
- Each subclass responds differently → **polymorphism in action**.

---

## ▶️ How to Run
1. Save the code in a file, e.g., `superhero_demo.py`.
2. Run in terminal or command prompt:
   ```bash
   python superhero_demo.py

Example Output
--- [Assignment 1: Superhero Class Demo] ---
💫 Character created: Marvelous Man is ready for action.

--- Marvelous Man ---
Power: Super Speed
Health: 150
Status: Active
Cape Color: Crimson Red

🌟 Marvelous Man swiftly flies to The City Center to save the day!
💥 Marvelous Man took 50 damage. Health remaining: 100
🌟 Marvelous Man swiftly flies to The North Bridge to save the day!

--- [Activity 2: Polymorphism Demo] ---
Vehicle Type: Car | Action: 🚗 Driving on four wheels, Vroom Vroom!
Vehicle Type: Plane | Action: ✈️ Flying high above the clouds, Weeeeee!
Vehicle Type: Boat | Action: ⛵ Cruising smoothly across the water. Ahoy!

