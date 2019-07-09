# Brief Documentation #
#   Must be run on admin/sudo mode
#   change the hosts variable according to to the location of your Host file:
#       Windows: rC:\Windows\System32\drivers\etc\hosts
#       Mac/Linux:  /etc/hosts
#   Add the website to be blocked on site-list.txt file
# End of Brief Documentation #

# Libraries
import time
from datetime import datetime as dt

# Hosts variables
hosts_path="hosts"
redirect = "127.0.0.1"
website_list = "site-list.txt"

# Script variables
curTime = dt.now()
startTime = dt(curTime.year, curTime.month, curTime.day, 8) # Start of blocking time
endTime = dt(curTime.year, curTime.month, curTime.day, 16) # End of blocking time

# Start script #

# Infinite loop (makes the program run automatically)
while True:
    
    # Check the if the current time is between the start and end blocking time
    if startTime < curTime < endTime:
        print ("Working hours...")
        with open(hosts_path, 'r+') as file: # open host file
            content = file.read() # read the content and assign to the variable
            with open(website_list, 'r') as srcFile: # open the website list
                websites = [line.rstrip('\n') for line in srcFile] # save the content line-by-line to the variable
                for website in websites: 
                    if website in content: # check if the list was already written
                        pass
                    else:
                        file.write(redirect + " " + website + "\n") # write each website on the list
    else:
        print ("Fun hours...")
    
    # check time
    time.sleep(5)

# End script #