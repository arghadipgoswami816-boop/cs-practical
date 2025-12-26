#1) Dice simulator

import random
import sys
def roll_dice():
    """Simulates rolling a 6-sided die and returns the result."""
    return random.randint(1, 6)

while True:
      user_input = input(" *")
      if user_input == 'exit':
            print("Exiting the simulator. Goodbye!")
            sys.exit()
      elif user_input == '':
            result = roll_dice()
            print("You rolled a:", result)
      else:
        print("Invalid command. Press Enter to roll or type 'exit' to quit.")


     
