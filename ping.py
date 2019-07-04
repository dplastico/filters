import os
import sys

uris = open("yahoo.txt", 'r').readlines()
newfile = open("alive.txt", 'w') 

for line in uris:
    sub = line.strip()
    try:
        response = os.system('ping -c 1 '+sub+ '2>/dev/null') 
        if response == 0:
            print sub + "not ok"
        else:
            newfile.write(sub)
            newfile.write("\n")
    except:
        pass
