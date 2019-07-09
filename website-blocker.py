# Libraries
import time
from datetime import datetime as dt

# Variables #
# Hosts variables
hosts_path=r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = "site-list.txt"

# Script variables
curTime = dt.now()
startTime = dt(curTime.year, curTime.month, curTime.day, 8) # Start of blocking time
endTime = dt(curTime.year, curTime.month, curTime.day, 16) # End of blocking time

# Start script #

# Infinite loop (makes the program run automatically)
while True:
    
    if startTime < curTime < endTime:
        print ("Working hours...")
    else:
        print ("Fun hours...")
    
    # check time
    time.sleep(5)

# End script #