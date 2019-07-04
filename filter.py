import sys
import requests

uris = open('yahoo.txt', 'r').readlines()
for line in uris:
    sub = line.strip()
    try:
        http = requests.get('https://'+sub) 
        wfile = open('200.txt', 'w')
        wfile.write(sub)
        wfile.write("\n")
        wfile.close()
        print sub +" RESPONDE!!!"
        
    except:
        print sub +" no responde"
        pass


