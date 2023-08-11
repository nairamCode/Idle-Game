# PLAN #
# Start
    # Create a window
    # Update your kps and amount count via a file
# Let the Player
    # Buy, Sell Addons (like fabrics, workers...)
# Update your amount every second
# When closed
    # Store kps and amount count in a file
import os
import tkinter as tk

class idle_game():
    
    def run():
        # Create a window
        root = tk.Tk()
        root.title('nairams idle game') # Window Titel
        root.geometry('600x400+50+50') # Window mesurements
        root.resizable(False, False)
        root.mainloop()
        # Update your kps and amount count via a file
        # Let the Player
            # Buy, Sell Addons (like fabrics, workers...)
        # Update your amount every second
        # When closed
            # Store kps and amount count in a file

    def read_data():
        # Open file
        # Read the amounts
        # Set variables to these amounts
        pass

    def save_data():
        # Open file
        # overwrite amounts from the variables
        pass

idle_game.run()