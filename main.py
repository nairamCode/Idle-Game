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
    
# GAME IDEA #
'''
1. Idle Game where you produce and sell goods
2. Sell Item: Pen, Paper
3. Produce One Item by pressing a button
4. Sell one Item by pressing a button
5. Goal: Sell as many Items as you can
6. Things to keep track of:
	a) Suply and Demand (pens/paper)
		The suply and demand starts at 1/5
        if you by one pen the suply for pens goes down but the suply for paper goes up 0/2
        if you then sell those 2 paper the suply for pens goes up again 2/0
    b) Price
    	The Price Starts at 0,30€ per Item
        The Demand for Free Items is at 100% -> If someone wants a Item he will buy it
        If The Price is at 1€ per Item the Demand is at 0% -> No one buys it
        You can Change the Price but higher price = lower demand
        Demande (in %) = (1 - Price) * 100
    c) Production Cost
    	The Production Cost starts at 0,30€
        Lower Production Cost = higher chance for an nonfunctional item
        If an product is nonfunctional you can't sell it
        Failure Chance = -1.225 * Production Price + 1.1125
	d) Storage
    	Your Storage starts at 1000
        higher Item Amount = lower cost per Product
        
'''
import os

class idle_game():
    def run():
        global money, kps
		idle_game.read_data()
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
        global money, kps
        # Open file
        money_open_file = open('money.txt', 'w')
        kps_open_file = open('kps.txt', 'w')
        # overwrite amounts from the variables
        money_open_file.write(str(money))
        kps_open_file.write(str(kps))

idle_game.run()