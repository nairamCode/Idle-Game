# PLAN #
# Start
    # Create a window
    # Update your kps and amount count via a file
# Let the Player
    # Buy, Sell Addons (like fabrics, workers...)
# Update your amount every second
'''     
    money = str(money + 10)
    kps = str(kps + 10)
'''
# When closed
    # Store kps and amount count in a file
import os
import tkinter as tk
import time

class idle_game():
    
    def run():
        global money
        global kps
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
        global money, kps
        # Open file
        money_open_file = open('money.txt', 'r')
        kps_open_file = open('kps.txt', 'r')
        # Read the amounts and set variables to these amounts
        money = int(money_open_file.read())
        kps = int(kps_open_file.read())

    def save_data():
        global money
        global kps
        # Open file
        money_open_file = open('money.txt', 'w')
        kps_open_file = open('kps.txt', 'w')
        # overwrite amounts from the variables
        money_open_file.write(str(money))
        kps_open_file.write(str(kps))

idle_game.run()